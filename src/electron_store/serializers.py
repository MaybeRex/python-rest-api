from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    """
        A serializer for users
    """

    class Meta:
        model = models.UserProfile
        fields = ('email', 'username', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {
            'write_only': True
        }}

    def create(self, validated_data):
        print(validated_data)
        """
            create and return new user
        """

        user = models.UserProfile(
            email = validated_data['email'],
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
