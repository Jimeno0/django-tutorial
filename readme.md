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

Im going to use SQLite in order to keep it simple and just focus on the framekork. To setup another DB chek the [tutorial part II](https://docs.djangoproject.com/en/1.10/intro/tutorial02/) or the [DB bindings](https://docs.djangoproject.com/en/1.10/topics/install/#database-installation).

From this point Im going to work with a SQLite DB.

* First Im going to set the `TIME_ZONE` in `mysite/settings.py` to my time zone (`Europe/Madrid`).
* Run `python3 manage.py migrate`: The migrate command looks at the `INSTALLED_APPS` in `settings.py` and create any necessary database table.


### Creating models

To define our models (database layouts):

* In `polls/models.py` we import `models` from `django.db`
* The we define our two models by classes:

  ```python
  class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

  class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
  ```
* Then we need to tell our project that the Polls app is installed:
  Go to `INSTALLED_APPS` in `mysite/settings.py` and add the "dotted" path to the polls app config: `polls/apps/PollsConfig`

* Then we run `python3 manage.py makemigrations polls` with `makemigrations` we are telling django taht we have made some changes to our model (made new ones) and want to store it as a migration (migrations is how django stores changes in our models)

* Finally run `python3 manage.py migrate` to create those model tables to our DB.

RESUME:

* Change your models (in `models.py`).
* Run `python manage.py makemigrations` to create migrations for those changes
* Run `python manage.py migrate` to apply those changes to the database.

### Playing with the API

Run `python3 manage.py shell` to invoke the python shell and start playing with the Django API.

Then we start playing:

* `>>>from polls.models import Question, Choice` | Import db models
* `>>> Question.objects.all()` | get all Questions 
* `>>> from django.utils import timezone` | 
* `>>> q = Question(question_text = 'whats up?', published_date = timezone.now())` | create a new question object
* `>>> q.save()` | save to the DB
* `>>> q.id` | acces to the id property
* `>>> q.question_text = 'Whats new fellas?'` | Change a property/field 
* `>>> q.save()` | Save the change
* `>>> Question.objects.all()` | get all questions obtaining: `<QuerySet [<Question: Question object>]>` not very usefull. to solve that add a method to the models classes `def __str(self):
    return self.choice_text`


Django provides a db lookup API

* `filter()` IE: 
  * `Question.objects.filter(id=1)`
  * `Question.objects.filter(question_text__startswith = 'What')
  * `Question.objects.filter(date_published__year = timezone.now().year)` (previously we need to import `timezone` from `django.utils`)
* `.get()` : `q = Question.objects.get(id=1)`

Create choices depending on the question (foregin key)

* Django creates a set to hold the other side of a `ForeginKey`
* `.create()` constructs a new choice object, pass it to the choices set and return  new Choice object
  * No need to `.save()` when `.create()`
  * Set the question target to add choices to it: `q = Question.objects.get(pk=1)`
  * To view all choices depending on q: `>>> q.choice_set.all()`
  * Add a choice: `>>> c = q.choice_set.create(choice_text='Not much', votes=0)`
  * Choice objects have API access to their related Question objects. `>>> c.question`
  * And viceversa: `>>> q.choice_set.count()`
  * Double underscores to separate relationships, as deep as you want: `>>> Choice.objects.filter(question__pub_date__year=current_year)`
  * To delete a Choice: `>>> c.delete()`

### Introducing to Django admin

Firts we need to create user who can logging to the admin site:
* Run `python3 manage.py createsuperuser`
* Then introduce a User name, mail and pass IE: Admin 123123123
* Start the server again `python3 manage.py runserver` go to localhost:8000/admin/ and introduce your credentials
* To can edit the `Question` model: In `polls/admin.py` and add:
  
  ```python
  from django.contrib import admin

  from .models import Question

  admin.site.register(Question)
  ```
