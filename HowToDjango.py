""" From Python Crash Course.  
Steps to setup virtual machine with Django and a sqlite.

mkdir bb_log
cd bb_log

Start virtual environment:
	first stop the old one, if there is one
(35_env) tomg@tomg-Inspiron-5759:~/code/bb_log$ deactivate

virtualenv bb_env

source bb_env/bin/activate

start Django
pip install Django

Create a project in Django 
django-admin.py startproject bb_log . 

The Django project has a database that keeps track of its models, etc.
Update it with  (creates  db.sqlite3):
	python manage.py migrate

run a web service to view the project:
	python manage.py runserver

	http://127.0.0.1:8000/

	Control C will stop it

Start a new App:
	source bb_env/bin/activate
	python manage.py startapp bb_logs


Created new subdirectory, bb_logs.  Go there and start editing models.py

MODEL
the models.py contains class TableOne(models.Model):
	with the definations of the Table contents...

After making changes to the django database they need to be activated:
	Edit settings.py in bb_log/bb_log/settings.py
	# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

	# My apps
	'bb_logs',

Now migrate the info to the database:
	python manage.py makemigrations bb_logs
	python manage.py migrate
	
Enabling the Superuser for the web site:
	python manage.py createsuperuser
	tomg greenday
Edit bb_log/bb_logs/admin.py by adding:

	from bb_logs.models import Operation, Base

	# Register your models here.
	admin.site.register(Operation)
	admin.site.register(Base)

Now experience the web site with http://localhost:8000/admin
	Adding extra data, using pull downs to fill in ForeignKey links.


Mapping a URL, creating subpages and passing arguments:
	Edit bb_log/urls.py
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'', include('bb_logs.urls', namespace='bb_logs')),
]
This will cause blank web addresses, r'',  to go to bb_logs.urls

Make a copy of the above urls.py into bb_log/bb_logs/urls.py:
urlpatterns = [
    url(r'^$', views.index, name='index'),
	
this will call view.py with a def index(request)
which processes url inputs and then calls the template index.html
First make several directories:   bb_log/bb_logs/templates/bb_logs
Create index.html inside the inner most, with any old HTML.

More pages, Inheritance from base.html:
	<p> Home Page </p>
	<a href="{% url 'bb_logs:index' %}>Boom Beach Home</a>
	
	{% block content%}	{% endblock content %}
Rewrite index.html to inherit from base.html:
	
{% extends "bb_logs/base.html" %}
{% block content %}
<H>Boom Beach Logs</H>

<p>The No Feet Task Force objectives and information about the battles will be presented here.  Members of our Task Force will be able to log in to see TF specific information. </p>
{% endblock content %}

As the author Eric Matthes says, this is a lot of overhead.  It means for each new 
view page you need to do:
	Create newpage.html  in templates/bb_logs
	Add to Edit bb_log/urls.py urlpatterns r'^newpage/$' ...
	Add to views.py return render(request, 'bb_logs/newpage.html', context)
	
Create a base view, list all  bases and their Operation,
best to list alphabetcal by operation
First bb_logs/urls.py






"""

