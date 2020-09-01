
## Change the admin page title and etc.
In the *sopp/urls.py* adding the following code to overwrite the django stuff

	from django.contrib import admin
	from django.urls import path, include
	from users import views as user_view

	*admin.site.site_header = 'School of Physics'	# default: "Django Administration"*
	*admin.site.index_title = 'Site Administration'  # default: "Site administration"*
	*admin.site.site_title = 'SoP Site Admin'		# default: "Django site admin"*

	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('register/', user_view.register, name='register'),
	]

Then restart the development server and see the admin page.
Source: https://stackoverflow.com/questions/4938491/django-admin-change-header-django-administration-text

