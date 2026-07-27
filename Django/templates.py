'''to start with templates we need to create a templates folder inside the runapp folder and inside folder we need to create a folder say blog folder.
Inside the blog folder we need to add the html files of home and about section.
we can use these html files to design the structure of the webpage

From the runapps, apps.py copy the class name and open the project settings.py file and to the installed apps sections add it using a string like:
'blog.apps.(class_name)' 

Since we are using html templates to get response we need to change view section of apps also. 
Of the homepage change the return value to the return render(request, 'name_of_the_file/name_of_the_html_file') change both the views in order to connect it with the html webpage.

In the app section in view.py, create a list for the posts and inside the lists use dictionary to write the data in key value pairs.

After that add the name of the list in the def, in whichever function you want to show.

After that in the html files write the codes to show the output in the webpage.
{post in posts %}
<h1> {{ post.Title}} </h1>
<p>by {{post.Author}} on {{post.Date_posted}} </p>
<p> {{post.Content}} </p>
{% end for %}
This is used to code in the html file to show the user data.

'''