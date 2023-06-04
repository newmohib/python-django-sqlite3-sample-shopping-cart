# Python Sample Shopping Cart

### install django

    pip install django=2.1

### initialize application

    django-admin startproject pyshop .

### Start Application

    python manage.py runserver

### Open in Browser this URL
    127.0.0.1:8000


### Create a package like products
    python manage.py startapp products

### Create migration up

    python manage.py makemigrations

### Create migration up
    python manage.py migrate

### include Template

    {% include navbar.html %}