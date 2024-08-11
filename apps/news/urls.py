from django.urls import path
from .views import (
    NewCreateView, NewDeleteView, NewDetailView, NewListView, NewUpdateView,
    CommentAdminCreateView, CommentCreateView, CommentDeleteView, CommentListView, CommentUpdateView, checkComments
                    )
urlpatterns = [
    path('listado/', NewListView.as_view(), name="News_List"),
    path('crear/', NewCreateView.as_view(), name="News_Create"),
    path('editar/<int:pk>/', NewUpdateView.as_view(), name="News_Update"),
    path('eliminar/<int:pk>/', NewDeleteView.as_view(), name="News_Delete"),
    path('detalle/<int:pk>/', NewDetailView.as_view(), name="News_Detail"),
    #Urls para los comentarios
    path('comentarios/aprobar/<int:id_objeto>/', checkComments, name="Comments_Check"),
    path('comentarios/listado/', CommentListView.as_view(), name="Comments_List"),
    path('comentarios/crear/', CommentAdminCreateView.as_view(), name="Comments_Create"),
    path('comentarios_crear_user/<int:pk>/', CommentCreateView.as_view(), name="Comments_User_Create"),
    path('comentarios/editar/<int:pk>/', CommentUpdateView.as_view(), name="Comments_Update"),
    path('comentarios/eliminar/<int:pk>/', CommentDeleteView.as_view(), name="Comments_Delete"),
]