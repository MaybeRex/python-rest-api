from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from . import models

# Create your views here.

class UserRegisterAPIView(CreateAPIView):
    """
        User register
    """

    serializer_class = serializers.UserSerializer
    queryset = models.UserProfile.objects.all()

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

class UserLoginAPIView(APIView):
    pass
