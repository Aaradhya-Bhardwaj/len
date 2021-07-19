from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('length', views.length, name='length'),
    path('contact', views.contact, name='contact')
]
