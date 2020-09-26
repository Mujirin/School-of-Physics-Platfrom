## Users Profile
### Creating users profile view
Create user profile view that currently just have a register view *users/views.py*

	from django.shortcuts import render, redirect
	from django.contrib import messages
	from .forms import UserRegisterForm

	def register(request):
		if request.method == 'POST':
			form = UserRegisterForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data.get('username')
				# Flash message
				messages.success(request, f'Your account has been created! You are now able to log in')
				return redirect('login')
		else:
			form = UserRegisterForm()
		return render(request, 'users/register.html', {'form': form})


	*def profile(request):*
		*return render(request, 'users/profile.html')*

### Creating profile template
Create file the *users/templates/profile.html*, and add the following code

	{% extends "users/base.html" %}
	{% load crispy_forms_tags %}
	{% block content %}
		<h1>{{ user.username }}</h1>
	{% endblock content %}

*Notes*: user in this template is not something that used to be passed in the view (profile view), because it is inherently add by django.


### Creating the profile route
Create the route for this profile view in the project urls
*sopp/urls.py*. This route that can be access to the user that have been login.

	from django.contrib import admin
	from django.contrib.auth import views as auth_views
	from django.urls import path, include
	from users import views as user_view

	admin.site.site_header = 'CallLawyer Administrator Page'
	admin.site.site_title = 'CallLawyer site admin'

	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('register/', user_view.register, name='register'),
	    *path('profile/', user_view.profile, name='profile'),*
	    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
	    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
	    path('', include('blog.urls')),
	]

And add this link to the navigation bar, in the *base.html*

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
		        		<a class="nav-item nav-link" href="*{% url 'profile' %}*">Profile</a>
		        		<a class="nav-item nav-link" href="{% url 'logout' %}">Logout</a>
		        	{% else %}
			          	<a class="nav-item nav-link" href="{% url 'login' %}">Login</a>
			          	<a class="nav-item nav-link" href="{% url 'register' %}">Register</a>
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

and see if this working in the browser by go to the route
	
	profile/

But we have a problem here that if we are logout, then nothing prevents us to go the profile page (even if there no username there). To make that access to this profile page that user should login first,

### Adding this profile route to the *sopp/settings.py*
So that after login we will get to this profile

	"""
	Django settings for sopp project.

	Generated by 'django-admin startproject' using Django 3.1.

	For more information on this file, see
	https://docs.djangoproject.com/en/3.1/topics/settings/

	For the full list of settings and their values, see
	https://docs.djangoproject.com/en/3.1/ref/settings/
	"""
	from setingan_rahasia import *
	from pathlib import Path

	# Build paths inside the project like this: BASE_DIR / 'subdir'.
	BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


	# Quick-start development settings - unsuitable for production
	# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

	# SECURITY WARNING: keep the secret key used in production secret!


	# SECURITY WARNING: don't run with debug turned on in production!
	DEBUG = True

	ALLOWED_HOSTS = []


	# Application definition

	INSTALLED_APPS = [
	    'users.apps.UsersConfig',
	    'crispy_forms',
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	]

	MIDDLEWARE = [
	    'django.middleware.security.SecurityMiddleware',
	    'django.contrib.sessions.middleware.SessionMiddleware',
	    'django.middleware.common.CommonMiddleware',
	    'django.middleware.csrf.CsrfViewMiddleware',
	    'django.contrib.auth.middleware.AuthenticationMiddleware',
	    'django.contrib.messages.middleware.MessageMiddleware',
	    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	]

	ROOT_URLCONF = 'sopp.urls'

	TEMPLATES = [
	    {
	        'BACKEND': 'django.template.backends.django.DjangoTemplates',
	        'DIRS': [],
	        'APP_DIRS': True,
	        'OPTIONS': {
	            'context_processors': [
	                'django.template.context_processors.debug',
	                'django.template.context_processors.request',
	                'django.contrib.auth.context_processors.auth',
	                'django.contrib.messages.context_processors.messages',
	            ],
	        },
	    },
	]

	WSGI_APPLICATION = 'sopp.wsgi.application'


	# Database
	# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.sqlite3',
	        'NAME': BASE_DIR / 'db.sqlite3',
	    }
	}


	# Password validation
	# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

	AUTH_PASSWORD_VALIDATORS = [
	    {
	        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	    },
	    {
	        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	    },
	    {
	        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	    },
	    {
	        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	    },
	]


	# Internationalization
	# https://docs.djangoproject.com/en/3.1/topics/i18n/

	LANGUAGE_CODE = 'en-us'

	TIME_ZONE = 'UTC'

	USE_I18N = True

	USE_L10N = True

	USE_TZ = True


	# Static files (CSS, JavaScript, Images)
	# https://docs.djangoproject.com/en/3.1/howto/static-files/

	STATIC_URL = '/static/'

	CRISPY_TEMPLATE_PACK = 'bootstrap4'

	*LOGIN_REDIRECT_URL = 'profile'*


### Restrict the profile route/view to the logged in only
By adding *@login_required* decorator to the profile view *users/views.py*.

	from django.shortcuts import render, redirect
	from django.contrib import messages
	*from django.contrib.auth.decorators import login_required*
	from .forms import UserRegisterForm

	def register(request):
		if request.method == 'POST':
			form = UserRegisterForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data.get('username')
				# Flash message
				messages.success(request, f'Your account has been created! You are now able to log in')
				return redirect('login')
		else:
			form = UserRegisterForm()
		return render(request, 'users/register.html', {'form': form})


	*@login_required*
	def profile(request):
		return render(request, 'users/profile.html')

### Directing unlogin users to login page
By this state, if you go to the 
	
	http://localhost:8000/profile/

route in the browser without login, you will some error that telling us that the page we are looking doesn’t exist. It looking for http://localhost:8000/accounts/login/?next=/profile/ this is default setting by django. So we change this in the settings.py, at the bottom of this file

	"""
	Django settings for sopp project.

	Generated by 'django-admin startproject' using Django 3.1.

	For more information on this file, see
	https://docs.djangoproject.com/en/3.1/topics/settings/

	For the full list of settings and their values, see
	https://docs.djangoproject.com/en/3.1/ref/settings/
	"""
	from setingan_rahasia import *
	from pathlib import Path

	# Build paths inside the project like this: BASE_DIR / 'subdir'.
	BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


	# Quick-start development settings - unsuitable for production
	# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

	# SECURITY WARNING: keep the secret key used in production secret!


	# SECURITY WARNING: don't run with debug turned on in production!
	DEBUG = True

	ALLOWED_HOSTS = []


	# Application definition

	INSTALLED_APPS = [
	    'users.apps.UsersConfig',
	    'crispy_forms',
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	]

	MIDDLEWARE = [
	    'django.middleware.security.SecurityMiddleware',
	    'django.contrib.sessions.middleware.SessionMiddleware',
	    'django.middleware.common.CommonMiddleware',
	    'django.middleware.csrf.CsrfViewMiddleware',
	    'django.contrib.auth.middleware.AuthenticationMiddleware',
	    'django.contrib.messages.middleware.MessageMiddleware',
	    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	]

	ROOT_URLCONF = 'sopp.urls'

	TEMPLATES = [
	    {
	        'BACKEND': 'django.template.backends.django.DjangoTemplates',
	        'DIRS': [],
	        'APP_DIRS': True,
	        'OPTIONS': {
	            'context_processors': [
	                'django.template.context_processors.debug',
	                'django.template.context_processors.request',
	                'django.contrib.auth.context_processors.auth',
	                'django.contrib.messages.context_processors.messages',
	            ],
	        },
	    },
	]

	WSGI_APPLICATION = 'sopp.wsgi.application'


	# Database
	# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.sqlite3',
	        'NAME': BASE_DIR / 'db.sqlite3',
	    }
	}


	# Password validation
	# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

	AUTH_PASSWORD_VALIDATORS = [
	    {
	        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	    },
	    {
	        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	    },
	    {
	        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	    },
	    {
	        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	    },
	]


	# Internationalization
	# https://docs.djangoproject.com/en/3.1/topics/i18n/

	LANGUAGE_CODE = 'en-us'

	TIME_ZONE = 'UTC'

	USE_I18N = True

	USE_L10N = True

	USE_TZ = True


	# Static files (CSS, JavaScript, Images)
	# https://docs.djangoproject.com/en/3.1/howto/static-files/

	STATIC_URL = '/static/'

	CRISPY_TEMPLATE_PACK = 'bootstrap4'

	LOGIN_REDIRECT_URL = 'profile'

	*LOGIN_URL = 'login'*

By this state, if users without login go to 
	
	http://localhost:8000/profile/

So if you go to the route profile/ without logged in user, now you redirected to the login page with the nice next url built by django to the profile page after you login. This keeping tract the route you trying to, So after you login, you will redirected to the profile page. By this stage, the profile page only accessible for logged in user.



