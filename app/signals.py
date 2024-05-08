from django.db.models.signals import post_delete
from django.dispatch import receiver

from app.models import EncryptedFile


@receiver(post_delete, sender=EncryptedFile)
def delete_encrypted_file(sender, instance: EncryptedFile, **kwargs):
    """
    this deletes the file from amazon s3.
    False is set to make sure the record is not recreated
    :param sender: sender
    :param instance: EncryptedFile instance
    :param kwargs: keyword arguments
    """
    instance.file.delete(save=False)
