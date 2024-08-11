from django.db import models
from django.utils.translation import gettext as _

from apps.main.models import BaseModel
# Create your models here.

class Service(BaseModel):

    title = models.CharField(_("Título"), max_length=100, null=False, blank=False)
    description = models.TextField(_("Descripción"), null=False, blank=False)
    icon = models.CharField(_("Icono"), max_length=100, default="fas fa-photo-video")

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")
        ordering = ['-id']

    def __str__(self):
        return self.title

