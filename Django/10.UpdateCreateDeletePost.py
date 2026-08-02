'''This part covers Django's class-based generic views for full CRUD (Create, Read, Update, Delete) on the Post model — building directly on PostListView and PostDetailView from earlier, and ties directly into the PostUpdateView bug we just fixed.

1. The four generic views (views.py)
python
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

Key points on each:

CreateView auto-generates a form from fields, and on submit calls form_valid() — overridden here to stamp author = request.user before saving, since author isn't in the editable fields list (users shouldn't be able to type in someone else's name as author).
UpdateView works almost identically to CreateView, but pre-fills the form with an existing object (matched via pk from the URL) instead of creating a new one.
DeleteView doesn't need a form at all — it just shows a confirmation page, and on POST, deletes the object and redirects to success_url.
LoginRequiredMixin blocks anonymous users entirely (redirects to LOGIN_URL).
UserPassesTestMixin + test_func() blocks logged-in users who aren't the post's author (403 Forbidden) — this is the piece that was missing in your earlier bug.
reverse_lazy (imported above) is used instead of reverse() whenever a URL needs to be resolved at class-definition time rather than at request time — e.g. if you set success_url = reverse_lazy('blog-home') instead of a hardcoded string.
2. URL patterns (urls.py)
python
from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

Note the ordering matters less here since post/new/ and post/<int:pk>/ won't collide (new isn't a valid integer), but it's still good practice to keep static paths like new/ distinct and readable.

3. Templates — Django's naming convention for generic views

Each generic view looks for a default template unless you override template_name, following this pattern:

<app>/<model>_<viewtype>.html
PostCreateView / PostUpdateView → blog/post_form.html (both share the same default template name since they're both form-based)
PostDeleteView → blog/post_confirm_delete.html
PostDetailView → blog/post_detail.html

post_form.html (used by both create and update):

html
{% extends "blog/base.html" %}
{% block content %}
<div class="content-section">
  <form method="POST">
    {% csrf_token %}
    <fieldset class="form-group">
      <legend class="border-bottom mb-4">Blog Post</legend>
      {{ form.as_p }}
    </fieldset>
    <div class="form-group">
      <button class="btn btn-outline-info" type="submit">Post</button>
    </div>
  </form>
</div>
{% endblock content %}

post_confirm_delete.html:

html
{% extends "blog/base.html" %}
{% block content %}
<div class="content-section">
  <form method="POST">
    {% csrf_token %}
    <fieldset class="form-group">
      <legend class="border-bottom mb-4">Delete Post</legend>
      <h2>Are you sure you want to delete the post "{{ object.title }}"?</h2>
    </fieldset>
    <button class="btn btn-outline-danger" type="submit">Yes, Delete</button>
    <a class="btn btn-outline-secondary" href="{% url 'post-detail' object.pk %}">Cancel</a>
  </form>
</div>
{% endblock content %}

object is the default context variable name DetailView/DeleteView/UpdateView provide automatically for the single model instance in question (same object you'd get from context_object_name if you set one explicitly).

4. Linking to Create/Update/Delete from templates

In post_detail.html, typically only shown if the logged-in user is the post's author:

html
{% if object.author == user %}
  <div>
    <a class="btn btn-secondary btn-sm mt-1 mb-1" href="{% url 'post-update' object.id %}">Update</a>
    <a class="btn btn-danger btn-sm mt-1 mb-1" href="{% url 'post-delete' object.id %}">Delete</a>
  </div>
{% endif %}

In base.html navbar, a link to create a new post for authenticated users:

html
<a class="nav-item nav-link" href="{% url 'post-create' %}">New Post</a>
5. The Post model — for reference (fields these views expect)
python
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

get_absolute_url() is worth calling out — CreateView and UpdateView redirect here by default after a successful save if you don't set success_url explicitly. Without this method defined, saving a post would raise an error (No URL to redirect to).'''