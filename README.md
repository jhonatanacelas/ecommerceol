# Omni Latam

This project corresponds to the business e-commerce model  

## Decisions

- This project was developed in Python 3.8 with Django 3.2.3
- The project was structured in the following modules: Orders, Shipments, Users, Payments
- Django Rest Framework was implemented for the API
- For the asynchronous process, Celery was implemented
- RabbitMQ was used for queues
- For the API test APITestCase from rest_framework.test was used

## Architecture

- Data base  [link](https://drive.google.com/file/d/1-roXGWDPlr0gOjpaf6I1D34nAhykGmfo/view?usp=sharing)


## Installation

###Requirements 
- Python3.8
- Rabbit MQ port 5672 

## Usage

Install requirements 


```
pip install -r requirements.txt
```

Run migrations

```
python manage.py migrate
```

Run project

```
python manage.py runserver 
```

Run celery 

```
celery -A ecommerceol -l INFO
```

Run the test

```
python manage.py test
```

# API Documentation in Redoc 

http://127.0.0.1:8000/redoc 

## SQL showing the paid orders 

Is located in query.sql file

