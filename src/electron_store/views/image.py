from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from django.core.files.storage import default_storage
from ..utils.ImgUtil import ImgUtil

class UserImageUploadAPIView(GenericAPIView):
    """
        User image upload endpoint
    """

    permission_classes = [AllowAny]

    def post(self, request, format=None):
        """
            Upload image
        """

        ImgUtil.write(request.data['file'], 'ubuntu/images/user/profileImage')

        return Response(status=status.HTTP_200_OK)
