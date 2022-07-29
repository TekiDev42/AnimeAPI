from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email_validator = EmailValidator()
    email = models.EmailField(
                    _("email address"),
                    unique=True,
                    validators=[email_validator])
