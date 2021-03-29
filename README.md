# oowlish
 Django REST API that provides information about customers.

## Project Setup


**Install requirements**

```console
$ pip install -r requirements.txt --user
```
**Management command : Create two extra fields for latitude and longitude using Google Maps API **

```console
$ python manage.py Google_Maps_API
```
**Management command : import the customers.csv file into your database**

```console
$ python manage.py Database
```


**Update the database **

```console
$ python manage.py migrate
```

**Start the web server on `http://127.0.0.1:8000/`**

```console
$ python manage.py runserver
```
## Usage

| HTTP verbs | Paths  | Used for |
| ---------- | ------ | --------:|
| GET | api/customers/|List all customers|
| GET | api/customers/id | Show a single customer |
