from django.shortcuts import render
from .serializers import CustomerListSerializer, CustomerDetailSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSupportTeam, IsSalesContact, IsManagementTeam
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
    permission_classes = [IsAuthenticated, IsSalesContact | IsManagementTeam | IsSupportTeam]

    def get_queryset(self, *args, **kwargs):
        queryset = Customer.objects.all()
        customer_email = self.request.GET.get('email')
        customer_name = self.request.GET.get('name')
        if customer_email:
            queryset = Customer.objects.filter(email=customer_email)
        elif customer_name:
            queryset = Customer.objects.filter(last_name=customer_name)
        return queryset

    def create(self, request):
        serializer = CustomerDetailSerializer(data=request.data)
        data = {}
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