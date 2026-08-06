'''The goal

Let a logged-in user edit two things at once on one page: their core User fields (username, email) and their Profile fields (like a profile picture). Since User and Profile are two separate models, this needs two forms on one page, submitted together.

1. Two ModelForms in forms.py
python
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
fields (plural, not field) is required on every ModelForm.Meta — this is exactly the bug from your earlier screenshot.
email is redeclared explicitly because Django's default User model doesn't mark email as required — this makes it a required field in the form.
2. One view handling both forms
python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)

Key points:

instance=request.user pre-fills the form with the logged-in user's current data, and makes .save() update that same row instead of creating a new one.
request.FILES is required alongside request.POST whenever a form includes a file/image upload — forgetting it is a very common bug (the image field will always come back empty).
Both forms must pass .is_valid() before either is saved, so you don't end up with one model updated and not the other.
3. Template — both forms in one <form> tag
html
{% extends "blog/base.html" %}
{% block content %}
<div class="content-section">
  <form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    <fieldset class="form-group">
      <legend class="border-bottom mb-4">Profile Info</legend>
      {{ u_form.as_p }}
      {{ p_form.as_p }}
    </fieldset>
    <div class="form-group">
      <button class="btn btn-outline-info" type="submit">Update</button>
    </div>
  </form>
</div>
{% endblock content %}
enctype="multipart/form-data" is mandatory on the <form> tag whenever any field is a file upload — without it, the image never actually gets sent to the server.
Both forms render inside the same <form> element since they're submitted together in one POST request.
4. settings.py — serving uploaded images in development
python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

And in the project's urls.py:

python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your paths
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Without this, uploaded images save to disk fine but return 404 when the browser tries to display them.
'''