from rest_framework import serializers
from rest_framework import status
from . import models

# User Models
# TODO externalize this into /models dir

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
            Create and return new user
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

class UpdateUserSerializer(serializers.Serializer):

    email = serializers.EmailField(required=False, allow_blank=True)
    username = serializers.CharField(required=False, allow_blank=True)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)

    old_password = serializers.CharField(required=False, allow_blank=True)
    new_password = serializers.CharField(required=False, allow_blank=True)
    password = serializers.CharField(required=False, allow_blank=True)

    def update(self, instance, validated_data):
        """
            Update and return updated user
        """

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)

        if validated_data.get('old_password') and validated_data.get('old_password') and instance.check_password(validated_data.get('old_password')):
            instance.set_password(validated_data.get('new_password'))

        elif validated_data.get('old_password') and validated_data.get('old_password'):
            return {
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Passwords do not match'
            }

        instance.save()

        return {
            'message': 'updated',
            'status': status.HTTP_202_ACCEPTED
        }

    def delete(self, instance, validated_data):
        if not instance.check_password(validated_data.get('password')):
            return {'message':'Incorrect Pasword' , 'status':status.HTTP_400_BAD_REQUEST}

        instance.delete()
        return {'message':'Deleted' , 'status':status.HTTP_202_ACCEPTED}
