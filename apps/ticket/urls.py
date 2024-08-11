from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import createTicketIndex,checkTicket, TicketCreateView, TicketListView, TicketDeleteView, TicketUpdateView, TicketUserListView
urlpatterns = [
    path('crear_ticket/', login_required(createTicketIndex, login_url="/users/login"), name="Tickets_Create_Index"),
    path('checkeado/<int:id_objeto>/', login_required(checkTicket, login_url="/users/login"), name="Tickets_Check"),
    path('listado/', TicketListView.as_view(), name="Tickets_List"),
    path('listado_user/', TicketUserListView.as_view(), name="Tickets_User_List"),
    path('crear/', TicketCreateView.as_view(), name="Tickets_Create"),
    path('editar/<int:pk>/', TicketUpdateView.as_view(), name="Tickets_Update"),
    path('eliminar/<int:pk>/', TicketDeleteView.as_view(), name="Tickets_Delete"),
]