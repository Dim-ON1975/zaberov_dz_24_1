from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Права создателя (владельца)"""

    def has_object_permission(self, request, view, obj):
        if request.user.pk == obj.pk:
            return True
        return False
