from rest_framework.permissions import BasePermission
from rest_framework import permissions

from .models import Customer
from staff.models import Staff


NO_PERMS = []
STAFF_PERMS = ['GET']
CONTACT_PERMS = ['GET','PUT', 'DELETE', 'POST']


class IsStaff(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            if request.method in NO_PERMS:
                 return True
        else:
            if request.method in STAFF_PERMS:
                 return True


class IsSalesContact(BasePermission):

    def has_permission(self, request, view):
        print(view.kwargs,'-------4-------',request.user.role == 'sales team')
        if request.user.role == 'sales team':
            if request.method in CONTACT_PERMS:
                if 'pk' in view.kwargs:
                    customer = Customer.objects.get(id=view.kwargs['pk'])
                    if customer.sales_contact.id == request.user.id :
                        return True



class IsSupportContact(BasePermission):

    def has_permission(self, request, view):
        print(view.kwargs,'-------4-------',request.user.role == 'sales team')
        if request.user.role == 'sales team':
            if request.method in CONTACT_PERMS:
                if 'pk' in view.kwargs:
                    customer = Customer.objects.get(id=view.kwargs['pk'])
                    if customer.sales_contact.id == request.user.id :
                        return True