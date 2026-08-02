'''This part wires up Django's built-in authentication views (LoginView, LogoutView) instead of writing login/logout logic from scratch — Django already ships this, so the work is mostly configuration, templates, and login-protecting other views. This connects directly to the bugs we fixed earlier in your project (the missing template_name on LogoutView, and the POST-only requirement).
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
Key points:

You don't need to write a LoginView or LogoutView yourself — Django provides fully working ones in django.contrib.auth.views. You're just pointing them at your own templates.
If you skip template_name, Django falls back to its own default template paths (registration/login.html, registration/logged_out.html) — which is exactly what caused your earlier bug where logout showed the Django admin's branded page instead of your own.

{% extends "blog/base.html" %}
{% block content %}
<div class="content-section">
  <form method="POST">
    {% csrf_token %}
    <fieldset class="form-group">
      <legend class="border-bottom mb-4">Log In</legend>
      {{ form.as_p }}
    </fieldset>
    <div class="form-group">
      <button class="btn btn-outline-info" type="submit">Login</button>
    </div>
  </form>
  <div class="border-top pt-3">
    <small class="text-muted">
      Need an account? <a href="{% url 'register' %}">Sign Up Now</a>
    </small>
  </div>
</div>
{% endblock content %}
LoginView automatically passes a form variable into the template context — you don't build this form yourself, Django's built-in AuthenticationForm handles it.

{% extends "blog/base.html" %}
{% block content %}
<h2>You have been logged out!</h2>
<div class="border-top pt-3">
    <small class="text-muted">
        Login in again <a href="{% url 'login' %}">Login In again</a>
    </small>
</div>
{% endblock content %}

LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL — where Django sends the user after a successful login (name of a URL pattern, e.g. your homepage).
LOGIN_URL — where Django sends unauthenticated users who try to access a page protected by @login_required. Without this, Django defaults to /accounts/login/, which likely doesn't exist in your project and would 404.
Any view wrapped this way redirects anonymous users to LOGIN_URL automatically, with a ?next=/profile/ query param so Django can send them back to the page they originally wanted after logging in.

{% if user.is_authenticated %}
  <a class="nav-item nav-link" href="{% url 'profile' %}">Profile</a>
  <form method="post" action="{% url 'logout' %}" class="d-inline">
    {% csrf_token %}
    <button type="submit" class="nav-item nav-link btn btn-link">Logout</button>
  </form>
{% else %}
  <a class="nav-item nav-link" href="{% url 'login' %}">Login</a>
  <a class="nav-item nav-link" href="{% url 'register' %}">Register</a>
{% endif %}
user.is_authenticated is available in every template automatically (Django's auth context processor injects user into context on every request, as long as 'django.contrib.auth.context_processors.auth' is in your TEMPLATES setting, which it is by default).

Note on the logout form/button: the original 2018 tutorial predates Django's security change (from Django 4.1 onward) requiring LogoutView to only accept POST. His original video probably just uses a plain <a href="{% url 'logout' %}">Logout</a> link, which worked fine on the Django version at the time — but on your current Django 6.0, that will 405 like you saw earlier. The form/button version above is the modern, correct approach for your setup.'''