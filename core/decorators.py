from django.shortcuts import redirect
from functools import wraps

def role_required(required_role):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect("login")

            profile = getattr(request.user, "profile", None)
            user_role = getattr(profile, "role", None)
            print(user_role, required_role)
            if user_role != required_role:
                return redirect("login")    

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
