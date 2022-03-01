from dataclasses import fields
from rest_framework import serializers
from .models import Event


class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['contract_event', 'event_date', 'number_guests', 'event_status','commentary', 'support_contact' ]