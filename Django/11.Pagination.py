'''Django Tutorial Part 11: Pagination & User Post FilteringThis lecture covers implementing pagination for blog posts using Django’s built-in Paginator class, adding pagination to class-based views, updating template navigation controls, and creating a dedicated filtered view for posts written by a specific user.  1. Django Shell Pagination BasicsBefore updating views, you can experiment with pagination directly in the Django shell:Bashpython manage.py shell
Pythonfrom django.core.paginator import Paginator
from blog.models import Post

# Fetch all posts
posts = Post.objects.all()

# Paginate 2 items per page
p = Paginator(posts, 2)

# Information methods
print(p.num_pages)      # Total number of pages
print(p.count)          # Total number of items

# Get a specific page
p1 = p.page(1)
print(p1.object_list)   # Items on page 1
print(p1.has_previous())# False
print(p1.has_next())    # True
print(p1.next_page_number()) # 2
2. Adding Pagination to PostListViewTo paginate a Class-Based View, add the paginate_by attribute to your ListView.blog/views.pyPythonfrom django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5  # Limits posts to 5 per page
3. Pagination Controls Template SetupWhen paginate_by is set, Django automatically passes is_paginated and page_obj to the template.blog/templates/blog/home.htmlHTML{% extends "blog/base.html" %}
{% block content %}
    {% for post in posts %}
        <article class="media content-section">
          <img class="rounded-circle article-img" src="{{ post.author.profile.image.url }}">
          <div class="media-body">
            <div class="article-metadata">
              <a class="mr-2" href="{% url 'user-posts' post.author.username %}">{{ post.author }}</a>
              <small class="text-muted">{{ post.date_posted|date:"F d, Y" }}</small>
            </div>
            <h2><a class="article-title" href="{% url 'post-detail' post.id %}">{{ post.title }}</a></h2>
            <p class="article-content">{{ post.content }}</p>
          </div>
        </article>
    {% endfor %}

    <!-- Pagination Navigation -->
    {% if is_paginated %}

      {% if page_obj.has_previous %}
        <a class="btn btn-outline-info mb-4" href="?page=1">First</a>
        <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.previous_page_number }}">Previous</a>
      {% endif %}

      {% for num in page_obj.paginator.page_range %}
        {% if page_obj.number == num %}
          <a class="btn btn-info mb-4" href="?page={{ num }}">{{ num }}</a>
        {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
          <a class="btn btn-outline-info mb-4" href="?page={{ num }}">{{ num }}</a>
        {% endif %}
      {% endfor %}

      {% if page_obj.has_next %}
        <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.next_page_number }}">Next</a>
        <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.paginator.num_pages }}">Last</a>
      {% endif %}

    {% endif %}
{% endblock content %}
4. User Post List ViewTo create a page showing only posts published by a specific user:  Update blog/views.pyPythonclass UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
Create blog/templates/blog/user_posts.htmlHTML{% extends "blog/base.html" %}
{% block content %}
    <h1 class="mb-3">Posts by {{ view.kwargs.username }} ({{ page_obj.paginator.count }})</h1>
    {% for post in posts %}
        <article class="media content-section">
          <img class="rounded-circle article-img" src="{{ post.author.profile.image.url }}">
          <div class="media-body">
            <div class="article-metadata">
              <a class="mr-2" href="{% url 'user-posts' post.author.username %}">{{ post.author }}</a>
              <small class="text-muted">{{ post.date_posted|date:"F d, Y" }}</small>
            </div>
            <h2><a class="article-title" href="{% url 'post-detail' post.id %}">{{ post.title }}</a></h2>
            <p class="article-content">{{ post.content }}</p>
          </div>
        </article>
    {% endfor %}

    <!-- Pagination Controls -->
    {% if is_paginated %}
      {% if page_obj.has_previous %}
        <a class="btn btn-outline-info mb-4" href="?page=1">First</a>
        <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.previous_page_number }}">Previous</a>
      {% endif %}

      {% for num in page_obj.paginator.page_range %}
        {% if page_obj.number == num %}
          <a class="btn btn-info mb-4" href="?page={{ num }}">{{ num }}</a>
        {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
          <a class="btn btn-outline-info mb-4" href="?page={{ num }}">{{ num }}</a>
        {% endif %}
      {% endfor %}

      {% if page_obj.has_next %}
        <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.next_page_number }}">Next</a>
        <a class="btn btn-outline-info mb-4" href="?page={{ page_obj.paginator.num_pages }}">Last</a>
      {% endif %}
    {% endif %}
{% endblock content %}
5. URL Routing SetupAdd the new path for user-specific posts:blog/urls.pyPythonfrom django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]'''