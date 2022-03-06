from django.contrib import admin

from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display =('id', 'first_name', 'last_name', 'company_name', 'sales_contact')

admin.site.register(Customer, CustomerAdmin)