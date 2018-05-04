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

