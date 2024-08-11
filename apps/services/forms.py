from django import forms
from .models import Service
class ServiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.visible_fields():
            f.field.widget.attrs['class'] = 'form-control'
            f.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Service
        fields = ("title","icon","description")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Título del Servicio"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Descripción del Servicio",
                    "rows": 3,
                    "cols": 3
                }
            ),
        }