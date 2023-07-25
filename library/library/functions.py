from django.http import HttpResponseForbidden
from django.shortcuts import redirect


def deny_non_librarian(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('authentication:login')
        elif request.user.role == 1:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("403 Forbidden")
    return wrapper
