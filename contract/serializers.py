from rest_framework import serializers
from .models import Contract


class CreateContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['customer',
                  'sales_contact',
                  'amount',
                 ]

class ContractDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['customer',
                  'sales_contact',
                  'amount',
                 ]

class ContractListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id',
                  'customer',
                  'sales_contact',
                  'amount',
                 ]