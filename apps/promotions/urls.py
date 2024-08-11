from django.urls import path
from .views import PromotionCreateView, PromotionListView, PromotionDetailView, PromotionDeleteView, PromotionUpdateView
urlpatterns = [
    path('listado/', PromotionListView.as_view(), name="Promotions_List"),
    path('crear/', PromotionCreateView.as_view(), name="Promotions_Create"),
    path('editar/<int:pk>/', PromotionUpdateView.as_view(), name="Promotions_Update"),
    path('eliminar/<int:pk>/', PromotionDeleteView.as_view(), name="Promotions_Delete"),
    path('detalle/<int:pk>/', PromotionDetailView.as_view(), name="Promotions_Detail"),
]