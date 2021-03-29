# OOWLISH-Task
 Django REST API that provides information about customers.

## Project Setup


**Install requirements**

```console
$ pip install -r requirements.txt --user
```
**Management command : Create two extra fields for latitude and longitude using Google Maps API**

```console
$ python manage.py Google_Maps_API
```
**Management command : import the customers.csv file into your database**

```console
$ python manage.py Database
```


**Update the database**

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

**Simple web page to consume the REST API**

```console
http://127.0.0.1:8000/swagger/
```


![image](https://user-images.githubusercontent.com/73910136/112832347-17dbc780-908d-11eb-823b-c5346bf56cc7.png)
![image](https://user-images.githubusercontent.com/73910136/112832424-32ae3c00-908d-11eb-9e43-593cb8185b24.png)


