from cryptography.fernet import Fernet
from django.core.files.base import ContentFile
from django.db.models import FileField

from app.models import EncryptedFile


def _encrypt_file(file: FileField) -> (bytes, bytes):
    """
    This function takes a file and returns an encrypted form
    of it in bytes along with the key used for encryption
    :param file: File that needs to be encrypted
    :return: tuple containing the encrypted file and the key used for encryption
    """

    # generate encryption key and create a new fernet instance
    encryption_key = Fernet.generate_key()
    fernet = Fernet(key=encryption_key)

    # read and encrypt the file
    encrypted_file = fernet.encrypt(data=file.read())

    return encrypted_file, encryption_key


def decrypt_file(encrypted_file: EncryptedFile, encryption_key: bytes) -> bytes:
    """
    This function takes an encrypted file and returns a decrypted form of it
    :param encrypted_file: File that needs to be decrypted
    :param encryption_key: Key used for encryption
    :return: Decrypted file
    """
    fernet = Fernet(key=encryption_key)
    return fernet.decrypt(
        token=encrypted_file.file.read()
    )


def create_encrypted_file(file: FileField) -> (EncryptedFile, bytes):
    """
    This function creates an encrypted version of the provided file and uploads it
    :param file: File that needs to be encrypted
    :return: tuple containing the encrypted file model object and the key used for encryption
    """
    # encrypt file
    encrypted_file, encryption_key = _encrypt_file(file)

    # create a django friendly file object since we cannot save encrypted bytes
    content_file = ContentFile(
        content=encrypted_file,
        name=file.name,
    )

    # create object and upload file
    encrypted_file_object = EncryptedFile.objects.create(
        file=content_file,
    )

    # return created object and encryption key
    return encrypted_file_object, encryption_key
