from rest_framework.permissions import BasePermission

from customer.models import Customer


STAFF_PERMS = ['GET']
CONTACT_PERMS = ['GET', 'PUT', 'DELETE', 'POST']


class IsSalesContact(BasePermission):

    """Les permissions de l'équipe de vente pour les contracts"""

    def has_permission(self, request, view):
        if request.method in CONTACT_PERMS:
            if request.data.__contains__('customer'):
                customer = Customer.objects.get(id=request.data['customer'])
                if customer.sales_contact.id == request.user.id:
                    return True
            else:
                if request.method in STAFF_PERMS:
                    return True


class IsManagementTeam(BasePermission):

    """Les permissions de l'équipe de management pour les contracts"""

    def has_permission(self, request, view):
        if request.user.role == 'management team':
            if request.method in CONTACT_PERMS:
                return True


class IsSupportTeam(BasePermission):

    """Les permissions de l'équipe support pour les contracts"""

    def has_permission(self, request, view):
        if request.user.role == 'support team':
            if request.method in STAFF_PERMS:
                return True
