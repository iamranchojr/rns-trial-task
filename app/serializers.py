from rest_framework import serializers

from app.models import EncryptedFile


class EncryptedFileSerializer(serializers.ModelSerializer):
    """
    Serializer for EncryptedFile
    """

    class Meta:
        model = EncryptedFile
        fields = '__all__'
