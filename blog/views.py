from django.shortcuts import render,redirect

def custom_handler(request, exception):
    return render(request, '404.html', status=404)