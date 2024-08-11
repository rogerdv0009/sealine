from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.users.mixins import LoginAndSuperUser
from .models import Team
from .forms import TeamForm
from apps.testimonials.models import Testimonial
# Create your views here.

class TeamListView(ListView):
    model = Team
    template_name = "teams/listado.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(state=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["testimonios"] = Testimonial.objects.filter(state = True)
        return context


class TeamCreateView(LoginAndSuperUser, CreateView):
    model = Team
    template_name = "teams/crear.html"
    form_class = TeamForm
    success_url = reverse_lazy("Teams_List")

    def form_valid(self, form):
        messages.success(self.request, "¡La creación se realizó correctamente!")
        return super().form_valid(form)


class TeamUpdateView(LoginAndSuperUser, UpdateView):
    model = Team
    template_name = "teams/editar.html"
    form_class = TeamForm
    success_url = reverse_lazy("Teams_List")

    def form_valid(self, form):
        messages.success(self.request, "¡La edición se realizó correctamente!")
        return super().form_valid(form)

class TeamDeleteView(LoginAndSuperUser, DeleteView):
    model = Team
    template_name = "teams/eliminar.html"

    def post(self, request, pk, *args, **kwargs):
        object = Team.objects.get(id = pk)
        object.state = False
        object.save()
        messages.success(self.request, "¡La eliminación se realizó correctamente!")
        return redirect('Teams_List')


