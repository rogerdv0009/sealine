from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from apps.main.models import BaseModel

def validateImageSize(value):
    filesize = value.size
    if filesize > 1 * 1024 * 1024:  # 1MB
        raise ValidationError("El tamaño máximo permitido es 1MB")

class Team(BaseModel):

    name = models.CharField(_("Nombre"), max_length=100)
    job = models.CharField(_("Cargo"), max_length=100)
    image = models.ImageField(_("Imagen"), upload_to="team/",null=True, blank=True, max_length=None, validators=[FileExtensionValidator(['jpg','jpeg','png','gif','webp']),validateImageSize])
    facebook = models.URLField(_("Facebook"), max_length=200)
    twitter = models.URLField(_("Twitter"), max_length=200)
    instagram = models.URLField(_("Instagram"), max_length=200)
    google = models.URLField(_("Google+"), max_length=200)
    linkedin = models.URLField(_("Linked In"), max_length=200)

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")
        ordering = ['-id']

    def __str__(self):
        return self.name


