from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.db import models

def validateImageSize(value):
    filesize = value.size
    if filesize > 1 * 1024 * 1024:  # 1MB
        raise ValidationError("El tamaño máximo permitido es 1MB")

class UserPManager(BaseUserManager):
    def _create_user(self, username, email, name, lastname, password, is_staff, is_superuser):
        user = self.model(
            username = username,
            email = email,
            name = name,
            lastname = lastname,
            is_staff = is_staff,
            is_superuser = is_superuser
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name, lastname, password = None):
        return self._create_user(username, email, name, lastname, password, False, False)

    def create_superuser(self, username, email, name, lastname, password = None):
        return self._create_user(username, email, name, lastname, password, True, True)

class UserP(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("Nombre de Usuario"), unique=True, max_length=100)
    email = models.EmailField(_("Correo Electrónico"), unique=True, max_length=254)
    name = models.CharField(_("Nombre"), blank=True, max_length=150, null=True)
    lastname = models.CharField(_("Apellidos"), max_length=200, blank=True, null=True)
    avatar = models.ImageField(_("Imagen de Perfil"), upload_to="avatar/", blank=True, null=True, max_length=None, validators=[FileExtensionValidator(['jpg','jpeg','png','gif','webp']),validateImageSize])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserPManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email","name","lastname"]

    def __str__(self):
        return f"Usuario {self.username}"
