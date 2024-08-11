from django.db import models
from django.utils.translation import gettext as _

from apps.main.models import BaseModel
from apps.users.models import UserP
# Create your models here.

select_ft_from = {
    ("New York","New York"),
    ("Lisbon","Lisbon"),
    ("Cuba","Cuba"),
}

select_ft_to = {
    ("Chicago","Chicago"),
    ("Madrid","Madrid"),
    ("Paris","París"),
}

select_ft_duration = {
    (1,"1 Día"),
    (2,"2 Días"),
    (3,"3 Días"),
}

class Ticket(BaseModel):

    ft_from = models.CharField(_("De"), max_length=150, null=False, blank=False, choices=select_ft_from)
    ft_to = models.CharField(_("Para"), max_length=150, null=False, blank=False, choices=select_ft_to)
    ft_date = models.DateField(_("Fecha"), auto_now=False, auto_now_add=False, null=False, blank=False)
    ft_duration = models.IntegerField(_("Duración"), null=False, blank=False, choices=select_ft_duration)
    ft_adults = models.IntegerField(_("Adultos"), null=False, blank=False, default=2)
    ft_children = models.IntegerField(_("Niños"), null=False, blank=False, default=0)
    ft_check = models.BooleanField(_("Aprobada"), default=False)
    ft_user = models.ForeignKey(UserP, verbose_name=_("Usuario"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Ticket")
        verbose_name_plural = _("Tickets")
        ordering = ['-id']

    def __str__(self):
        return f'Ticket de {self.ft_from} para {self.ft_to}, fecha de salida {self.ft_date}'

