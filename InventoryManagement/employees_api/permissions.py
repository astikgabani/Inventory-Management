from rest_framework import permissions


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Allow users to modify themselves.
    """

    def has_object_permission(self, request, view, obj):
        """
        Check whether user is trying to access their own profile.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id or request.user.is_superuser

    def has_permission(self, request, view):
        if not request.user.is_superuser and request.method in {'POST'}:
            return False
        return True
