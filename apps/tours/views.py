from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from apps.users.mixins import LoginAndSuperUser
from .models import Tour
from .forms import TourForm
# Create your views here.

class TourListView(ListView):
    model = Tour
    template_name = "tours/listado.html"

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

class TourCreateView(LoginAndSuperUser, CreateView):
    model = Tour
    template_name = "tours/crear.html"
    form_class = TourForm
    success_url = reverse_lazy("Tours_List")

    def form_valid(self, form):
        messages.success(self.request, "¡La creación se realizó correctamente!")
        return super().form_valid(form)


class TourUpdateView(LoginAndSuperUser, UpdateView):
    model = Tour
    template_name = "tours/editar.html"
    form_class = TourForm
    success_url = reverse_lazy("Tours_List")

    def form_valid(self, form):
        messages.success(self.request, "¡La edición se realizó correctamente!")
        return super().form_valid(form)

class TourDeleteView(LoginAndSuperUser, DeleteView):
    model = Tour
    template_name = "tours/eliminar.html"

    def post(self, request, pk, *args, **kwargs):
        object = Tour.objects.get(id = pk)
        object.state = False
        object.save()
        messages.success(self.request, "¡La eliminación se realizó correctamente!")
        return redirect('Tours_List')

class TourDetailView(DetailView):
    model = Tour
    template_name = "tours/detalle.html"
