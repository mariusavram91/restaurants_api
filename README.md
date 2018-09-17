# Restaurants REST API

List all the restaurants.
```
    GET /restaurants
```

Add a restaurant to the list of known restaurants.

```
    POST /restaurants
    {'name': 'Burger1'}
```

Delete a restaurant from the list of restaurants.
```
    DELETE /restaurants/<name>
```

Pick a random restaurant from the list of restaurants.
```
    GET /restaurants/random
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
