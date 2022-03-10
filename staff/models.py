from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.TextChoices):
    management_team = 'management team'
    sales_team = 'sales team'
    support_team = 'support team'

class Staff(AbstractUser):
    role = models.CharField(max_length=28, choices=Role.choices, verbose_name='role')
