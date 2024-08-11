from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from apps.users.models import UserP

from apps.users.mixins import LoginAndSuperUser
from .models import Ticket
from .forms import Ticket_IndexForm, TicketForm
# Create your views here.

#Metodo para crear un ticket desde el index
def createTicketIndex(request):
    if request.method == 'POST':
        form = Ticket_IndexForm(request.POST)
        if form.is_valid():
            ft_from = form.cleaned_data['ft_from']
            ft_to = form.cleaned_data['ft_to']
            ft_date = form.cleaned_data['ft_date']
            ft_duration = form.cleaned_data['ft_duration']
            ft_adults = form.cleaned_data['ft_adults']
            ft_children = form.cleaned_data['ft_children']
            ft_user_id = request.POST['ft_user']
            ft_user = UserP.objects.filter(pk = ft_user_id).first()
            tickets_usuario = Ticket.objects.filter(ft_user = ft_user, ft_check = False).count()
            if tickets_usuario < 5:
                ticket = Ticket(
                    ft_from = ft_from,
                    ft_to = ft_to,
                    ft_date = ft_date,
                    ft_duration = ft_duration,
                    ft_adults = ft_adults,
                    ft_children = ft_children,
                    ft_user = ft_user,
                    ft_check = False
                    )
                ticket.save()
                messages.success(request, "¡Ticket solicitado con éxito, espere a que nuestro equipo lo apruebe!")
                return redirect("Tickets_User_List")
            else:
                messages.error(request, "¡Usted ha solicitado más de 4 ticket que aun no se han aprobado, por el momento debe esperar a que nuestro equipo apruebe al menos uno para poder solicitar otro!")
                return redirect("Main")
        else:
            messages.error(request, "¡El formulario no es válido!")
            return redirect("Main")
    else:
        messages.error(request, "¡El formulario se está enviando por el método incorrecto!")
        return redirect("Main")

#Metodo para aprobar los tickets
def checkTicket(request, id_objeto):
    if request.user.is_superuser:
        ticket = Ticket.objects.get(id = id_objeto)
        ticket.ft_check = True
        ticket.save()
        messages.success(request, "¡Se aprobó el ticket con éxito!")
        return redirect('Tickets_List')
    else:
        messages.error(request, "Usted no tiene permisos para acceder a esta ruta")
        return redirect("Main")


class TicketUserListView(ListView):
    model = Ticket
    template_name = "tickets/listado_user.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(state=True)
        user = self.request.user
        if user:
            queryset = queryset.filter(ft_user = user, state = True)
        return queryset

class TicketListView(LoginAndSuperUser,ListView):
    model = Ticket
    template_name = "tickets/listado.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(state=True)
        filtrado = self.request.GET.get("select_filtrado")
        if filtrado:
            if filtrado == "General":
                queryset = queryset.filter(state=True)
            else:
                queryset = queryset.filter(ft_check = filtrado, state = True)
        return queryset

class TicketCreateView(LoginAndSuperUser, CreateView):
    model = Ticket
    template_name = "tickets/crear.html"
    form_class = TicketForm
    success_url = reverse_lazy("Tickets_List")

    def form_valid(self, form):
        messages.success(self.request, "¡La creación se realizó correctamente!")
        return super().form_valid(form)


class TicketUpdateView(LoginAndSuperUser, UpdateView):
    model = Ticket
    template_name = "tickets/editar.html"
    form_class = TicketForm
    success_url = reverse_lazy("Tickets_List")

    def form_valid(self, form):
        messages.success(self.request, "¡La edición se realizó correctamente!")
        return super().form_valid(form)

class TicketDeleteView(LoginAndSuperUser, DeleteView):
    model = Ticket
    template_name = "tickets/eliminar.html"

    def post(self, request, pk, *args, **kwargs):
        object = Ticket.objects.get(id = pk)
        object.state = False
        object.save()
        messages.success(self.request, "¡La eliminación se realizó correctamente!")
        return redirect('Tickets_List')


