from django.shortcuts import render
from .serializers import CustomerListSerializer, CustomerDetailSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required

from .permissions import IsStaff, IsSallesContact, IsSupportContact
from .models import Customer
from staff.models import Staff


class MultipleSerializerMixin:
    
    """ Mixin permet d'afficher les vues en détail ou en liste"""

    detail_serializer_class = None
    
    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class CustomerViewSet(MultipleSerializerMixin, ModelViewSet):
    
    """ Le ModelViewSet de l'inscription """

    serializer_class = CustomerListSerializer
    detail_serializer_class = CustomerDetailSerializer
    permission_classes = [IsStaff, IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        queryset = Customer.objects.all()
        """if "pk" in self.kwargs:
            return Customer.objects.filter(pk=self.kwargs['pk'])
        queryset = Customer.objects.filter(Q(creator_id=self.request.user.id))"""
        return queryset
    
    def create(self, request):
        serializer = CustomerDetailSerializer(data=request.data)
        data = {}
        print(request.data['sales_contact'],'-----------------------')
        valid_staff = Staff.objects.get(pk=request.data['sales_contact'])
        if valid_staff.role != 'sales team':
            data['response'] = "Staff is not from sales team"
            return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE) 
        else:
            if serializer.is_valid(request):
                serializer.save()
                data['response'] = "Successfully registered a new user"
            return Response(data, status=status.HTTP_201_CREATED) 


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED, headers=headers)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        data = {"response": "Le client est supprimé."}
        return Response(data, status=status.HTTP_204_NO_CONTENT)