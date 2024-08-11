from django.urls import path
from .views import TeamCreateView, TeamDeleteView, TeamListView, TeamUpdateView
urlpatterns = [
    path('listado/', TeamListView.as_view(), name="Teams_List"),
    path('crear/', TeamCreateView.as_view(), name="Teams_Create"),
    path('editar/<int:pk>/', TeamUpdateView.as_view(), name="Teams_Update"),
    path('eliminar/<int:pk>/', TeamDeleteView.as_view(), name="Teams_Delete"),
]