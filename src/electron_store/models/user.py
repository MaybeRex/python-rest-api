from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.

class UserProfileManager(BaseUserManager):
    """
        Helps Django work with our custom user models
    """

    def create_user(self, email, username, first_name, last_name, password):
        """
            Creates a new user profile object
        """

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, username, first_name, last_name, password):
        """
            Creates and saves a new superuser with given details
        """

        user = self.create_user(
            email,
            username,
            first_name,
            last_name,
            password
        )

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
        User profile in our system
    """

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    # NOTE ^^^ those are needed

    #  NOTE these are needed
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # NOTE this is needed
    objects = UserProfileManager()

    # NOTE so is this
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    # extra fields that I've added
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    # DOCS https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.DateField
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # NOTE and this
    def get_full_name(self):
        """
            get full name of user
        """
        return '{}, {}'.format(self.last_name, self.first_name)

    # NOTE this too
    def get_short_name(self):
        """
            get short name of user
        """
        return self.username

    def ___str___(self):
        return self.email


#
# class AppEntry(models.Model):
#     """
#         Database model for storing electron app
#     """
#
#     user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE) # NOTE, should we? idk
#     app_name = models.CharField(max_length=15)
#     description = models.TextField() # NOTE have to validate against HTML insertions
#
#     # binary = ???? #TODO figure this out
#
#     created_on = models.DateTimeField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now=True)
