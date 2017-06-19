from rest_framework import serializers
from .. import image as imageModel

class ImageSerializer(serializers.ModelSerializer):
    """
        Serializer for the image model
    """

    class Meta:
        model = imageModel.Image
        fields = ('user_profile', 'created_on', 'updated_on', '')
        extra_kwargs = {'user_profile', {
            'read_only': True
        }}

    def create(self, validated_data):
        """
            Save image and return instance
        """

        print(validated_data)
