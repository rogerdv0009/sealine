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

class Testimonial(BaseModel):

    name = models.CharField(_("Nombre"), max_length=100, null=False, blank=False)
    description = models.TextField(_("Descripción"), null=False, blank=False)
    job = models.CharField(_("Cargo"), max_length=100, null=False, blank=False)
    image = models.ImageField(_("Imagen"), upload_to="testimonials/", height_field=None, width_field=None, max_length=None, validators=[FileExtensionValidator(['jpg','jpeg','png','gif','webp']),validateImageSize])

    class Meta:
        verbose_name = _("Testimonial")
        verbose_name_plural = _("Testimonials")
        ordering = ['-id']

    def __str__(self):
        return self.name

