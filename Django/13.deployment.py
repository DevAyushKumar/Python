'''Django Tutorial Part 13: Using AWS S3 for File UploadsThis lecture covers configuring Amazon Web Services (AWS) Simple Storage Service (S3) to host media files (like user profile pictures) instead of storing them on the local filesystem. Storing uploads on AWS S3 allows the web application to scale smoothly across different servers or deployment platforms (such as Heroku or AWS EC2).  1. Prerequisites & Package InstallationTo integrate Django with AWS S3, install boto3 (AWS SDK for Python) and django-storages (Django custom storage backends):Bashpip install boto3 django-storages
Add storages to your INSTALLED_APPS:django_project/settings.pyPythonINSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
    'storages',  # Added for AWS S3 file management
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
2. AWS S3 & IAM User Setup SummaryCreate S3 Bucket:Log into AWS Console -> S3 -> Create Bucket (e.g., django-blog-files).Uncheck "Block all public access" (or set proper bucket policies for reading uploads) and set up CORS configuration if needed.CORS Configuration (S3 Permission Tab):JSON[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "POST",
            "PUT"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
Create IAM User for Access Credentials:AWS IAM -> Users -> Add User.Attach Policy directly: AmazonS3FullAccess.Save the AWS Access Key ID and AWS Secret Access Key.3. Environment Variables ConfigurationStore credentials safely as system environment variables rather than hardcoding them into source control:Mac/Linux (~/.bash_profile or ~/.zshrc):Bashexport AWS_ACCESS_KEY_ID="your_access_key_id"
export AWS_SECRET_ACCESS_KEY="your_secret_access_key"
export AWS_STORAGE_BUCKET_NAME="your_s3_bucket_name"
Windows Command Prompt:DOSsetx AWS_ACCESS_KEY_ID "your_access_key_id"
setx AWS_SECRET_ACCESS_KEY "your_secret_access_key"
setx AWS_STORAGE_BUCKET_NAME "your_s3_bucket_name"
4. Setting up S3 Settings in DjangoAdd AWS S3 storage variables to your project settings:django_project/settings.pyPythonimport os

# Media settings for local development
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# AWS S3 Storage Settings
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

# Prevent overwriting files with the same name
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

# Set S3 as the default file storage backend
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
5. Refactoring Profile Model save() MethodIn Part 9, a custom save() method was added to resize profile images using Pillow with local file paths (self.image.path). Because S3 remote storage does not use local disk paths, self.image.path will raise an NotImplementedError or FileNotFoundError when uploading to S3.  Remove or comment out the overridden save() method in users/models.py (or handle image resizing via AWS Lambda / client-side processing instead):users/models.pyPythonfrom django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Remove or comment out the overridden save() method that relied on self.image.path:
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
With this configuration complete, all newly uploaded profile pictures will automatically upload directly to your S3 bucket, and Django will dynamically construct and serve the AWS S3 URL for user avatars.'''