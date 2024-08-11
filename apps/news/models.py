from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from apps.main.models import BaseModel
# Create your models here.

def validateImageSize(value):
    filesize = value.size
    if filesize > 1 * 1024 * 1024:  # 1MB
        raise ValidationError("El tamaño máximo permitido es 1MB")

class New(BaseModel):

    title = models.CharField(_("Título"), max_length=100, null=False, blank=False)
    category = models.CharField(_("Categoría"), max_length=100, null=False, blank=False)
    description = models.TextField(_("Descripción"), null=False, blank=False)
    date = models.DateField(_("Fecha"), auto_now=False, auto_now_add=False, null=False, blank=False)
    image = models.ImageField(_("Imagen"), upload_to="news/",null=True, blank=True, height_field=None, width_field=None, max_length=None, validators=[FileExtensionValidator(['jpg','jpeg','png','gif','webp']),validateImageSize])
    autor = models.CharField(_("Autor"), max_length=100, default=_("Anónimo"))

    class Meta:
        verbose_name = _("New")
        verbose_name_plural = _("News")
        ordering = ['-id']

    def __str__(self):
        return self.title


class Comment(BaseModel):

    email = models.EmailField(_("Correo"), max_length=254, null=False, blank=False)
    description = models.TextField(_("Descripcion"))
    new = models.ForeignKey(New, verbose_name=_("Noticia"), on_delete=models.CASCADE)
    check_comment = models.BooleanField(_("Aprobada"), default=False)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ['-id']

    def __str__(self):
        return f"Comentario realizado por: {self.email}"

