# django

## About

This is a repo following the steps of the Django framework tutorial

## Part I

### Create a proyect:

* To start a project: `django-admin startproject mysite`
* Run testing server: `python3 manage.py runserver (0.0.0.0:8000)`
                              
### Create an app:

A proyect can contain multiple apps

* Create the polls app: `python3 manage.py startapp polls`

### Creating my first (app) view:

* Create an index view at `polls/views.py`:
  * Import `HttpResponse` module from `django.http`
  * Define `index` function:
    ```python 
    def index(response):
      return HttpRespose('Hello mode fokas!')
    ```
* Create an `url.py` module inside polls folder (app):
  * Import the `url` module from `django.conf.urls`
  * Import the `views` module
  * create the `urlpatterns` list:
    ```python
    urlpatterns = [
      url(r'^$', views.index, name='index'),
    ]
    ```
* Inlude the `polls/urls` in the proyect root urls list:
  * Import the `include` mudule from `django.conf.urls`
  * Include the module inside the urlpatterns list:
    ```python
    urlpatterns = [
      url(r'^polls/', include('polls/urls')),
      url(r'^admin/', admin.site.urls),
    ]
    ```
Notes: 
* When using include() the regular expression doesnt have `$` (end-of-string match character)
* String inside include


## Part II

### Database setup











***** Second tuto notes:




Set local time: myite.settings.py : TIME_ZONE


Run  `python manage.py migrate` to look at the INSTALLED_APPS in mysite/settings.py and create any necesaty database tables that the default apps need.

Creamos los models de nuestra app (encuesta) questions and Choices

```python 


from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

```


tell the project that the polls app is installed: add ` 'polls.apps.PollsConfig',` to The `INSTALLED_APPS` IN `mysite/settings.py`

Para decirle a Django que hemos hecho cambios en el model nuestra app `polls`

      python manage.py makemigrations polls




 Ver que hace la sql migration: `python manage.py sqlmigrate polls 0001`


 Despues volvemos a escribir `python3 manage.py migrate` para crear las tablas del modelo que hemos creado con makemigrations en la base de datos.



 ***

 Change your models (in models.py).
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.

***



Playing with the API



python3 manage.py shell


*****

