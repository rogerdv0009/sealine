from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class BaseModel(models.Model):

    id = models.AutoField(primary_key=True)
    state = models.BooleanField(_('Estado'), default=True)
    created_date = models.DateField(_('Fecha de Creación'), auto_now=False, auto_now_add=True)
    updated_date = models.DateField(_('Fecha de Modificación'), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("ModelBase")
        verbose_name_plural = _("ModelBases")
        abstract = True


