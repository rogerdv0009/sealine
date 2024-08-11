from django import forms
from .models import Tour
class TourForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.visible_fields():
            f.field.widget.attrs['class'] = 'form-control'
            f.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Tour
        fields = ("title","price","description","image")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Título del Tour"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Descripción del Tour",
                    "rows": 3,
                    "cols": 3
                }
            ),
        }
