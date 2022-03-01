from django.shortcuts import render
from .serializers import SignupSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import Customer

class SignUpViewSet(ModelViewSet):
    
    """ Le ModelViewSet de l'inscription """

    serializer_class = SignupSerializer
    
    def create(self, request):
        serializer = SignupSerializer(data=request.data)
        data = {}
        if serializer.is_valid(request):
            account = serializer.save()
            data['response'] = "Successfully registered a new user"

        return Response(data, status=status.HTTP_201_CREATED)