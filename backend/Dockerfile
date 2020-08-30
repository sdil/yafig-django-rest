FROM python:3.8-slim

WORKDIR /app

RUN pip install django djangorestframework drf-yasg psycopg2-binary \
    dj-database-url djangorestframework-simplejwt pyyaml \ 
    Pillow django-cors-headers sentry-sdk django-storages coreapi boto3 \
    whitenoise gunicorn python-memcached
COPY . .
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "yafig_api.wsgi:application"]
