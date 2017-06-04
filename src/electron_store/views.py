from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from . import serializers
from . import models
from . import persmissions

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

class UserUpdateAPIView(APIView):

    def patch(self, request, format=None):
        """
            Update user profile
        """

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        """
            Delete profile
        """

        return Response(status=status.HTTP_200_OK)
