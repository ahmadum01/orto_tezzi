from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import UserManager as CoreUserManager
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from carts.services import CartCreator


class UserQuerySet(models.QuerySet):
    pass


class UserManagerQuery(CoreUserManager.from_queryset(UserQuerySet)):
    pass


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_field):
        if not username:
            raise ValueError("User must have an username.")
        user = self.model(username=username, **extra_field)
        user.set_password(password)
        user.save(using=self._db)
        CartCreator(user).execute()
        return user

    def create_superuser(self, username, password, **extra_field):
        user = self.create_user(username, password, **extra_field)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractUser):
    username_validators = [
        AbstractUser.username_validator,
        MinLengthValidator(4),
        MaxLengthValidator(30),
    ]
    username = models.CharField(
        _("username"),
        max_length=20,
        unique=True,
        null=True,
        blank=True,
        validators=username_validators,
        error_messages={
            "unique": _("The username is already taken"),
        },
        db_index=True,
    )
    full_name = models.CharField(_("full name"), max_length=150, blank=True, null=True)

    phone_number = models.CharField(max_length=20, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return f"@{self.username}"
