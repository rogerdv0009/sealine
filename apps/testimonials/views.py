from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from apps.users.mixins import LoginAndSuperUser
from .models import Testimonial
from .forms import TestimonialForm
# Create your views here.

class TestimonialCreateView(LoginAndSuperUser, CreateView):
    model = Testimonial
    template_name = "testimonials/crear.html"
    form_class = TestimonialForm
    success_url = reverse_lazy("Teams_List")

    def form_valid(self, form):
        messages.success(self.request, "¡La creación se realizó correctamente!")
        return super().form_valid(form)


class TestimonialUpdateView(LoginAndSuperUser, UpdateView):
    model = Testimonial
    template_name = "testimonials/editar.html"
    form_class = TestimonialForm
    success_url = reverse_lazy("Teams_List")

    def form_valid(self, form):
        messages.success(self.request, "¡La edición se realizó correctamente!")
        return super().form_valid(form)

class TestimonialDeleteView(LoginAndSuperUser, DeleteView):
    model = Testimonial
    template_name = "testimonials/eliminar.html"

    def post(self, request, pk, *args, **kwargs):
        object = Testimonial.objects.get(id = pk)
        object.state = False
        object.save()
        messages.success(self.request, "¡La eliminación se realizó correctamente!")
        return redirect('Teams_List')

