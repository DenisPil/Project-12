from rest_framework import serializers

from .models import Staff


class StaffSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['username',
                  'password',
                  'email',
                  'role']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        account = Staff(email=self.validated_data['email'],
                        username=self.validated_data['username'],
                        role=self.validated_data['role'])
        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account


class StaffDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['username',
                  'email',
                  'role']

class StaffListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id',
                  'username',
                  'email',
                  'role']
