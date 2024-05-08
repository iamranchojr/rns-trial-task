from django.urls import path

from app import views

urlpatterns = [
    path('upload/', views.UploadEncryptedFileAPI.as_view(), name='upload-encrypted-file'),
    path('list/', views.ListEncryptedFileAPI.as_view(), name='list-encrypted-file'),
    path('<int:pk>/delete/', views.DeleteEncryptedFileAPI.as_view(), name='delete-encrypted-file'),
    path('<int:pk>/decrypt/', views.DecryptEncryptedFileAPI.as_view(), name='decrypt-encrypted-file'),
]
