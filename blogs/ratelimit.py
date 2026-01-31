from django_ratelimit.decorators import ratelimit
from django.http import JsonResponse

def rate_limit_response(limit, window_seconds, context="requests"):
    return JsonResponse({
        "error": "rate_limit_exceeded",
        "message": f"You have exceeded the limit of {limit} {context} per {window_seconds//60} minute(s). "
                   f"Please wait {window_seconds} seconds before retrying.",
        "retry_after_seconds": window_seconds
    }, status=429)

contact_rate_limit = {
    "decorator": ratelimit(key='ip', rate='5/m', block=False),
    "limit": 5,
    "window": 60,
    "context": "contact form submissions"
}

login_rate_limit = {
    "decorator": ratelimit(key='ip', rate='3/m', block=False),
    "limit": 3,
    "window": 60,
    "context": "login attempts"
}