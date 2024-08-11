from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from apps.users.mixins import LoginAndSuperUser
from .models import New, Comment
from .forms import NewForm, CommentForm, CommentAdminForm
# Create your views here.

class NewListView(ListView):
    model = New
    template_name = "news/listado.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(state=True)
        search = self.request.GET.get("buscar_input")
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(description__icontains=search),
                state = True
            ).distinct()
        return queryset

class NewCreateView(LoginAndSuperUser, CreateView):
    model = New
    template_name = "news/crear.html"
    form_class = NewForm
    success_url = reverse_lazy("News_List")

    def form_valid(self, form):
        messages.success(self.request, "¡La creación se realizó correctamente!")
        return super().form_valid(form)


class NewUpdateView(LoginAndSuperUser, UpdateView):
    model = New
    template_name = "news/editar.html"
    form_class = NewForm
    success_url = reverse_lazy("News_List")

    def form_valid(self, form):
        messages.success(self.request, "¡La edición se realizó correctamente!")
        return super().form_valid(form)

class NewDeleteView(LoginAndSuperUser, DeleteView):
    model = New
    template_name = "news/eliminar.html"

    def post(self, request, pk, *args, **kwargs):
        object = New.objects.get(id = pk)
        object.state = False
        object.save()
        messages.success(self.request, "¡La eliminación se realizó correctamente!")
        return redirect('News_List')

class NewDetailView(DetailView):
    model = New
    template_name = "news/detalle.html"

    def commentsList(self):
        new = self.model.objects.get(id = self.kwargs["pk"])
        comments = Comment.objects.filter(new = new, state = True, check_comment = True)
        return comments

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.commentsList()
        return context



#Vistas para los comentarios
class CommentCreateView(CreateView):
    model = Comment
    template_name = "comments/crear.html"
    form_class = CommentForm
    success_url = reverse_lazy("News_List")

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            description = form.cleaned_data['description']
            new_id = request.POST['new_id']
            new = New.objects.filter(id = new_id).first()
            comment = Comment(
                email = email,
                description = description,
                new = new,
                check_comment = False
                )
            comment.save()
            messages.success(self.request, "¡El comentario se creó correctamente, se mostrará en la noticia luego de ser aprobado!")
            return redirect(self.success_url)
        else:
            messages.error(request, "¡El formulario no es válido!")
            return redirect(self.success_url)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new"] = self.model.objects.get(id = self.kwargs["pk"])
        return context



# Crear Comentarios Admin
class CommentListView(LoginAndSuperUser, ListView):
    model = Comment
    template_name = "comments/listado.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(state=True)
        filtrado = self.request.GET.get("select_filtrado")
        if filtrado:
            if filtrado == "General":
                queryset = queryset.filter(state=True)
            else:
                queryset = queryset.filter(check_comment = filtrado, state = True)
        return queryset

class CommentAdminCreateView(LoginAndSuperUser, CreateView):
    model = Comment
    template_name = "comments/crear_admin.html"
    form_class = CommentAdminForm
    success_url = reverse_lazy("Comments_List")

    def form_valid(self, form):
        messages.success(self.request, "¡El comentario se creó correctamente!")
        return super().form_valid(form)

class CommentUpdateView(LoginAndSuperUser, UpdateView):
    model = Comment
    template_name = "comments/editar.html"
    form_class = CommentAdminForm
    success_url = reverse_lazy("Comments_List")

    def form_valid(self, form):
        messages.success(self.request, "¡La edición se realizó correctamente!")
        return super().form_valid(form)

class CommentDeleteView(LoginAndSuperUser, DeleteView):
    model = Comment
    template_name = "comments/eliminar.html"

    def post(self, request, pk, *args, **kwargs):
        object = Comment.objects.get(id = pk)
        object.state = False
        object.save()
        messages.success(self.request, "¡La eliminación se realizó correctamente!")
        return redirect('Comments_List')

#Metodo para aprobar los comentarios
def checkComments(request, id_objeto):
    if request.user.is_superuser:
        comment = Comment.objects.get(id = id_objeto)
        comment.check_comment = True
        comment.save()
        messages.success(request, "¡Se aprobó el comentario con éxito!")
        return redirect('Comments_List')
    else:
        messages.error(request, "Usted no tiene permisos para acceder a esta ruta")
        return redirect("Main")