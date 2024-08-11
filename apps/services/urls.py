from django.urls import path
from .views import ServiceCreateView, ServiceListView, ServiceDeleteView, ServiceUpdateView
urlpatterns = [
    path('listado/', ServiceListView.as_view(), name="Services_List"),
    path('crear/', ServiceCreateView.as_view(), name="Services_Create"),
    path('editar/<int:pk>/', ServiceUpdateView.as_view(), name="Services_Update"),
    path('eliminar/<int:pk>/', ServiceDeleteView.as_view(), name="Services_Delete"),
]