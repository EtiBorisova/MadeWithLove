from django.contrib.auth.models import UserManager, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.utils import timezone

from django.db import models
from django.contrib.auth import models as auth_models, get_user_model
from django.utils.translation import gettext_lazy as _


class MadeWithLoveUser(auth_models.AbstractBaseUser,PermissionsMixin):
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,

    )
    email = models.EmailField(
        null=False,
        blank=True,
        unique=True
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    objects = UserManager()


UserModel = get_user_model()


class ProfileModel(models.Model):

    CHOISES = (
        ("Male",'Male' ),
        ('Female', 'Female'),
        ('Do not show', 'Do not show')
    )
    email = models.EmailField(
        null=True,
        blank=True
    )
    first_name = models.CharField(
        max_length=30,
        validators=(MinLengthValidator(2),),
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=30,
        validators=(MinLengthValidator(2),),
        null=True,
        blank=True
    )
    gender = models.CharField(
        max_length=30,
        choices=CHOISES,
        null=True,
        blank=True
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True
    )
    profile_image = models.ImageField(
        null=True,
        blank=True
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return self.first_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
