from django.urls import path
from .views import TestimonialCreateView, TestimonialDeleteView, TestimonialUpdateView
urlpatterns = [
    path('crear/', TestimonialCreateView.as_view(), name="Testimonials_Create"),
    path('editar/<int:pk>/', TestimonialUpdateView.as_view(), name="Testimonials_Update"),
    path('eliminar/<int:pk>/', TestimonialDeleteView.as_view(), name="Testimonials_Delete"),
]