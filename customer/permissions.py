from rest_framework.permissions import BasePermission
from rest_framework import permissions

from .models import Customer


STAFF_PERMS = ['GET']
CONTACT_PERMS = ['GET','PUT', 'DELETE', 'POST']


class IsSalesContact(BasePermission):

    def has_permission(self, request, view):
        if request.method in CONTACT_PERMS:
            if 'pk' in view.kwargs:
                customer = Customer.objects.get(id=view.kwargs['pk'])
                print(customer.sales_contact.id == request.user.id)
                if customer.sales_contact.id == request.user.id :
                    return True
                else:
                    return False
            else:
                if request.user.role == "sales team" :
                    return True
                else:
                    return False


class IsManagementTeam(BasePermission):

    def has_permission(self, request, view):
        if request.user.role == 'management team':
            if request.method in CONTACT_PERMS:
                return True


class IsSupportTeam(BasePermission):
    
    def has_permission(self, request, view):
        if request.user.role == 'support team':
            if request.method in STAFF_PERMS:
                return True