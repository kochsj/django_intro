# Django Intro

**Author**: Stephen Koch
**Version**: 1.0.0

## Overview
In this repository, I am exploring the python library [Django](https://www.djangoproject.com/) to create web applications using python. My goal is to start by wiring together several views, run a server, be able to request urls, get views as a response, and pass information between pages. 
## Getting Started (running Django)

First, make sure that you have python3 installed:
```
$ python3 --version
Python 3.7.5
```
If you do not:
```
$ brew install python
```
You need to have the files locally. Click on the green clone or download button and Download ZIP:

![Click_to_download](assets/Click_to_download.png)


In your command line, navigate to this directory:
```
$ cd ~  ##this is your root directory
$ cd Downloads  ##by default: Downloads is a directory inside of your root; and where your file will be downloaded
$ cd django_intro ##and now you are in this directory
```
This is the start of a web app and is currently able to run a server and link views together. 
To run a server you need to install django:
```
$ pipenv install django
```
<br>**To start the server:**

```
$ python3 manage.py runserver
```


## Functionality/Architecture
This web app is for demonstration purposes. It is a Django web app project called candy_site and currently has two 'apps' contained in it; snickers and frosted flakes.

We are currently able to run a server and, using the nav.html template, navigate between four urls/four different views.

## Change Log
Mon Jan 13 2020 20:36:07<br>Wired together a django driven website.

