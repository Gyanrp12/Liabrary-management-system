from rest_framework.permissions import BasePermission
from .models import *


class LibrarianPermissions(BasePermission):
    def has_permission(self, request, view):
        user = User.objects.get(email=request.user)
        if user.user_type == 'librarian':
            return True


class UserPermissions(BasePermission):
    def has_permission(self, request, view):
        user = User.objects.get(email=request.user)
        if user.user_type == 'user':
            return True
