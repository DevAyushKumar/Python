'''Django Tutorial Part 12: Password Reset System & Email ConfigurationThis lecture covers setting up Django’s built-in authentication views to handle forgotten passwords. It covers configuring password reset URL patterns, building the four required HTML templates, setting up Gmail SMTP for sending real emails, and adding a reset link to the login page.  1. URL Routing for Password Reset ViewsDjango provides built-in class-based views for the entire password reset workflow. Import django.contrib.auth.views in your main urls.py.  django_project/urls.pyPythonfrom django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    
    # Password Reset Routes
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
         
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
         
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
         
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('', include('blog.urls')),
]
2. Password Reset TemplatesThe password reset workflow requires 4 dedicated templates inside the users/templates/users/ folder.Step A: Form to Request Reset Emailusers/templates/users/password_reset.htmlHTML{% extends "blog/base.html" %}
{% load crispy_forms_tags %}
{% block content %}
    <div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Reset Password</legend>
                {{ form|crispy }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Request Password Reset</button>
            </div>
        </form>
    </div>
{% endblock content %}
Step B: Email Sent Confirmation Noticeusers/templates/users/password_reset_done.htmlHTML{% extends "blog/base.html" %}
{% block content %}
    <div class="alert alert-info">
        An email has been sent with instructions to reset your password.
    </div>
{% endblock content %}
Step C: New Password Entry Formusers/templates/users/password_reset_confirm.htmlHTML{% extends "blog/base.html" %}
{% load crispy_forms_tags %}
{% block content %}
    <div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Reset Password</legend>
                {{ form|crispy }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Reset Password</button>
            </div>
        </form>
    </div>
{% endblock content %}
Step D: Password Reset Complete Success Pageusers/templates/users/password_reset_complete.htmlHTML{% extends "blog/base.html" %}
{% block content %}
    <div class="alert alert-info">
        Your password has been reset.
    </div>
    <a href="{% url 'login' %}">Sign In Here</a>
{% endblock content %}
3. Email Settings ConfigurationTo send real emails (e.g., using Gmail SMTP), update settings.py. Credentials should be loaded securely from environment variables rather than hardcoded.  django_project/settings.pyPythonimport os

# SMTP Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
Note: For Gmail, EMAIL_PASS requires a 16-character App Password generated via Google Account Security settings (with 2-Factor Authentication enabled), not your personal Gmail login password.4. Add "Forgot Password?" Link on Login PageUpdate your login template to give users direct access to the reset form.users/templates/users/login.htmlHTML{% extends "blog/base.html" %}
{% load crispy_forms_tags %}
{% block content %}
    <div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Log In</legend>
                {{ form|crispy }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Login</button>
                <small class="text-muted ml-2">
                    <a href="{% url 'password_reset' %}">Forgot Password?</a>
                </small>
            </div>
        </form>
        <div class="border-top pt-3">
            <small class="text-muted">
                Need An Account? <a class="ml-2" href="{% url 'register' %}">Sign Up Now</a>
            </small>
        </div>
    </div>
{% endblock content %}'''