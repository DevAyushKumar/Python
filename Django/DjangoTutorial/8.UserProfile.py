'''The core idea

Django's built-in User model only has basic auth fields (username, email, password, etc.) — no room for a profile picture, bio, etc. Rather than modifying User directly (risky, and not recommended), you create a separate Profile model linked to User via a OneToOneField. This is the standard pattern for extending Django's auth system.

1. The Profile model (models.py)
python
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

Key points:

OneToOneField means each User has exactly one Profile, and each Profile belongs to exactly one User — this is what "extending" the user model means in practice.
on_delete=models.CASCADE — if the User is deleted, their Profile is deleted too.
default='default.jpg' gives every new profile a placeholder image before the user uploads their own.
upload_to='profile_pics' tells Django to store uploaded images in a profile_pics/ subfolder inside MEDIA_ROOT.
The overridden save() method resizes large uploaded images down to 300×300px after saving — this needs the Pillow library:
bash
  pip install Pillow

Without Pillow installed, ImageField won't even work — Django will raise an error at migration time.

2. Auto-creating a Profile whenever a User signs up (signals)

This is the trickiest part of Part 8 conceptually. Since Profile is a separate model, a user could register without ever getting a Profile row — which would crash any code (like request.user.profile) that assumes one always exists. Django's signals solve this by hooking into the User creation process automatically.

users/signals.py:

python
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
post_save fires every time a User is saved.
created is True only the first time (i.e. on registration) — this ensures a Profile is created once, not duplicated on every login/update.
The second signal makes sure the profile is saved whenever the user object is saved elsewhere too.

users/apps.py — signals need to be explicitly connected when the app loads:

python
from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals

users/__init__.py:

python
default_app_config = 'users.apps.UsersConfig'

(Note: on modern Django (3.2+), this line is often unnecessary since Django auto-detects AppConfig — but explicitly setting default = True in apps.py or just relying on auto-discovery is fine too, depending on your Django version.)

3. Register Profile in admin (admin.py)
python
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)

This lets you view/edit profiles from /admin/, useful for debugging while building the feature.

4. Displaying the picture in a template
html
<img src="{{ user.profile.image.url }}" class="rounded-circle account-img">

user.profile works because of the OneToOneField — Django auto-creates that reverse accessor.

5. Media settings — required for image uploads to work at all

In settings.py:

python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

In the project's urls.py:

python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ...
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
6. Migrations

After adding the Profile model and signals:

bash
python manage.py makemigrations
python manage.py migrate

Since existing users (created before Profile existed) won't get a Profile automatically via the signal (it only fires on new user creation), you may need to manually create profiles for any pre-existing users in the shell:

python
from django.contrib.auth.models import User
from users.models import Profile

for user in User.objects.all():
    Profile.objects.get_or_create(user=user)'''