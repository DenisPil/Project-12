from tkinter import CURRENT
from django.db import models

from contract.models import Contract
from staff.models import Staff


class Status(models.TextChoices):
    
    PAYMENT_IN_PROGRESS = 'paiement en cours'
    FULL_PAYMENT = 'payé'
    FUTURE_EVENT =  'événement à venir'
    CURRENT_EVENT = 'événement en cours'
    ENDED_EVENT = 'événement terminé'

class Event(models.Model):
    contract_event = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='contractevent')
    event_date = models.DateField(verbose_name='eventdate')
    number_guests = models.IntegerField(blank=True, null=True)
    event_status = models.fields.CharField(choices=Status.choices, max_length=32)
    commentary = models.TextField(max_length=256)
    support_contact = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='supportcontact')
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
