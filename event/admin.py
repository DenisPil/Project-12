from django.contrib import admin

from .models import Event, Status

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'contract_event','event_date','support_contact', 'event_status')


admin.site.register(Event, EventAdmin)
admin.site.register(Status)