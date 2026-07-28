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

We can create a base.html in the blog folder with the other html files, and now we can add the syntax which are common in both about and home html files

To like all three files we need to add {% extends "blog/base.html" %}

and for the things which are not common in them we need to create a {% block content %} and end with {% endblock %}, we need to add this in both from where we want to show out output and from where we want to take the input

go to https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template to get the bootstrap started template, copy everything from the head section of the website and paste it in the head section of the base.html, do the same with the scripts also.

put the blog content inside a div tag and give it a class

go to the https://github.com/CoreyMSchafer/code_snippets/blob/master/Django_Blog/snippets/navigation.html snipits folder and get the navigation.html code(it contians the code for the navigation bar) and add that code in the top of the body tag

now we can remove the {% block content %} from the base.html file as we will copy and paste the main.html code from the https://github.com/CoreyMSchafer/code_snippets/blob/master/Django_Blog/snippets/main.html this snippit contains the block content that's why we need to remove it. 

Now in the runapps folder create a new file name static and inside that folder create a folder name  blog and inside blog create a css file name, main.css 

copy the code from the https://github.com/CoreyMSchafer/code_snippets/blob/master/Django_Blog/snippets/main.css snippit and paste it in the main.css folder 

Now to load the static folder in the base.html folder write {% load static%} and in the head add <link rel="stylesheet" type="text/css" href="{% static 'blog/main.css' %}" to link the css file with the base.html 

and now run the server, if its already running refresh the page, if still it does not shows it restart the server

copy code from https://github.com/CoreyMSchafer/code_snippets/blob/master/Django_Blog/snippets/article.html and add it in the home.html inside the current for loop replacing the old h1 tags 

In the base templates of the nativigation bar, we have hard coded the bars to replace it replace it with {% url 'blog-home' %} and {% url 'blog-about' %}, this is a good coading practice. '''