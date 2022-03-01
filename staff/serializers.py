from rest_framework import serializers
from .models import Staff


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name','role']