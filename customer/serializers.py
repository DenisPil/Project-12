from .models import Customer
from rest_framework import serializers


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email','phone', 'mobile','company_name','sales_contact']