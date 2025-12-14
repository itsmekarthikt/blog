from django.shortcuts import redirect, reverse

class RedirectAuthmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        #check if user is authenticated and trying to access login or register page
        if request.user.is_authenticated and request.path in [reverse("main:login"), reverse("main:register")]:
            # if authenticated and try to acess login and register page, redirect to dashboard
            return redirect("main:dashboard")

        return response
    

class RestricUnauthendicatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Restrict unauthenticated users from accessing dashboard
        if not request.user.is_authenticated and request.path in [reverse("main:dashboard")]:
            return redirect("main:login")
        
        return response