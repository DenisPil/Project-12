from rest_framework import serializers
from .models import Contract
from customer.serializers import CustomerListSerializer

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
    
    # customer = CustomerListSerializer(many=True)
    
    class Meta:
        model = Contract
        fields = ['id',
                  'customer',
                  'sales_contact',
                  'amount',
                 ]

class ContractParamSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Contract
        fields = ['id',
                  'customer',
                  'sales_contact',
                  'amount',
                 ]
