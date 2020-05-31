from django.urls import path, re_path

from shortener import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    re_path('(?P<secret_url>^[a-zA-Z]{10}$)', views.redirect_to_secret_website, name='secret')
]
