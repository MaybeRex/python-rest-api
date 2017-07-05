from rest_framework import serializers
from ..models import image as imageModel

class ImageSerializer(serializers.ModelSerializer):
    """
        Serializer for the image model
    """

    class Meta:
        model = imageModel.Image
        fields = ('user_profile', 'created_on', 'updated_on', 'file_path')

        extra_kwargs = {'user_profile': {
            'read_only': True
        }}

    def create(self, validated_data):
        """
            Save image and return instance
        """
        # TODO add user_profile_id
        image = imageModel.Image(
            file_path = validated_data['file_path'],
            user_profile_id = 3
        )
        image.save()

        return image
