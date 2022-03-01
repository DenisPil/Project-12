from django.db import models

from customer.models import Customer
from staff.models import Staff


class Contract(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customercontract')
    sales_contact = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='salescontact')
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    is_signed = models.BooleanField(default=False)
