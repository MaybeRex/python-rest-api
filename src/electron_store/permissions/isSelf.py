from rest_framework import permissions
from django.conf import settings

import jwt

class IsSelf(permissions.BasePermission):
    """
        Checks if models is self
    """

    def has_object_permission(self, request, view, obj):
        """
            Only lets self through
        """

        token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
        decodedToken = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

        return obj.id == request.user.id == decodedToken['user_id']
