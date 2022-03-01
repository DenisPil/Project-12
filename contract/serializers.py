from rest_framework import serializers
from .models import Contract

class CreateContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['sales_contact', 'customer', 'status', 'amount']