import random
import string

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.http import HttpResponseRedirect, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from shortener.forms import HomeForm
from shortener.models import Site
from urllib.parse import urlparse
from django.contrib import messages


def generate_secret_url():
    letters = string.ascii_letters
    secret = ''.join(random.choice(letters) for i in range(10))
    if Site.objects.filter(secret_url=secret).exists():
        generate_secret_url()
    return secret


def validate_website_url(website):
    """Validate website into valid URL"""
    msg = "Cannot validate this website: %s" % website
    validate = URLValidator(message=msg)
    try:
        validate(website)
    except:
        o = urlparse(website)
        if o.path:
            path = o.path
            while path.endswith('/'):
                path = path[:-1]
            path = "http://"+path
            validate(path)
            return path
        else:
            raise ValidationError(message=msg)
    return website


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        form = HomeForm()
        sites = Site.objects.filter(user=request.user.id)
        user = request.user

        args = {
            'form': form, 'sites': sites, 'users': user, 'domain': request.META['HTTP_HOST']
        }

        return render(request, self.template_name, args)

    def post(self, request):
        url = ''
        form = HomeForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user

            url = form.cleaned_data['url']
            if not validate_website_url(url):
                messages.info(request, "Invalid URL.")
                return redirect('home')

            secret_url = generate_secret_url()

            data.secret_url = secret_url
            data.click_count = 0
            data.save()

            return redirect('home')

        sites = Site.objects.filter(user=request.user.id)

        args = {'form': form, 'text': url, 'sites': sites, 'domain': request.META['HTTP_HOST']}
        return render(request, self.template_name, args)


def redirect_to_secret_website(request, secret_url):
    try:
        website = Site.objects.get(secret_url=secret_url)
        website.click_count += 1
        website.save()
        return HttpResponseRedirect("https://{}".format(website.url))
    except Site.DoesNotExist:
        return render(request, '404.html')
