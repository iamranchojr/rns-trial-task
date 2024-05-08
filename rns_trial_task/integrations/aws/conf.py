import os

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_KEY')
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'eu-west-2'
# AWS_QUERYSTRING_EXPIRE = '604800'  # expires in 7 days

DEFAULT_FILE_STORAGE = 'rns_trial_task.integrations.aws.utils.MediaRootS3BotoStorage'
# STATICFILES_STORAGE = 'rns_trial_task.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_S3_BUCKET_NAME')
S3DIRECT_REGION = 'eu-west-2'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
