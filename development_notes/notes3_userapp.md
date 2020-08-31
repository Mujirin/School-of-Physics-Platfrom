## Aplikasi Users
	$ python manage.py startapp users
### Tambahkan users config pada setting
Buka settings.py dan tambahkan 'users.apps.UsersConfig' di daftar INSTALLED_APP

	INSTALLED_APPS = [
	    'users.apps.UsersConfig',
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	]

### User Registration
#### Create users view
in users/views.py adding the following code so that it become

	from django.shortcuts import render

	from django.shortcuts import render
	from django.contrib.auth.forms import UserCreationForm

	def register(request):
		form = UserCreationForm()
		return render(request, 'users/register.html', {'form': form})

#### Adding url mapping in project urls
Add the following code to the *sopp/urls.py*

	from django.contrib import admin
	from django.urls import path, include
	from users import views as user_view


	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('register/', user_view.register, name='register'),
	]

#### Creating base templates
Make a template dir and the app name (users/templates/users), and fill it with *base.html*, 
	$ touch users/templates/users/base.html
the path become *users/templates/blog/base.html*

	{% load static %}
	<!DOCTYPE html>
	<html>
	<head>
		<!-- Required meta tags -->
	    <meta charset="utf-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	    <!-- Bootstrap CSS -->
	    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

	    <link rel="stylesheet" type="text/css" href="{% static 'users/main.css' %}">

		{% if title %}
			<title>School of Physics - {{ title }}</title>
		{% else %}
			<title>School of Physics</title>
		{% endif %}
	</head>
	<body>
		<header class="site-header">
		  <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
		    <div class="container">
		      <a class="navbar-brand mr-4" href="#">School of Physics</a>
		      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
		      <span class="navbar-toggler-icon"></span>
		      </button>
		      <div class="collapse navbar-collapse" id="navbarToggle">
		        <div class="navbar-nav mr-auto">
		          <a class="nav-item nav-link" href="#">Home</a>
		          <a class="nav-item nav-link" href="#">About</a>
		        </div>
		        <!-- Navbar Right Side -->
		        <div class="navbar-nav">
		        	{% if user.is_authenticated %}
		        		<a class="nav-item nav-link" href="#">New Post</a>
		        		<a class="nav-item nav-link" href="#">Profile</a>
		        		<a class="nav-item nav-link" href="#">Logout</a>
		        	{% else %}
			          	<a class="nav-item nav-link" href="#">Login</a>
			          	<a class="nav-item nav-link" href="#">Register</a>
			        {% endif %}
		        </div>
		      </div>
		    </div>
		  </nav>
		</header>
		<main role="main" class="container">
		  <div class="row">
		    <div class="col-md-4">
		      <div class="content-section">
		        <h3>Our Sidebar</h3>
		        <p class='text-muted'>You can put any information here you'd like.
		          <ul class="list-group">
		            <li class="list-group-item list-group-item-light">Latest Posts</li>
		            <li class="list-group-item list-group-item-light">Announcements</li>
		            <li class="list-group-item list-group-item-light">Calendars</li>
		            <li class="list-group-item list-group-item-light">etc</li>
		          </ul>
		        </p>
		      </div>
		    </div>
		  </div>
		</main>
		
		<!-- Optional JavaScript -->
	    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
	    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
	    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
	    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

	</body>
	</html>


#### Creating registration template
In *users/templates/users/* Make a directory *templates* in users dir and create *users* dir in it and in it create *register.html*, 
	$ touch users/templates/users/register.html
add the following code

	{% extends "users/base.html" %}
	{% load crispy_forms_tags %}

	{% block page_name %}
		<a style="font-size: 13px;" class="navbar-brand mr-4" href=""><span>&laquo;</span>&nbsp&nbsp&nbsp&nbsp {{page_name}}</a>
	{% endblock %}

	{% block content %}
		<div class="content-section">
			<form method="POST">
				{% csrf_token %}
				<fieldset class="form-group">
					{{ form|crispy }}
				</fieldset>
				<div class="form-group">
					<button class="btn btn-outline-info" type="submit">Sign Up</button>
				</div>
			</form>
			<div class="border-top pt-3">
				<small class="text-muted">
					Sudah memilik Akun? <a class="ml-2" href="">Sign In</a>
				</small>
			</div>
		</div>
	{% endblock content %}

#### Adding flash message
##### Adding flash messege in the view
In this stage the form just direct to the same page, so to improve, edit the *users/view.py* and adding flash messages as below

	from django.shortcuts import render, redirect
	from django.contrib.auth.forms import UserCreationForm
	from django.contrib import messages

	def register(request):
		if request.method == 'POST':
			form = UserCreationForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data.get('username')
				# Flash message
				messages.success(request, f'Account created for {username}')
				# return redirect('blog-home')
				return render(request, 'users/register.html', {'form': form})
		else:
			form = UserCreationForm()
		return render(request, 'users/register.html', {'form': form})

##### Adding flash messege in the base template
By adding flash message to the base template, every message will display in every template.

	{% load static %}
	<!DOCTYPE html>
	<html>
	<head>
		<!-- Required meta tags -->
	    <meta charset="utf-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	    <!-- Bootstrap CSS -->
	    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

	    <link rel="stylesheet" type="text/css" href="{% static 'users/main.css' %}">

		{% if title %}
			<title>School of Physics - {{ title }}</title>
		{% else %}
			<title>School of Physics</title>
		{% endif %}
	</head>
	<body>
		<header class="site-header">
		  <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
		    <div class="container">
		      <a class="navbar-brand mr-4" href="#">School of Physics</a>
		      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
		      <span class="navbar-toggler-icon"></span>
		      </button>
		      <div class="collapse navbar-collapse" id="navbarToggle">
		        <div class="navbar-nav mr-auto">
		          <a class="nav-item nav-link" href="#">Home</a>
		          <a class="nav-item nav-link" href="#">About</a>
		        </div>
		        <!-- Navbar Right Side -->
		        <div class="navbar-nav">
		        	{% if user.is_authenticated %}
		        		<a class="nav-item nav-link" href="#">New Post</a>
		        		<a class="nav-item nav-link" href="#">Profile</a>
		        		<a class="nav-item nav-link" href="#">Logout</a>
		        	{% else %}
			          	<a class="nav-item nav-link" href="#">Login</a>
			          	<a class="nav-item nav-link" href="#">Register</a>
			        {% endif %}
		        </div>
		      </div>
		    </div>
		  </nav>
		</header>
		<main role="main" class="container">
		  <div class="row">
		    <div class="col-md-8">
		    	<!-- Flash Message -->
		    	{% if messages %}
		    		{% for message in messages %}
		    			<div class="alert alert-{{ message.tags }}">
		    				{{ message }}
		    			</div>
		    		{% endfor %}
		    	{% endif %}
		    	{% block content %}{% endblock %}
		    </div>
		    <div class="col-md-4">
		      <div class="content-section">
		        <h3>Our Sidebar</h3>
		        <p class='text-muted'>You can put any information here you'd like.
		          <ul class="list-group">
		            <li class="list-group-item list-group-item-light">Latest Posts</li>
		            <li class="list-group-item list-group-item-light">Announcements</li>
		            <li class="list-group-item list-group-item-light">Calendars</li>
		            <li class="list-group-item list-group-item-light">etc</li>
		          </ul>
		        </p>
		      </div>
		    </div>
		  </div>
		</main>
		
		<!-- Optional JavaScript -->
	    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
	    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
	    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
	    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

	</body>
	</html>

If you run the development server by

	$ python manage.py runserver

and go to *http://localhost:8000/register/* you will see the flash message about creation, but still in the same page.

### Saving the new user that has been created using usercreation form
Add form.save in the *users/view.py*

	from django.shortcuts import render, redirect
	from django.contrib.auth.forms import UserCreationForm
	from django.contrib import messages

	def register(request):
		if request.method == 'POST':
			form = UserCreationForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data.get('username')
				# Flash message
				messages.success(request, f'Account created for {username}')
				# return redirect('blog-home')
				return render(request, 'users/register.html', {'form': form})
		else:
			form = UserCreationForm()
		return render(request, 'users/register.html', {'form': form})

Then try close the development server, and run again, then create a new user in register page and klick “Sign Up” in the browser, and then see at admin page *http://localhost:8000/admin/auth/user/*, you will see that the new user had been created and saved there.








