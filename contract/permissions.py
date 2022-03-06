from rest_framework.permissions import BasePermission
from rest_framework import permissions

from .models import Contract
from customer.models import Customer
from staff.models import Staff

STAFF_PERMS = ['GET']
CONTACT_PERMS = ['GET','PUT', 'DELETE', 'POST']


class IsSalesContact(BasePermission):

    def has_permission(self, request, view):
        print(request.data['sales_contact'],request.data)
        if request.method in CONTACT_PERMS:

            customer = Customer.objects.get(id=request.data['customer'])
            print(customer.sales_contact.id == request.user.id)
            if customer.sales_contact.id == request.user.id :
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