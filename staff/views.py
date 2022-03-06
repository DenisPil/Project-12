from django.shortcuts import render
from django.shortcuts import render
from .serializers import StaffDetailSerializer, StaffListSerializer, StaffSignupSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import Staff
from .permissions import IsSupportTeam, IsSalesContact, IsManagementTeam
from rest_framework.permissions import IsAuthenticated

class MultipleSerializerMixin:
    
    """ Mixin permet d'afficher les vues en détail ou en liste"""

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class StaffViewSet(MultipleSerializerMixin, ModelViewSet):
    
    """ Le ModelViewSet de l'inscription """

    serializer_class = StaffListSerializer
    detail_serializer_class = StaffDetailSerializer
    permission_classes = [IsAuthenticated, IsSalesContact | IsManagementTeam | IsSupportTeam]
    
    def get_queryset(self, *args, **kwargs):
        queryset = Staff.objects.all()
        return queryset
    
    def create(self, request):
        serializer = StaffSignupSerializer(data=request.data)
        data = {}
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
        data = {"response": "Le collaborateur est supprimé."}
        return Response(data, status=status.HTTP_204_NO_CONTENT)