from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from .enums import UserRole
from .managers import CustomManager


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=13, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=5, choices=UserRole.choices(), blank=True, null=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["role"]

    def __str__(self):
        return self.phone


class SmsRegister(models.Model):
    phone = models.CharField(max_length=13)
    code = models.IntegerField()

    def __str__(self):
        return f"{self.phone}: {self.code}"