## Login and logout system
### Creating url app for the login and logout, with the class based view
Add the following code to the *sopp/urls.py*

	from django.contrib import admin
	*from django.contrib.auth import views as auth_views*
	from django.urls import path, include
	from users import views as user_view

	admin.site.site_header = 'School of Physics Administration'	# default: "Django Administration"
	admin.site.index_title = 'Site Administration'  			# default: "Site administration"
	admin.site.site_title = 'SoP Site Admin'					# default: "Django site admin" 
	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('register/', user_view.register, name='register'),
	    *path('login/', auth_views.LoginView.as_view(), name='login'),*
	    *path('logout/', auth_views.LogoutView.as_view(), name='logout'),*
	]

Go to the development server and make sure do not have an error there, and go to the route login in the browser, you will see an error because template does not exist yet. And the errors says it look the registration dir and login.html on it. 

	Exception Type:	TemplateDoesNotExist
	Exception Value:	registration/login.html

But we would not make a registration dir and fill it with login.html here. And we will make login.html template inside the users directory app, and tell the django where it is with passing the parameter template_name in the as_view function in the urls mapp above.

	from django.contrib import admin
	*from django.contrib.auth import views as auth_views*
	from django.urls import path, include
	from users import views as user_view

	admin.site.site_header = 'School of Physics Administration'	# default: "Django Administration"
	admin.site.index_title = 'Site Administration'  			# default: "Site administration"
	admin.site.site_title = 'SoP Site Admin'					# default: "Django site admin" 

	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('register/', user_view.register, name='register'),
	    *path('login/', auth_views.LoginView.as_view(*template_name='users/login.html'*), name='login'),*
	    *path('logout/', auth_views.LogoutView.as_view(*template_name='users/logout.html'*), name='logout'),*
	]

With these changes the error now say
Exception Type:	TemplateDoesNotExist
Exception Value:	users/login.html
and then 

### Make files login.html and logout.html template in user templates
this templates same as the register.html template with the difference in the *italic* lines.
#### Login template
*users/templates/users/login.py*

	{% extends "users/base.html" %}
	{% load crispy_forms_tags %}
	{% block content %}
		<div class="content-section">
			<form method="POST">
				{% csrf_token %}
				<fieldset class="form-group">
					<legend class="border-bottom mb-4">
						Log In
					</legend>
					{{ form|crispy }}
				</fieldset>
				<div class="form-group">
					<button class="btn btn-outline-info" type="submit">Login</button>
				</div>
			</form>
			<div class="border-top pt-3">
				<small class="text-muted">
					Need An Account? <a class="ml-2" href="{% url 'register' %}">Sign Up Now</a>
				</small>
			</div>
		</div>
	{% endblock content %}
#### Add login link to the Register template
And don’t forget add the login link to the register.html template because now we have that route. See the blog line below:

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
					Sudah memilik Akun? <a class="ml-2" href="*{% url 'login' %}*">Sign In</a>
				</small>
			</div>
		</div>
	{% endblock content %}

#### Add login direct url
If you check the rout login/ in the browser, some functionality have been work there such as if the username  and the password do not exist or match than the form tell us the error. But if we enter the correct username and password it redirect to the profile page that did not exist yet. This redirect route is by default set by django, to change this go tho the *sopp/settings.py* and add the following in bold in the bottom.

	STATIC_URL = '/static/'

	CRISPY_TEMPLATE_PACK = 'bootstrap4'

	*LOGIN_REDIRECT_URL = 'home-page'*

#### Adding redirec login to the register
so if we login again with the correct username and password in the browser we will go to the home page.
If you login with the user that have access tho the admin page, if you go to the admin page, you have already login there.
If you login with user that have not access to the admin page, if you go to the admin page, you forced to the  administration login page.
So the login page is represent two login that is login in general and admin login page, if you are the user that have access to the admin page.

In the registration view, change the following in bold to improve the logic message, and the redirected to the login page. *users/views.py*
	from django.shortcuts import render, redirect
	from django.contrib import messages
	from .forms import UserRegistrationForm

	def register(request):
		if request.method == 'POST':
			form = UserRegistrationForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data.get('username')
				# Flash message
				messages.success(request, f'Your account has been created! You are now able to log in')
				return redirect('login')
		else:
			form = UserRegistrationForm()
		return render(request, 'users/register.html', {'form': form})


#### Logout template
And in the project urls if we remove the template_name params, *django_project/urls.py*
	
	from django.contrib import admin
	from django.urls import path, include
	from users import views as user_view
	from django.contrib.auth import views as auth_views


	admin.site.site_header = 'School of Physics Administration'	# default: "Django Administration"
	admin.site.index_title = 'Site Administration'  			# default: "Site administration"
	admin.site.site_title = 'SoP Site Admin'					# default: "Django site admin" 

	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('register/', user_view.register, name='register'),
	    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
	    *path('logout/', auth_views.LogoutView.as_view(), name='logout'),*
	]


If we check in the browser and go to the route logout/, after this changes, and you will redirect to the page

	Django administration
	Home
	Logged out
	Thanks for spending some quality time with the Web site today.
	Log in again

It wired because it is django administration authentication, and if we click log in again above we redirected to the admin login page. 
This not we want, we want the authentication system that work for everyone users that do not posses to the admin system.
So back in the project *django_project/urls.py*

	from django.contrib import admin
	from django.contrib.auth import views as auth_views
	from django.urls import path, include
	from users import views as user_view

	admin.site.site_header = 'CallLawyer Administrator Page'
	admin.site.site_title = 'CallLawyer site admin'

	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('register/', user_view.register, name='register'),
	    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
	    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
	]

So that this logout route looking for users logout template.

In users logout templates add the following code *users/templates/users/logout.html*

	{% extends "users/base.html" %}
	{% load crispy_forms_tags %}

	{% block page_name %}
		<a style="font-size: 13px;" class="navbar-brand mr-4" href=""><span>&laquo;</span>&nbsp&nbsp&nbsp&nbsp {{page_name}}</a>
	{% endblock %}

	{% block content %}
		<h2>You have been logged out</h2>
		<div class="border-top pt-3">
			<small class="text-muted">
				<a href="{% url 'login' %}">Log In Again</a>
			</small>
		</div>
	{% endblock content %}

And then try to login and logout with user without and with admin pages, if the user is with admin access if it logout or login it automatically login and logout the admin page.
*Notes:*
By this time we don't have home page yet so after login you will see an error, but it doesn't matter we will get there.

#### Improve navigation route
Open *base.html* template in users apps and add the following in blod to also check if the user is logged in or not useing user.is_authenticated, if its authenticated/already login then show the logout navigation, else show login and register route.

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
		        		<a class="nav-item nav-link" href="*{% url 'logout' %}*">Logout</a>
		        	{% else %}
			          	<a class="nav-item nav-link" href="*{% url 'login' %}*">Login</a>
			          	<a class="nav-item nav-link" href="*{% url 'register' %}*">Register</a>
			        {% endif %}
		        </div>
		      </div>
		    </div>
		  </nav>
		</header>
		<main role="main" class="container">
		  <div class="row">
		  	<!-- Flash Message -->
		    <div class="col-md-8">
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

See in the browser the changes, try click in the menu the login and logout, or register.



*Other notes:*
sopp URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
1. Add an import:  from my_app import views
2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views
1. Add an import:  from other_app.views import Home
2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf
1. Import the include() function: from django.urls import include, path
2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))


	



