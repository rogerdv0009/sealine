from typing import Any
from django import forms
from django.utils.translation import gettext as _
from .models import UserP

class UserPForm(forms.ModelForm):
    password1 = forms.CharField(label=_("Contraseña"), widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': _('Ingrese su contraseña'),
            'id': 'password1',
            'required': 'required'
        }
    ))

    password2 = forms.CharField(label=_("Verificar Contraseña"), widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': _('Verifique su contraseña'),
            'id': 'password2',
            'required': 'required'
        }
    ))

    class Meta:
        model = UserP
        fields = ('username','name','lastname','email','avatar')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    "placeholder": _("Ingrese el nombre de usuario"),
                    "class": "form-control"
                }
            ),
            'name': forms.TextInput(
                attrs={
                    "placeholder": _("Ingrese el nombre"),
                    "class": "form-control"
                }
            ),
            'lastname': forms.TextInput(
                attrs={
                    "placeholder": _("Ingrese los apellidos"),
                    "class": "form-control"
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    "placeholder": _("Ingrese el correo electrónico"),
                    "class": "form-control"
                }
            ),
            'avatar': forms.FileInput(
                attrs={
                    "class": "form-control"
                }
            ),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Contraseñas no coinciden!")
        return password2

    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user