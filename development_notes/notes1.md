
## Creating Github Repository
### Cloning Repository
After creating Github repository, in somewhere of your computers

	$ git clone github.com-Mujirin:Mujirin/School-of-Physics-Platfrom.git

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
See the welcoming site in **localhost:8000/**
### Secret key
- Buat file setara dengan manage.py dengan nama setingan_rahasia.py
- Cut SECRET_KEY di sopp/setting.py dan taruh di setingan_rahasia.py
- Tambahakan

	from setingan_rahasia import *

di bagian paling atas sopp/setting.py

## Gitignore
- Buat file .gitignore setara dengan README.md
- Tambahkan di file tersebut

	# # Secret key
	setingan_rahasia.py

	# # Ignore Mac system files
	.DS_Store

### Commit to the repo
	$ git status
	$ git add .
	$ git status
	$ git commit -m "Initial commit."
	$ git push
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

go to the development server in the browser by

	http://localhost:8000/admin/

Enter the username and password
## Creating users app
	$ python manage.py startapp users