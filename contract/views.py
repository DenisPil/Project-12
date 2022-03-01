from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import CreateContractSerializer

class SignUpContractViewSet(ModelViewSet):
    
    """ Le ModelViewSet de l'inscription """

    serializer_class = CreateContractSerializer
    
    def create(self, request):
        serializer = CreateContractSerializer(data=request.data)
        data = {}
        if serializer.is_valid(request):
            account = serializer.save()
            data['response'] = "Successfully registered a new Contract"

        return Response(data, status=status.HTTP_201_CREATED)