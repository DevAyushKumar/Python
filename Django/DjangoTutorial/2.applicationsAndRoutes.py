'''Now we ned to create startup app using the command python manage.py startapp name_of_the_startup

Open that new startapp directory and open the views.py files and write these code:
from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

    
create a urls.py in the startapp folder and add these codes in it:

from django.urls import path
from . import views
urlpatters = [
path('', views.home, name='name_of_the_url'),
]
in the above code we import views and path from the django library
and redirect the path to view folder of function name home, and the name of that directory will be the name of the url and in the first argument of path we need to add default view and home pasge.

Now in project section of urls we need to add include in the django.urls line, and in urls patters we need to create a new url path('', include('name_of_the_startapp')),

now we need to add this code to the startapp's view section
def about(response):
    return HttpsResonse('<h1>This is about</h1>')
    
Now we need to add one more path in the startapp urls  path('about/', views.about, name='name_of_url'),

The path which we have given in the project urls, url patters will guide us to the blog urls and we change the name of that then we also need to do the same in the website in order to access it
If we leave the name of the path empty then it will make the blog home as the default home for the local host. 
'''