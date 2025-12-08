from django.urls import path
from . import views


app_name='main'

urlpatterns=[
    path("", views.home, name='blog-home'),
    path("detail/<str:slug>", views.details, name='blog-detail'),
    path("contact/", views.contact, name='blog-contact'),
    path("about/", views.about_us, name='blog-about'),
    path("register/", views.register, name='blog-register'),
    
   
    
    ]