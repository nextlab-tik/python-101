Python 101 Introduction - Web Dev with Django
=============================================

Common Django Commands
----------------------

```sh
django-admin startproject PROJECT_NAME . # create a django project on current dir
python manage.py startapp APP_NAME       # create an app
python manage.py runserver [IP:PORT]     # run server on address http://IP:PORT or http://127.0.0.1:8000
python manage.py makemigrations          # generate app migration files
python manage.py migrate                 # apply migration files
python manage.py createsuperuser         # create superuser account
```

Common Django app dev steps
---------------------------

- add app name to `INSTALLED_APPS` array on `PROJECT_NAME/settings.py` file.
- add url pattern to `urlpatterns` array on `PROJECT_NAME/urls.py` file to include APP_NAME `urls.py` file.
- define view function (or class) on `APP_NAME/views.py`
- define url pattern releated to the view function on `APP_NAME/urls.py` and add `name`
- define our Databese models on `APP_NAME/models.py` based on `models.Model` class
- define `__str__` funtion for every model to have a better name
- register our models to the admin site on `APP_NAME/admin.py`
- add our templates files under `APP_NAME/templates/APP_NAME/TEMPLATE.html`

Links
-----

- Django:

  - [Open Class Room Django Tutorial](https://openclassrooms.com/courses/developpez-votre-site-web-avec-le-framework-django)
    (French)
  - [Django Official Documentation](https://docs.djangoproject.com/en/1.10):

    - [Django Official Tutorial](https://docs.djangoproject.com/en/1.10/intro/overview/)

- HTML5 & CSS3:

  - [Open Class Room HTML5 Tutorial](https://openclassrooms.com/courses/apprenez-a-creer-votre-site-web-avec-html5-et-css3)
    (French)
  - [Mozilla Developer Network](https://developer.mozilla.org/en-US/):

    - [Web Docs](https://developer.mozilla.org/en-US/docs/Web)

  - [Bootstrap 4 Doc](http://v4-alpha.getbootstrap.com/getting-started/introduction/)

- JavaScript:

  - [Open Class Room JavaScript Tutorial](https://openclassrooms.com/courses/dynamisez-vos-sites-web-avec-javascript)
    (French)
  - [Mozilla Developer Network](https://developer.mozilla.org/en-US/):

    - [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

  - [Angular 2 Doc](https://angular.io/docs/ts/latest/):

    - [Quick Start](https://angular.io/docs/ts/latest/quickstart.html)
    - [Guide](https://angular.io/docs/ts/latest/quickstart.html)
