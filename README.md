
1. Install Django
```
pip3 install Django
```
2. Create Django Project
A `Django Project` is a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings. These configurations will be in the `/mysite` directory. You can change `mysite` to any project name you'd like. Tip: avoid using project names like `test` and `Django` - it might mess things up.
```
django-admin startproject mysite . 
```

This creates the following files:
:no_entry_sign:  - you should rarely have to edit these files. 
:white_check_mark:  - you will have to edit these files
```
├── manage.py :no_entry_sign:         # How you run Django code
└── mysite
    ├── __init__.py :no_entry_sign:    # Tells Python this is a Python code folder
    ├── asgi.py :no_entry_sign:         # Provides hooks for web servers when Django app is deployed
    ├── settings.py :white_check_mark:    # Configures the Django project
    ├── urls.py :white_check_mark:        # Routes web requests based on the URL
    └── wsgi.py :no_entry_sign:         # Provides hooks for web servers when Django app is deployed
```

2. Create Django App
A `Django App` is 
```
django-admin startproject mysite . 
```