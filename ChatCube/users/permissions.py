from rest_framework import permissions

class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, customuser):
        if request.user:
            return customuser == request.user
        return False