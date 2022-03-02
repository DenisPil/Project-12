from django.shortcuts import render
from .serializers import SignupSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import Customer

class SignUpViewSet(ModelViewSet):
    
    """ Le ModelViewSet de l'inscription """

    serializer_class = SignupSerializer
    
    def get_queryset(self, *args, **kwargs):
        queryset = Customer.objects.all()
        """if "pk" in self.kwargs:
            return Customer.objects.filter(pk=self.kwargs['pk'])
        queryset = Customer.objects.filter(Q(creator_id=self.request.user.id))"""
        return queryset
    
    def create(self, request):
        serializer = SignupSerializer(data=request.data)
        data = {}
        if serializer.is_valid(request):
            account = serializer.save()
            data['response'] = "Successfully registered a new user"

        return Response(data, status=status.HTTP_201_CREATED)