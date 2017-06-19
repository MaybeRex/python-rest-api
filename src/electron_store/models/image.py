from django.db import models
from . import user

class Image(models.Model):
    """
        Profile image model
    """

    user_profile = models.OneToOneField(
        user.UserProfile,
        on_delete=models.CASCADE,
        primary_key=True
    )

    created_on = models.DateField(auto_now_add=True)
    updated_on = updated_on = models.DateTimeField(auto_now=True);

    file_path = models.CharField(max_length=255)

    def __str__(self):
        """
            Return the adress of thr string
        """
        return self.file_path
