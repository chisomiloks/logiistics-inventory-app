### Shopify Backend Developer Intern Challenge (Summer 2022) Project

Inventory tracking web application for a logitics company.

***Instructions to follow...***

In order to run the application you need to have the following installed.

- Python 3
- Django, and 
- The following django packages 
  - django-crispy-forms
  - django-taggit
  - django-import-export

---

Installation Instructions

---

1. Python

- Detailed instructions for installing python3 depending on your operating system (OS) can be found at [Python 3 Installation & Setup Guide](https://wsvincent.com/install-python/) by William Vincent

> It is advised that you install a python virtual environment and install django and the different packages in order to run the application on that environment

>> Virtual Environment Install and Activation (I use pipenv, the user can explore other virtual environment tools if they want or use the virtual environment service they already have)

```
pip3 install pipenv
``` 

to install, then run

```
pipenv shell
```

in the main directory where the files of the application are stored to activate the virtual environment. 

You can now install Django and the other packages in the activated environment using th commands below. (N/B - to exit the evironment you only need to enter the command ***exit*** and to start it up again, you rerun ***pipenv shell*** in the directory)

2. Django
```
pipenv install django
```

Application uses latest version of Django


3. django-crispy forms
```
pipenv install django-crispy-forms
```

4. django-import-export
```
pipenv install django-import-export
```

5. django-taggit
```
pipenv install django-taggit

```

run python command to open interpreter and confirm it points to python 3 if not use python3 instead of python for commands below

---

Run Application

---

In application main directory (The directory with the ***manage.py*** file), run
```
python manage.py runserver
```

to start the application server.


If getting warning about migrations, run

```
python manage.py makemigrations
```
```
python manage.py migrate
```

Visit http://127.0.0.1:8000/ to visit application homepage

For administrative page visit http://127.0.0.1:8000/admin and login with the following information

```
Admin Account

Username - admin
Password - admin@123

```

Extra feature related to exporting product data to a csv can be found under Inventorys