# BigHouzz

BigHouzz - system for managing relationships with neighbors in multi-apartment residential buildings

## System Requirements and Stack Technologies

  * Python 3.12
  * Django 4.2.6
  * django-bootstrap v5
  * django-environ 0.11.2
  * pillow 10.1.0

## Documentation

The full documentation is at https://github.com/botalov-pro/BigHouzzz/wiki

## Installation

  1. Install and activate the virtual environment
  2. Create a .env file in the project root folder with the following contents:
```python
DEBUG=True
SECRET_KEY='<YOUR_SECRET_KEY>'
```
  3. Install dependencies from requirements.txt file
```python
pip install -r requirements.txt
``` 
  4. Do a database migration
```python
python manage.py makemigrations
python manage.py migrate
``` 
  5. Create a superuser
```python
python manage.py createsuperuser
``` 
  6. In the folder with the manage.py file, run the command:
```python
python manage.py runserver
``` 

## Bugs and suggestions

If you have found a bug or if you have a request for additional functionality, please use the issue tracker on GitHub.

https://github.com/botalov-pro/BigHouzzz

## Author

Developed and maintained by [Konstantin Botalov](https://botalov.pro)
