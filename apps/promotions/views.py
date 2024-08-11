from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from apps.users.mixins import LoginAndSuperUser
from .models import Promotion
from .forms import PromotionForm
# Create your views here.

class PromotionListView(ListView):
    model = Promotion
    template_name = "promotions/listado.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(state=True)
        return queryset

class PromotionCreateView(LoginAndSuperUser, CreateView):
    model = Promotion
    template_name = "promotions/crear.html"
    form_class = PromotionForm
    success_url = reverse_lazy("Promotions_List")

    def form_valid(self, form):
        messages.success(self.request, "¡La creación se realizó correctamente!")
        return super().form_valid(form)


class PromotionUpdateView(LoginAndSuperUser, UpdateView):
    model = Promotion
    template_name = "promotions/editar.html"
    form_class = PromotionForm
    success_url = reverse_lazy("Promotions_List")

    def form_valid(self, form):
        messages.success(self.request, "¡La edición se realizó correctamente!")
        return super().form_valid(form)

class PromotionDeleteView(LoginAndSuperUser, DeleteView):
    model = Promotion
    template_name = "promotions/eliminar.html"

    def post(self, request, pk, *args, **kwargs):
        object = Promotion.objects.get(id = pk)
        object.state = False
        object.save()
        messages.success(self.request, "¡La eliminación se realizó correctamente!")
        return redirect('Promotions_List')

class PromotionDetailView(DetailView):
    model = Promotion
    template_name = "promotions/detalle.html"

