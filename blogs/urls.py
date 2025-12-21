from django.urls import path
from . import views


app_name='main'

urlpatterns=[
    path("", views.home, name='home'),
    path("detail/<str:slug>", views.details, name='detail'),
    path("contact/", views.contact, name='contact'),
    path("about/", views.about_us, name='about'),
    path("register/", views.register, name='register'),
    path("login/", views.login_view, name='login'),
    path("dashboard/", views.dashboard_view, name='dashboard'),
    path("logout/", views.logout_view, name='logout'),
    path("forgot_password/", views.forgot_password, name='forgot_password'),
    path('reset_password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    path('newpost/', views.newpost, name='newpost'),
    path('editpost/<int:post_id>/', views.editpost, name='editpost'),
    path('deletepost/<int:post_id>/', views.deletepost, name='deletepost'),
    path('publish/<int:post_id>/', views.publish_post, name='publish_post'),



    
    
   
    
    ]