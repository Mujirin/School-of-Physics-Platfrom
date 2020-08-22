## Buat applikasi Users
	$ python manage.py startapp users
### Tambahkan users config pada setting
Buka settings.py dan tambahkan 'users.apps.UsersConfig' di daftar INSTALLED_APP
	INSTALLED_APPS = [
	    ***'users.apps.UsersConfig',***
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	]
