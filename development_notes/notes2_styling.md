## Improve styling with Crispy Form
This notes is to improve styling in the template. 
### Installing crispy from (in virtual env)
	$ pip install django-crispy-forms
### Adding the crispy form to the setting
In settings.py add the following in bold in INSTALLED_APPS settings.py

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

### Adding static url
And in the bottom of this setting.py file settings.py

	CRISPY_TEMPLATE_PACK = 'bootstrap4'

This style will soon you see in the next development.

