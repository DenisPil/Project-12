from django.contrib import admin

from .models import Staff


class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'role')
    
admin.site.register(Staff, StaffAdmin)