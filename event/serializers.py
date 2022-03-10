from rest_framework import serializers

from .models import Event


class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['contract_event',
                  'event_date',
                  'number_guests',
                  'commentary',
                  'event_status',
                  'support_contact']


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['contract_event',
                  'event_date',
                  'number_guests',
                  'commentary',
                  'support_contact']


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id',
                  'contract_event',
                  'event_date',
                  'number_guests',
                  'commentary',
                  'support_contact']
