# Restaurants REST API

## Requirements

List all the restaurants.
```
    GET /restaurants/
```

Optional parameter available to sort all the restaurants by name.
```
    GET /restaurants/?sort=true
```

Add a restaurant to the list of known restaurants. Names are unique and a
message will be returned if there is duplication.
```
    POST /restaurants/
    {'name': 'Burger1'}
```

Delete a restaurant from the list of restaurants.
```
    DELETE /restaurants/<name>/
```

Pick a random restaurant from the list of restaurants.
```
    GET /restaurants/random/
```

## Environment

If you don't have Python you can follow the instructions from https://www.python.org/downloads/.

Make sure to install Python 3.x

First, create an environment.
```
$ virtualenv env
```
If you have both python 2.x and 3.x versions, use the below command.
```
$ virtualenv --python=/usr/bin/python3 env
```
You can activate it.
```
$ source ./env/bin/activate
```
Verify the version of python with the below command.
```
$ python
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
When not using you can deactivate it.
```
$ deactivate
```

## Dependencies

```
$ pip install -r requirements.txt
```

## Database configuration

Default values are: user=api, password=restaurantapi. Set environment variables
with your own values.

```
$ export DB_USER=<USER>
$ export DB_PASS=<PASS>
```

## Run API

```
$ python manage.py runserver
```

You can go to [http://localhost:8000](http://localhost:8000)
and use the Django REST Framework API interface

or use cURL:

```
$ curl -X GET http://127.0.0.1:8000/restaurants/
```

```
curl -X POST http://127.0.0.1:8000/restaurants/ \
  -H 'content-type: application/json' \
  -d '{"name": "New Restaurant"}'
```
```
curl -X DELETE http://127.0.0.1:8000/restaurants/New%20Restaurant/
```

```
curl -X GET http://127.0.0.1:8000/restaurants/random/
```

## Tests

```
$ python manage.py test
```
