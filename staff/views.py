from django.shortcuts import render
from django.shortcuts import render
from .serializers import SignupSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import Staff

class SignUpStaffViewSet(ModelViewSet):
    
    """ Le ModelViewSet de l'inscription """

    serializer_class = SignupSerializer
    
    def create(self, request):
        serializer = SignupSerializer(data=request.data)
        data = {}
        if serializer.is_valid(request):
            account = serializer.save()
            data['response'] = "Successfully registered a new user"
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.error
        return Response(data, status=status.HTTP_201_CREATED)