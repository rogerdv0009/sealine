from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

from apps.main.models import BaseModel
# Create your models here.

def validateImageSize(value):
    filesize = value.size
    if filesize > 1 * 1024 * 1024:  # 1MB
        raise ValidationError("El tamaño máximo permitido es 1MB")

class Tour(BaseModel):

    title = models.CharField(_("Título"), max_length=100, null=False, blank=False)
    description = models.TextField(_("Descripción"), null=False, blank=False)
    price = models.DecimalField(_("Precio"), max_digits=10, decimal_places=2)
    image = models.ImageField(_("Imagen"), upload_to="tours/", null=True, blank=True, max_length=None, validators=[FileExtensionValidator(['jpg','jpeg','png','gif','webp']),validateImageSize])

    class Meta:
        verbose_name = _("Tour")
        verbose_name_plural = _("Tours")
        ordering = ['-id']

    def __str__(self):
        return self.title

