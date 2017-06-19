from os import makedirs
from os.path import isdir
from django.conf import settings

class ImgUtil(object):
    """
        Utility class for writing, deleting and updating images
    """

    @staticmethod
    def write(file, path):
        """
            Static method for writing images
        """
        if not isdir(path):
            makedirs('{}/{}'.format(settings.FILES_DIR, path), exist_ok=True)

        with open('{}/{}/image.png'.format(settings.FILES_DIR, path), 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return True

    @staticmethod
    def deleteImage(path):
        """
            Static method for deleting images
        """
        pass
