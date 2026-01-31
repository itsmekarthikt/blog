# blogs/utils.py
from django.http import JsonResponse

def rate_limit_response(limit, window_seconds, context="requests"):
    response = JsonResponse({
        "error": "rate_limit_exceeded",
        "message": f"You have exceeded the limit of {limit} {context} per {window_seconds//60} minute(s). "
                   f"Please wait {window_seconds} seconds before retrying.",
        "retry_after_seconds": window_seconds
    }, status=429)
    response["Retry-After"] = window_seconds
    return response