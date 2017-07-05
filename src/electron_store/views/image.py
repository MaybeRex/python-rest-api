from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from ..serializers import image as imageSerializers
from ..permissions.isSelf import IsSelf
from ..models import image as imageModels
from ..utils.ImgUtil import ImgUtil

class UserImageUploadAPIView(GenericAPIView):
    """
        User image upload endpoint
    """

    serializer_class = imageSerializers.ImageSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = imageModels.Image.objects.all()
    lookup_field = 'username'

    permission_classes = [
        IsSelf
    ]

    def post(self, request, username, format=None):
        """
            Upload image
        """
        pathWritten = 'ubuntu/images/{}/profileImage'.format(username)

        ImgUtil.write(request.data['file'], pathWritten)
        request.data['file_path'] = pathWritten
        del request.data['file']

        data = {
            'file_path': pathWritten,
            'user_profile_id': # TODO add the correct image id here instead of the profile name
        }

        # TODO get the user model, extract the ID, and based on
        # if the image is in the DB, create or update it

        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            image = serializer.save()
            if image:
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_400_BAD_REQUEST)
