from django.db import models
from django.core.validators import RegexValidator

from staff.models import Staff

#  
class Customer(models.Model):
    first_name = models.CharField(max_length=24, verbose_name='fname')
    last_name = models.CharField(max_length=24, verbose_name='lname')
    email = models.EmailField(max_length=128, unique=True, verbose_name='email')
    phone = models.CharField(max_length=32, null=True, blank=True, validators=[RegexValidator(r'^((\+)33|0|0033)[1-9](\d{2}){4}$')], verbose_name='phone')
    mobile = models.CharField(max_length=32, verbose_name='mobile', validators=[RegexValidator(r'^((\+)33|0|0033)[1-9](\d{2}){4}$')])
    company_name = models.CharField(max_length=64, verbose_name='company_name')
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    sales_contact = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='sales_contact')

