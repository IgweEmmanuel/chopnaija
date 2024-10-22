from rest_framework import permissions

class IsVendor(permissions.BasePermission):
    """
    Custom permission to only allow vendors to manage their own stores.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_vendor
