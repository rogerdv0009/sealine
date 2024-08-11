from django import forms
from .models import Team
class TeamForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.visible_fields():
            f.field.widget.attrs['class'] = 'form-control'
            f.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Team
        fields = ("name","job","image","facebook","twitter","instagram","google","linkedin",)
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Nombre del miembro"
                }
            ),
            "job": forms.TextInput(
                attrs={
                    "placeholder": "Cargo del Miembro"
                }
            ),
            "facebook": forms.URLInput(
                attrs={
                    "placeholder": "https://example.com"
                }
            ),
            "twitter": forms.URLInput(
                attrs={
                    "placeholder": "https://example.com"
                }
            ),
            "instagram": forms.URLInput(
                attrs={
                    "placeholder": "https://example.com"
                }
            ),
            "google": forms.URLInput(
                attrs={
                    "placeholder": "https://example.com"
                }
            ),
            "linkedin": forms.URLInput(
                attrs={
                    "placeholder": "https://example.com"
                }
            ),
        }
