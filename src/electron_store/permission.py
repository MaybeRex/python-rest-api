from rest_framework import permissions

# Custom persmissions go here

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """Only let Owner perform write operations on themselves"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
