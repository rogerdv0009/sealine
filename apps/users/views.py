from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, RedirectView
from django.contrib.auth.views import LoginView

from .mixins import LoginAndSuperUser
from .models import UserP
from .forms import UserPForm
# Create your views here.

#Autenticar
class LoginFormView(LoginView):
    template_name = 'login/login.html'
    success_url = reverse_lazy('Main')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, "Usted ya se encuentra autenticado!")
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

#Registrar
class RegisterView(CreateView):
    model = UserP
    template_name = "login/registrar.html"
    form_class = UserPForm
    success_url = reverse_lazy("Login")

    def form_valid(self, form):
        messages.success(self.request, "¡El registro se realizó correctamente!")
        return super().form_valid(form)

#Cerrar Sesion
class CloseSesion(RedirectView):
    pattern_name = 'Main'
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)

class UserPListView(LoginAndSuperUser,ListView):
    model = UserP
    template_name = "users/listado.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset

class UserPCreateView(LoginAndSuperUser,CreateView):
    model = UserP
    template_name = "users/crear.html"
    form_class = UserPForm
    success_url = reverse_lazy("Users_List")

    def form_valid(self, form):
        messages.success(self.request, "¡La creación se realizó correctamente!")
        return super().form_valid(form)

class UserPUpdateView(LoginAndSuperUser,UpdateView):
    model = UserP
    template_name = "users/editar.html"
    form_class = UserPForm
    success_url = reverse_lazy("Users_List")

    def form_valid(self, form):
        messages.success(self.request, "¡La edición se realizó correctamente!")
        return super().form_valid(form)

class UserPDeleteView(LoginAndSuperUser,DeleteView):
    model = UserP
    template_name = "users/eliminar.html"

    def post(self, request, pk, *args, **kwargs):
        object = UserP.objects.get(id = pk)
        object.is_active = False
        object.save()
        messages.success(self.request, "¡La eliminación se realizó correctamente!")
        return redirect('News_List')