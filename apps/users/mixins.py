from django.shortcuts import redirect
from django.contrib import messages

class LoginAndSuperUser(object):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return super().dispatch(request, *args, **kwargs)
        messages.error(request, "No esta autorizado para acceder a esta ruta")
        return redirect("Main")