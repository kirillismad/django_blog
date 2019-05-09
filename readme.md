# Django blog
Blog example using **Django** backend stack

## Overview
Web application implements:
- Sign up/sign in
- Create post (with couple of tags)
- Get list of posts (+ search)
- Get post with specific tag
- Get specific post
- Comment post
- Edit self profile
- Get list of other profiles (+ search)
- Get a specific profile and its posts
- Admin panel

## Features
- Caching
- Task queue
- JWT auth (for api)
- API schema
  
## Database schema
![db schema](https://github.com/kirillismad/django_blog/blob/master/screenshots/dbschema.png?raw=true)


## Requirements
- Python 3.7
- Django 2.2
- DRF
- PostgreSQL
- Memcached (https://github.com/lericson/pylibmc)
- Celery
- RabbitMQ
- Swagger (https://github.com/axnsan12/drf-yasg)
- JWT Auth (https://github.com/GetBlimp/django-rest-framework-jwt)
  
## How to run

[Vagrant](https://www.vagrantup.com/downloads.html)

[Docker Compose](https://docs.docker.com/compose/install/)

### Vagrant
```
username@pcname:/dir/with/Vagrantfile$ vagrant up && vagrant ssh # up virtual machine
vagrant@ubuntu-bionic:~$ source v_env/bin/activate # activate virtualenv
(v_env) vagrant@ubuntu-bionic:/vagrant/src$ cd /vagrant/src/  # go to source directory
(v_env) vagrant@ubuntu-bionic:/vagrant/src$ python manage.py runserver 0.0.0.0:8000  # run server
```

Go to browser: `localhost:8000/`

### Docker
```
username@pcname:/dir/with/docker-compose.yml$ docker-compose up --build
```

Go to browser: `localhost:8080/`

#### Credentials
- email: blogadmin@main.ru, password: 7890uiop **(admin)**
- email: thispersondoesnotexist1@mail.ru, password: 7890uiop
- email: thispersondoesnotexist2@mail.ru, password: 7890uiop
- email: thispersondoesnotexist3@mail.ru, password: 7890uiop
- email: thispersondoesnotexist4@mail.ru, password: 7890uiop
- email: thispersondoesnotexist5@mail.ru, password: 7890uiop
- email: thispersondoesnotexist6@mail.ru, password: 7890uiop

**All user faces are obtained from [thispersondoesnotexist.com](https://thispersondoesnotexist.com).**


![main page](https://github.com/kirillismad/django_blog/blob/master/screenshots/main_page.png?raw=true)


#### API schema
Go to browser: `localhost:8080/api/` (for docker run)

![api schema](https://github.com/kirillismad/django_blog/blob/master/screenshots/api.png?raw=true)


## Tests
### Vagrant
```
(v_env) vagrant@ubuntu-bionic:/vagrant/src$ python manage.py test
```
### Docker
```
username@pcname:/dir/with/docker-compose.yml$ docker-compose run --entrypoint="python manage.py test" web
```