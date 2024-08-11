from django.urls import path
from .views import TourCreateView, TourListView, TourDetailView, TourDeleteView, TourUpdateView
urlpatterns = [
    path('listado/', TourListView.as_view(), name="Tours_List"),
    path('crear/', TourCreateView.as_view(), name="Tours_Create"),
    path('editar/<int:pk>/', TourUpdateView.as_view(), name="Tours_Update"),
    path('eliminar/<int:pk>/', TourDeleteView.as_view(), name="Tours_Delete"),
    path('detalle/<int:pk>/', TourDetailView.as_view(), name="Tours_Detail"),
]