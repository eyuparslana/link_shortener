from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.forms import (
    RegistrationForm
)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
        else:
            return redirect('register')

    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'registration/register.html', args)