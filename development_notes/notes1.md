
## Creating Github Repository
### Cloning Repository
After creating Github repository, in somewhere of your computers
$ git clone github.com-Mujirin:Mujirin/School-of-Physics-Platfrom.git
### Commit to the repo
	$ git status
	$ git add .
	$ git status
	$ git commit -m "Initial commit."
	$ git push
## Creating project
### Virtual environment
#### Creating virtual environment
	$ mkdir SoPP
	$ cd SoPP/
	$ virtualenv sopp_env
#### Activate
	$ source sopp_env/bin/activate
### Django
#### Installing Django
	$ pip install django
#### Checking its version
	$ python -m django --version
#### Starting the project
	$ django-admin startproject sopp
	$ cd sopp
#### Running the development server
	$ python manage.py runserver
See the welcoming site in localhost:8000/ 

## Migrations
	$ python manage.py migrate
## Creating superuser
	$ python manage.py createsuperuser
	$ Username (leave blank to use 'thomas'): mujirin
	$ Email address: mujirin@ui.ac.id             
	$ Password: 
	$ Password (again): 
Superuser created successfully.
Then start the development server
	$ python manage.py runserver
go to the development server by
	$ http://localhost:8000/admin/
enter the username and password
## Creating users app
	$ python manage.py startapp users