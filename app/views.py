import base64

from cryptography.fernet import InvalidToken
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, DestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from app.models import EncryptedFile
from app.serializers import EncryptedFileSerializer
from app.services import create_encrypted_file, decrypt_file


class UploadEncryptedFileAPI(GenericAPIView):
    """
    This API endpoint allows you to upload encrypted files.
    The encryption is done by the API itself and uploaded to S3
    """

    def post(self, request, *args, **kwargs):
        try:
            # encrypt uploaded file
            encrypted_file, encryption_key = create_encrypted_file(
                file=request.FILES['file']
            )

            # serialize data
            serializer = EncryptedFileSerializer(
                instance=encrypted_file,
                context={'request': request},
            )

            # return response of encrypted file and encryption key
            return Response(
                data={
                    'encrypted_file': serializer.data,
                    'encryption_key': encryption_key,
                },
                status=status.HTTP_201_CREATED,
            )
        except KeyError:
            return Response(
                data={'error': 'No file provided'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except TypeError as e:
            return Response(
                data={'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class DecryptEncryptedFileAPI(GenericAPIView):
    queryset = EncryptedFile.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            encrypted_file = self.get_object()
            decrypted_file = decrypt_file(
                encrypted_file=encrypted_file,
                encryption_key=request.data['encryption_key'],
            )

            # encode decrypted file as base64 image and return it
            base64_file = base64.b64encode(decrypted_file)

            return Response(
                data={'decrypted_file': base64_file}
            )
        except KeyError:
            return Response(
                data={'error': 'Encryption key not provided'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except (TypeError, ValueError, InvalidToken) as e:
            return Response(
                data={'error': str(e) or 'Invalid encryption key provided'},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ListEncryptedFileAPI(ListAPIView):
    serializer_class = EncryptedFileSerializer
    queryset = EncryptedFile.objects.all()
    pagination_class = LimitOffsetPagination
    ordering = ['-created_at']
    ordering_fields = ['created_at']


class DeleteEncryptedFileAPI(DestroyAPIView):
    serializer_class = EncryptedFileSerializer
    queryset = EncryptedFile.objects.all()
