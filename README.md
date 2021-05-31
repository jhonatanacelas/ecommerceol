# Omni Latam

This project correspond to e-commerce model business 

## Decisions

- This project was developed in Python 3.8  with Django  3.2.3
- The project was ordered in the following modules: Orders, Shipping, Users, Payments
- For the API  was implemented Django Rest Framework
- For Asynchronous proccess was implemented Celery
- For Queue was used RabbitMQ  
- For API test was used APITestCase from rest_framework.test

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

