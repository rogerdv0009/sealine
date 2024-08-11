from django.urls import path
from .views import UserPCreateView, UserPListView, UserPDeleteView, UserPUpdateView, LoginFormView, CloseSesion, RegisterView
urlpatterns = [
    path("login/", LoginFormView.as_view(), name="Login"),
    path("registrar/", RegisterView.as_view(), name="Register"),
    path("logout/", CloseSesion.as_view(), name="Logout"),
    path('listado/', UserPListView.as_view(), name="Users_List"),
    path('crear/', UserPCreateView.as_view(), name="Users_Create"),
    path('editar/<int:pk>/', UserPUpdateView.as_view(), name="Users_Update"),
    path('eliminar/<int:pk>/', UserPDeleteView.as_view(), name="Users_Delete"),
]