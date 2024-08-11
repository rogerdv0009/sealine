from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ("ft_from","ft_to","ft_date","ft_duration","ft_adults","ft_children","ft_user","ft_check")
        widgets = {
            "ft_from": forms.Select(
                attrs={
                    "class": "form-control",
                    "autocomplete": "off"
                }
            ),
            "ft_to": forms.Select(
                attrs={
                    "class": "form-control",
                    "autocomplete": "off"
                }
            ),
            "ft_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                    "autocomplete": "off"
                }
            ),
            "ft_duration": forms.Select(
                attrs={
                    "class": "form-control",
                    "autocomplete": "off"
                }
            ),
            "ft_adults": forms.NumberInput(
                attrs={
                    "min": 0,
                    "class": "form-control",
                    "autocomplete": "off"
                }
            ),
            "ft_children": forms.NumberInput(
                attrs={
                    "min": 0,
                    "class": "form-control",
                    "autocomplete": "off"
                }
            ),
            "ft_user": forms.Select(
                attrs={
                    "class": "form-control",
                    "autocomplete": "off"
                }
            ),
            "ft_check": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                    "autocomplete": "off"
                }
            ),
        }

class Ticket_IndexForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ("ft_from","ft_to","ft_date","ft_duration","ft_adults","ft_children")
        widgets = {
            "ft_from": forms.Select(
                attrs={
                    "class": "form-control",
                    "autocomplete": "off"
                }
            ),
            "ft_to": forms.Select(
                attrs={
                    "class": "form-control",
                    "autocomplete": "off"
                }
            ),
            "ft_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                    "autocomplete": "off"
                }
            ),
            "ft_duration": forms.Select(
                attrs={
                    "class": "form-control",
                    "autocomplete": "off"
                }
            ),
            "ft_adults": forms.NumberInput(
                attrs={
                    "min": 0,
                    "class": "form-control",
                    "autocomplete": "off"
                }
            ),
            "ft_children": forms.NumberInput(
                attrs={
                    "min": 0,
                    "class": "form-control",
                    "autocomplete": "off"
                }
            ),
        }
