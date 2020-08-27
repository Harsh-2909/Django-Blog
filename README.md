# Django Blog App

A Django blog app created using Django v3 and Python 3.8 for educational purpose. This is my first Django project so it's unrefined around the edges.

**Live Site running on Heroku**: https://mydjangoblogapp2.herokuapp.com/

## Demostration

**CREATING A POST**

![Creating a Post](http://g.recordit.co/Pn4287QG2G.gif)

**UPDATING AND DELETING POST**

![Updating and Deleting a Post](http://g.recordit.co/YK6qBdFYNQ.gif)

**ACCOUNT CREATION AND SIGN IN**

![Account Creation and Login](http://g.recordit.co/i5jpi0HkyE.gif)

## How to Setup in Localhost

1. Clone this repository.
2. Open the cloned repository.
3. Install dependencies using ``pip install -r requirements.txt``
**OR**
Install ``pipenv`` using ``pip install pipenv`` and initialise a Virtual Machine using ``pipenv install`` in the directory.
4. Set environment variables like `SECRET_KEY`, `DEBUG_VALUE`, `EMAIL_USER`, `EMAIL_PASS`.
5. Run the Django Server using ``python manage.py runserver`` and then goto ``localhost:8000`` or ``127.0.0.1:8000`` and see the server running.

### Environment Variables:

`SECRET_KEY`: Django secret key which can be any long hexadecimal value. Django recommends *atleast* **50 characters** to make it secure.
`DEBUG_VALUE`: Set it as **"True"** for Debug environment and **"False"** for Production.
`EMAIL_USER`: The email address that will be used to email incase somebody forgets password.
`EMAIL_PASS`: The password to that email address. Refer to [App Passwords](https://myaccount.google.com/apppasswords) if the email has 2 factor auth.

## How to Setup for Production

Refer on how to deploy Python apps in Heroku [here](https://devcenter.heroku.com/articles/deploying-python) and Django app configuration [here](https://devcenter.heroku.com/articles/django-app-configuration).

## Features

- Create, update and delete posts.
- Create account and Login in it.
- Can send emails incase the user forgets password.
- Profile System with a profile image.
- Follows most of the Django security checks.
- Uses Django Class Views for handling Blog Posts.

#### Known Issues:

- Profile image only works in development environment for me, apparantly hosting images in AWS S3 bucket can fix this problem in production.

*Please make a GitHub issue if any other bugs are found.*

## Notes

This project was created on **Ubuntu-20.04 LTS** and tested under **Windows 10** and **Ubuntu**, and is expected to work fully in other systems too.

This project is still under development. Parts of the source codes may not be well documented. Also suitable prompts may not be available for the user at the moment.

More features and fixes are yet to come. Meanwhile suggestions, ideas, bug reports are welcomed.