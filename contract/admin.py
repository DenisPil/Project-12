from django.contrib import admin

from .models import Contract

class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'sales_contact', 'status')

admin.site.register(Contract, ContractAdmin)