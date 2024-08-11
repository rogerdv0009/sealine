from django import forms
from .models import New, Comment
class NewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.visible_fields():
            f.field.widget.attrs['class'] = 'form-control'
            f.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = New
        fields = ("title","category","description","date","image","autor")
        widgets = {
            "date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Título de la noticia"
                }
            ),
            "category": forms.TextInput(
                attrs={
                    "placeholder": "Categoría de la noticia"
                }
            ),
            "autor": forms.TextInput(
                attrs={
                    "placeholder": "Autor de la noticia"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Descripción de la noticia",
                    "rows": 3,
                    "cols": 3
                }
            ),
        }


#Formulario de Comentario
class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.visible_fields():
            f.field.widget.attrs['class'] = 'form-control'
            f.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Comment
        fields = ("email","description")
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Correo electrónico"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Descripción del Comentario",
                    "rows": 3,
                    "cols": 3
                }
            ),
        }

#Formulario de Comentario para admin
class CommentAdminForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("email","description","new","check_comment")
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Correo electrónico",
                    "class": "form-control",
                    "autocomplete": "off"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Descripción del Comentario",
                    "rows": 3,
                    "cols": 3,
                    "class": "form-control",
                    "autocomplete": "off"
                }
            ),
            "new": forms.Select(
                attrs={
                    "class": "form-control",
                    "autocomplete": "off"
                }
            ),
            "check_comment": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                    "autocomplete": "off"
                }
            ),
        }
