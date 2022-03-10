from rest_framework.permissions import BasePermission

from .models import Event
from contract.models import Contract


STAFF_PERMS = ['GET']
SALES_PERMS = ['GET', 'POST']
SUPPORT_PERMS = ['GET', 'PUT', 'DELETE']
MANAGEMENT_PERMS = ['GET', 'PUT', 'POST', 'DELETE']


class IsSalesContact(BasePermission):

    """Les permissions de l'équipe de vente pour les événements"""

    def has_permission(self, request, view):
        if request.method in SALES_PERMS:
            if request.data.__contains__('contract_event'):
                contract = Contract.objects.get(id=request.data['contract_event'])
                if contract.sales_contact.id == request.user.id:
                    return True
                else:
                    if request.method in STAFF_PERMS:
                        return True
            else:
                if request.method in STAFF_PERMS:
                    return True


class IsManagementTeam(BasePermission):

    """Les permissions de l'équipe de management pour les événements"""

    def has_permission(self, request, view):
        if request.user.role == 'management team':
            if request.method in MANAGEMENT_PERMS:
                return True


class IsSupportTeam(BasePermission):

    """Les permissions de l'équipe support pour les événements"""

    def has_permission(self, request, view):
        if request.method in SUPPORT_PERMS:
            if 'pk' in view.kwargs:
                print(view.kwargs)
                event = Event.objects.get(id=view.kwargs['pk'])
                if event.support_contact.id == request.user.id:
                    return True
                else:
                    if request.method in STAFF_PERMS:
                        return True
            else:
                if request.method in STAFF_PERMS:
                    return True
