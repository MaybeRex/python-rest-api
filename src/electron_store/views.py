from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from . import serializers
from . import models
from . import permissions

# Create your views here.

class UserRegisterAPIView(CreateAPIView):
    """
        User registration endpoint
    """

    serializer_class = serializers.UserSerializer
    queryset = models.UserProfile.objects.all()

    permission_classes = [
        AllowAny # Or anon users can't register
    ]

    def post(self, request, format=None):
        """
            Creates a user
        """
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserUpdateAPIView(GenericAPIView):
    """
        User update endpoint
    """

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsOwner,)
    serializer_class = serializers.UpdateUserSerializer
    queryset = models.UserProfile.objects.all()
    lookup_field = 'username'

    def patch(self, request, username,format=None):
        """
            Update user profile
        """

        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)

        # NOTE use this to manually check permissions
        # self.check_object_permissions(request, obj)
        if serializer.is_valid():
            updateResult = serializer.update(instance, serializer.validated_data)

            return Response({'message': updateResult['message']}, status=updateResult['status'])
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        """
            Delete profile
        """

        return Response(status=status.HTTP_200_OK)

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'status': status.HTTP_200_OK
    }
