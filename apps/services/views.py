from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from apps.users.mixins import LoginAndSuperUser
from .models import Service
from .forms import ServiceForm
# Create your views here.

class ServiceListView(ListView):
    model = Service
    template_name = "services/listado.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(state=True)
        search = self.request.GET.get("buscar_input")
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(description__icontains=search),
                state = True
            ).distinct()
        return queryset

class ServiceCreateView(LoginAndSuperUser, CreateView):
    model = Service
    template_name = "services/crear.html"
    form_class = ServiceForm
    success_url = reverse_lazy("Services_List")

    def form_valid(self, form):
        messages.success(self.request, "¡La creación se realizó correctamente!")
        return super().form_valid(form)


class ServiceUpdateView(LoginAndSuperUser, UpdateView):
    model = Service
    template_name = "services/editar.html"
    form_class = ServiceForm
    success_url = reverse_lazy("Services_List")

    def form_valid(self, form):
        messages.success(self.request, "¡La edición se realizó correctamente!")
        return super().form_valid(form)

class ServiceDeleteView(LoginAndSuperUser, DeleteView):
    model = Service
    template_name = "services/eliminar.html"

    def post(self, request, pk, *args, **kwargs):
        object = Service.objects.get(id = pk)
        object.state = False
        object.save()
        messages.success(self.request, "¡La eliminación se realizó correctamente!")
        return redirect('Services_List')

