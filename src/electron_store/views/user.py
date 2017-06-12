from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from ..serializers import user as userSerializers
from ..models import user as userModels
from ..permissions.isSelf import IsSelf

# Create your views here.

class UserRegisterAPIView(CreateAPIView):
    """
        User registration endpoint
    """

    serializer_class = userSerializers.UserSerializer
    queryset = userModels.UserProfile.objects.all()

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
    permission_classes = (IsSelf,)
    serializer_class = userSerializers.UpdateUserSerializer
    queryset = userModels.UserProfile.objects.all()
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
            return Response({'detail': updateResult['message']}, status=updateResult['status'])

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username, format=None):
        """
            Delete profile
        """
        if (    # NOTE check that all these fields are passed in
                not request.data.get('first_name') or
                not request.data.get('last_name') or
                not request.data.get('username') or
                not request.data.get('email') or
                not request.data.get('password')
            ):
            return Response({'detail': 'Missing Parameters'}, status=status.HTTP_400_BAD_REQUEST)

        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            deleteResult = serializer.delete(instance, serializer.validated_data)
            return Response({'detail': deleteResult['message']}, status=deleteResult['status'])
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
