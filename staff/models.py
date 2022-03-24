from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class EpicManager(BaseUserManager):
    def create_user(self, username, password, role, **extra_fields):

        user = self.model(username=username, role=role, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, role="management team", **extra_fields):
        user = self.create_user(
            username=username,
            password=password,
            role=role,
        )
        if user.role == "management team":
            user.is_admin = True
            user.is_superuser = True
            user.is_staff = True
            user.save()
            return user


class Role(models.TextChoices):
    management_team = 'management team'
    sales_team = 'sales team'
    support_team = 'support team'

class Staff(AbstractUser):
    role = models.CharField(max_length=28, choices=Role.choices, verbose_name='role')
    objects = EpicManager()
