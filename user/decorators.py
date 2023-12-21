from django.http import HttpResponseRedirect
from django.urls import reverse
def Authenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        return view_func(request, *args, **kwargs)
    return wrapper_func


def Role(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return HttpResponseRedirect(reverse('flight'))
        return view_func(request, *args, **kwargs)
    return wrapper_func