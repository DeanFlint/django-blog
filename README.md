### SETUP ENV

``` wget -q https://git.io/v77xs -O /tmp/setup-workspace.sh && source /tmp/setup-workspace.sh ```

#### Create a virtual env:

``` mkvirtualenv foo ```

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

