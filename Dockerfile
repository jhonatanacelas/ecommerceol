FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /code
RUN apt update -y
RUN apt install binutils libproj-dev gdal-bin -y
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD python manage.py runserver 0.0.0.0:80
CMD celery -A  ecommerceol worker -l INFO
EXPOSE 80