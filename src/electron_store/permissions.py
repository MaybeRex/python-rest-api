from rest_framework import permissions
from django.conf import settings

import jwt

# Custom persmissions go here

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """
            Only let Owner perform write operations on themselves
        """
        token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
        decodedToken = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

        return obj.id == request.user.id == decodedToken['user_id']
