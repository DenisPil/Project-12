from rest_framework.permissions import BasePermission
from rest_framework import permissions


STAFF_PERMS = ['GET']
MANAGEMENT_PERMS = ['GET','PUT', 'DELETE', 'POST']


class IsSalesContact(BasePermission):

    def has_permission(self, request, view):
        if request.user.role == 'sales team':
            if request.method in STAFF_PERMS:
                return True


class IsManagementTeam(BasePermission):

    def has_permission(self, request, view):
        if request.user.role == 'management team':
            if request.method in MANAGEMENT_PERMS:
                return True


class IsSupportTeam(BasePermission):
    
    def has_permission(self, request, view):
        if request.user.role == 'support team':
            if request.method in STAFF_PERMS:
                return True