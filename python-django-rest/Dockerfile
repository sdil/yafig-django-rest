FROM python:3.8-slim

WORKDIR /app

RUN pip install django djangorestframework drf-yasg
COPY . .
CMD ./manage.py makemigrations && ./manage.py runserver 0.0.0.0:$PORT