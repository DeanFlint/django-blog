### SETUP ENV

``` wget -q https://git.io/v77xs -O /tmp/setup-workspace.sh && source /tmp/setup-workspace.sh ```

#### Create a virtual env:

``` mkvirtualenv foo ```

##### Side note: When opening a terminal, to switch back to your virtenv:

``` workon foo ```

#### Install Django:

``` sudo pip3 install django==1.11 ```

#### Create requirements.txt:

``` pip freeze > requirements.txt ```

#### Create the project:

``` django-admin startproject blog . ```

#### Change mode on manage.py to make executional:

``` chmod +x manage.py ```

#### Migrate it:

``` ./manage.py migrate ```

#### Run the server:

``` ./manage.py runserver $IP:$PORT ```

#### Add our hostname into the settings.py:

``` ALLOWED_HOSTS = ['django-blog-deanflint.c9users.io'] ```

#### Create .gitignore:

```
*.sqlite3
*.pyc
.~c9
__pycache__
```

#### Add travis-ci.org

Sign in with github (top right corner)

Click on your name and accounts menu.

Find your repository and click on the toggle.

Click on the name again and click on 'Build/Unknown'.

Select Markdown from the dropdown.

#### Add to the ReadMe:

[![Build Status](https://travis-ci.org/DeanFlint/django-blog.svg?branch=master)](https://travis-ci.org/DeanFlint/django-blog)

#### Create a .travis.yml file and add the following:

``` 
language: python
python: 
    - "3.4"
install: "pip install -r requirements.txt"
script:
- SECRET_KEY="whatever" ./manage.py test
```

### Directory Structure

####

``` ./manage.py startapp posts ```

#### In the root director, create the following folders:

media

media/img

static

static/css

static/img

static/js

#### In the 'posts' app, create the following folder:

templates

#### In settings.py, add the following:

``` 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
]
```

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]
```

```
STATIC_URL = '/static/'
STATICFILES_DIR = (os.path.join(BASE_DIR, 'static'), )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

#### models.py
```
from django.db import models
from django.utils import timezone

class Post(models.Model):
    """ A single blog post """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    
    def __unicode__(self):
        return self.title
```

#### forms.py
```
from django import forms
from .models import Post

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag', 'published_date')
```

#### admin.py
```
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

#### In the terminal:

``` pip install pillow ```

#### Now that we've installed a new package, we need to update requirements.txt:

``` pip freeze > requirements.txt ```

#### Now make your migrations:

``` ./manage.py makemigrations ```

``` ./manage.py migrate ```

#### Install:

``` pip install django-forms-bootstrap ```

#### Update INSTALLED_APPS:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_forms_bootstrap',
    'posts',
]
```

#### Create superuser:

``` ./manage.py createsuperuser ```

