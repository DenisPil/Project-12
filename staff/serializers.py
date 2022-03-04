from rest_framework import serializers
from .models import Staff


class StaffSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['username',
                  'password',
                  'email',
                  'role',
                 ]

class StaffDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['username',
                  'email',
                  'role',
                 ]

class StaffListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id',
                  'username',
                  'email',
                  'role'
                ]