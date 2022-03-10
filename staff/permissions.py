from rest_framework.permissions import BasePermission


STAFF_PERMS = ['GET']
MANAGEMENT_PERMS = ['GET', 'PUT', 'DELETE', 'POST']


class IsSalesContact(BasePermission):

    """Les permissions de l'équipe de vente pour le staff"""

    def has_permission(self, request, view):
        if request.user.role == 'sales team':
            if request.method in STAFF_PERMS:
                return True


class IsManagementTeam(BasePermission):

    """Les permissions de l'équipe de management pour le staff"""

    def has_permission(self, request, view):
        if request.user.role == 'management team':
            if request.method in MANAGEMENT_PERMS:
                return True


class IsSupportTeam(BasePermission):

    """Les permissions de l'équipe support pour le staff"""

    def has_permission(self, request, view):
        if request.user.role == 'support team':
            if request.method in STAFF_PERMS:
                return True
