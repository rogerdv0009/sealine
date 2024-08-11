from django import forms
from .models import Testimonial
class TestimonialForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.visible_fields():
            f.field.widget.attrs['class'] = 'form-control'
            f.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Testimonial
        fields = ("name","job","description","image")
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Nombre de la Persona"
                }
            ),
            "job": forms.TextInput(
                attrs={
                    "placeholder": "Rol actual de esa Persona"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Descripción del Testimonio",
                    "rows": 3,
                    "cols": 3
                }
            ),
        }