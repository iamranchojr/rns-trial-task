import os

from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string


def upload_encrypted_file(instance, filename):
    """
    function to return directory to upload encrypted file.
    :param instance: encrypted file
    :param filename: filename
    :return: directory to upload encrypted file
    """
    filename_split = filename.split('.')
    file_extension = filename_split[-1]
    filename = '{}.{}'.format(f'{filename_split[0]}{get_random_string(3)}', file_extension)
    return os.path.join(f'rns_trial_task/encrypted_files', filename)


class DateTimeFields(models.Model):
    """
    BaseModel class for providing date-time fields
    """
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Indicates that this model should not be created in the database.


class EncryptedFile(DateTimeFields):
    """
    Encrypted file model
    """
    file = models.FileField(upload_to=upload_encrypted_file)
