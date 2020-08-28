# Cars API
This project is a REST API made as a task from Netguru

## Overview
- [Cars API](#cars-api)
  - [Overview](#overview)
  - [Requirements](#requirements)
  - [Setup](#setup)
    - [.env configuration](#env-configuration)
    - [Run project](#run-project)
    - [Test REST API](#test-rest-api)
  - [Used technologies](#used-technologies)


## Requirements
- [Docker](https://docs.docker.com/v17.12/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)


## Setup
Firstly you need to have [required programs](#requirements)
1. Clone/download the repository
2. Enter inside project directory on your machine
3. Create **.env** file based on **.env-example** [click here to read more](#env-configuration)
4. `docker-compose build`
5. Now you can **[run](#run-project)** or **[test](#test-rest-api)** project


### .env configuration
To create .env file follow these steps:
1. Copy *.env-examle* as **.env**     <br /> - Linux(Debian) terminal example: **`cp .env-example .env`**
2. Edit .env file                     <br /> - Linux(Debian) terminal example: **`nano .env`**
3. Set boolean *DJANGO_DEBUG* (*TRUE* or *FALSE*)
4. Set *ALLOWED_HOSTS* with your IP's or/and sides (if you want to add **more then one** use *[comma symbol](https://en.wikipedia.org/wiki/Comma)*, if you want to **allow all** use *[asterisk symbol](https://en.wikipedia.org/wiki/Asterisk)*)
5. Additional, non required:
   1. Add *DATABASE_URL* as URL to your DB, but if you don't set this variable Django will create SQLite DB file after run app using docker
   2. Set your *DJANGO_SECRET_KEY*, but if you don't set up this variable Django will generate random key each time you run the app using docker

.env file should look like this:
```
DJANGO_DEBUG=FALSE
ALLOWED_HOSTS=localhost, 0.0.0.0, other_ip, some-side.com, *
DJANGO_SECRET_KEY=your-key-here
DATABASE_URL=your-db_url-here
```

[Back to setup](#setup)\
[Back to overview](#overview)

### Run project
>Firstly [setup project](#setup)\
To run the project using this command:
`docker-compose up`

[Back to setup](#setup)\
[Back to overview](#overview)

### Test REST API
>Firstly [setup project](#setup)\
To run tests use this command:
`docker-compose run app bash -c "python manage.py test"`\
If command above doesn't work use this command:
`docker-compose run app bash -c "python manage.py test api"`

[Back to setup](#setup)\
[Back to overview](#overview)


## Used technologies

technologies:
  - [Docker](https://docs.docker.com/v17.12/install/)
  - [Docker Compose](https://docs.docker.com/compose/install/)
  - [python 3.8.5](https://www.python.org/downloads/release/python-385/)
  - [PostgreSQL](https://www.postgresql.org/) - I choose those SQL DB because it is more professional than SQLite which I often use in my projects

python frameworks & libraries:
  - **[django](https://www.djangoproject.com/)** - the framework for web apps (I did not learn other web apps frameworks for python like Flask because I think Django is the most community-supported and brilliant for big project usage)
  - **[django rest framework](https://www.django-rest-framework.org/)** - the framework for REST API's compatible with Django, is must-have for REST API projects because of features that are provided for the developer's usage
  - **[drf-yasg](https://drf-yasg.readthedocs.io/en/stable/)** - easy to use docs generator for Django rest framework, also must have for REST API project in my opinion, because that provides us easy to read and use for humans docs like swagger or redoc
  - **requests** - used for validate data by requesting cars from used [vehicle API](https://vpic.nhtsa.dot.gov/api/)
  - django-environ, python-decouple, dj_database_url - for statics files and reading .env file values
  - psycopg2 - required PostgreSQL library

[Back to overview](#overview)
