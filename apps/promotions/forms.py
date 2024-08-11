from django import forms
from .models import Promotion
class PromotionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.visible_fields():
            f.field.widget.attrs['class'] = 'form-control'
            f.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Promotion
        fields = ("title","description","image")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Título de la Promoción"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Descripción de la Promoción",
                    "rows": 3,
                    "cols": 3
                }
            ),
        }