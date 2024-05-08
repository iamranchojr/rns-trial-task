from django.contrib import admin

from app.models import EncryptedFile


@admin.register(EncryptedFile)
class EncryptedFileModelAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False
