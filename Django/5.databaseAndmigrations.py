'''In the apps find models.py file this is used to write the database without using the any sql.

write this code replacing the comment in that file:
from django.utils import timezone
from django.contrib.auth.models import User

class posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
Now in command propmt run the python manage.py makemigrations, this will provide where migrations have been created in the file and with its initials.

To check it in the sql run the command python manage.py sqlmigrate blog 0001.

And finally to confirm it use python manage.py migrate

to run the querry, use python manage.py shell

and inside the shell use the User.objects.all() to see the nummber of user and their username. 

From the terminal also we can provide the content for the database, we need to first assign the user like user = User.objects.filter(usrname='ayush').first()
This will assign the value to the user of the username ayush

Now to insert values using this post_1 = posts(title = 'blog 1', content = 'This is the first blog', author = user)
and then use post_1.save() to save the post in database
To check we can use the posts.object.all()

To show data from directly the database not the dummy model is by the following steps:
create a function __str__ in the models.py inside the same class and write
def __str__(self):
    return self.title

There is one more way to create a data using the posts
create a user from the above meathod and run these querries symaltaneously
user.post_set
user.post_set.create(title = 'blog 3', content = 'This is blog 3')

Now, we have create a set database with the details, we now need to link this with our home page in order to display it, to do so

go to views foler and add from .models import posts
and in home function change the value of context with the posts.object.all()

now run the server to check if everything is working fine. 

We can also modify the date and timings by going to the home.html folder and adding |date: F d,Y next to the date_posted

Since, we are no longer using the dummy data and directly using the database, we can remove the dummy data.

We also need to add our models in admin.py folder so we can see the posts in admin section:
from .models import posts
admin.site.register(posts)

This will show the posts in the admin section for the posts.'''