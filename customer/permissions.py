from rest_framework.permissions import BasePermission
from rest_framework import permissions

from .models import Customer
from staff.models import Staff



STAFF_PERMS = ['GET']
CONTACT_PERMS = ['PUT', 'DELETE', 'POST']


class IsStaff(BasePermission):

    print('mabite')
    def has_permission(self, request, view):
        customers = Customer.objects.get(id=view.kwargs['projects__pk'])
        print(customers,'55555555555555555555555555555555555')
        if customers.creator.id == request.user.id:
            if request.method in STAFF_PERMS:
                return True


class IsSallesContact(BasePermission):

    def has_permission(self, request, view):
        contributeurs_project = Staff.objects.filter(
            project_id__id=view.kwargs['projects__pk'])
        for contributor in contributeurs_project:
            if contributor.contributor_id.id == request.user.id:
                if request.method in CONTACT_PERMS:
                    return True


class IsSupportContact(BasePermission):

    def has_permission(self, request, view):
        if 'pk' in view.kwargs:
            issue = Staff.objects.get(id=view.kwargs['pk'])
            if issue.assignee_user_id.id == request.user.id:
                if request.method in CONTACT_PERMS:
                    return True
