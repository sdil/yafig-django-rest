FROM python:3.8-slim

WORKDIR /app

RUN pip install django djangorestframework drf-yasg psycopg2-binary \
    dj-database-url djangorestframework-simplejwt pyyaml \ 
    Pillow django-cors-headers sentry-sdk django-storages coreapi boto3
COPY . .
CMD ./manage.py runserver 0.0.0.0:$PORT
