from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from rest_framework_jwt.authentication import JSONWebTokenAuthentication


from . import serializers
from . import models
from . import permission

# Create your views here.

class UserRegisterAPIView(CreateAPIView):
    """
        User register
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
        serializer = serializers.UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserUpdateAPIView(GenericAPIView):

    authentication_classes = (JSONWebTokenAuthentication,)
    persmission_classes = (permission.IsOwner,)
    serializer_class = serializers.UpdateUserSerializer
    queryset = models.UserProfile.objects.all()
    lookup_field = 'username'

    def patch(self, request, username,format=None):
        """
            Update user profile
        """
        # instance = self.get_object()
        # data = {
        #     'id': request.data.id,
        #     'username': request.data.username,
        #     'token': str(request.auth)
        # }

        print(self.get_queryset())
        print(self.get_object())

        instance = self.get_object()
        # return Response(data)
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        """
            Delete profile
        """

        return Response(status=status.HTTP_200_OK)
