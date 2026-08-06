'''The first step to create an app using the command python manage.py startapp user

The first step after creating a user app is to register in the settings, by adding the string 'user.apps.UserConfig' in the installed apps list in the settings.py folder

The next step is to create a views in the user apps, using the code in the views.py file:
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form':form})
        
To show the webpage in the website we create templates folder in the user apps and inside templates we create user and inside that we create register.html 

Inside the register.html we use the following code:
{% extends "blog/base.html" %}
{% block content %}
<div class="content_section">
    <form meathod="POST">
        {% csrf_token %}
        <fieldset class="form-group">
            <legend class="border-bottom mb-4">
                Register Today in My Blog Website !
            </legend>
            {{ form.as_p }}
        </fieldset>
        <div class="form-groups">
            <button class="btn btn-outline-info" type="subumit">Sign up</button>
        </div>
    </form>
    <div class="border-top pt-3">
        <small class="text-muted">
            Already have an account ? <a class="ml-2" href="#">Sign in</a>
        </small>
    </div>
</div>
{% endblock content %}

and to register as a url, open the urls.py from project section by these meathods:
first, add from users import views as user_views
path('register/', user_views.register, name='register'),

now to display them in the webpage we need to add :
      {% if messages %}
      {% for message in messages %}
      <div class="alert alert-{{message.tags}}">
        {{ message }}
      </div>
      {% endfor %}
      {% endif %}
      {% block content %}{% endblock %}
This code block above the content block in order to access every alerts in the registration page to the webpage.

Till now we have only recreated forms to register, but these are not getting stored in the databases,  

To save the data if the user is valid add form.save() just below the form.is_valid, '''