from django.db import models
from django.core.validators import RegexValidator

from contract.models import Contract
from staff.models import Staff


class Status(models.Model):
    event_status = models.BooleanField(default=False)
    commentary = models.TextField(max_length=256, blank=True, null=True)
    # event_status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='eventstatus')


class Event(models.Model):
    contract_event = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='contractevent')
    event_date = models.DateField(verbose_name='eventdate')
    number_guests = models.IntegerField(blank=True, null=True)
    event_status = models.BooleanField(default=False)
    commentary = models.TextField(max_length=256)
    support_contact = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='supportcontact')
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
