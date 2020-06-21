# YAFIG API Server (Django REST Framework)

## Implementations

| Django App | Details |
|------------|---------|
| API Doc    | [DRF YASG](https://drf-yasg.readthedocs.io/en/stable/) - Redoc style |
| User       | Uses DRF SimpleJWT for authentication |
| Post       | Uses [Generic Views](https://www.django-rest-framework.org/api-guide/generic-views/) |
| Search     | Uses bare request handler |

## Wishlist

- Celery & Celery Beatx
- Reliability: [on_commit()](https://docs.djangoproject.com/en/3.0/topics/db/transactions/) message dispatching, atomic transaction
- Performance optimizations: Select_Related, Prefetch_related, defer & only query, query annotation, Func
- Queryset Q & F
- FilterSet
- Django-cacheops
- Django social login
- Django Channel & [Shared WebWorker](https://noti.st/aaronbassett/xzOUkb)
- django-debug-toolbar & django-silk
- uptime monitor (ensure heroku dyno is active all the time)
- [APM](https://www.youtube.com/watch?v=optor4DsgvY)
- django-url-filter
- Varnish caching (serving static cache even the API is breaking)
- Rate limiting
- Load testing with Locust
- django-memoize
- ORM: unique_together, indexes & partial/conditional index, Lag, Window, raw SQL, select extra, custom queryset and custom manager, inspect query (`str(order.query`)

## References

- [Build user registration & authorization using SimpleJWT](https://hackernoon.com/110percent-complete-jwt-authentication-with-django-and-react-2020-iejq34ta), [Github repo](https://github.com/Toruitas/Complete-JWT-Authentication/?ref=hackernoon.com)
- [Django REST OpenAPI 3 Support](https://djangoadventures.com/django-rest-framework-openapi-3-support/)
- [Build File/Image upload in DRF](https://www.techiediaries.com/django-rest-image-file-upload-tutorial/)
- [Upload files to S3 using DRF](https://stackoverflow.com/questions/46195181/upload-file-to-s3-using-drf)

## Conferences

- [DjangoCon US 2016 - High-Availability Django by Frankie Dintino](https://www.youtube.com/watch?v=lAMlZviIPw4&list=PLE7tQUdRKcyZNknh0wA44b5IEIxQ37vL7&index=10)
- [DjangoCon 2014- High Performance Django: From Runserver to Reddit Hugs](https://www.youtube.com/watch?v=Toa9lW8UMOA)
- [DjangoCon 2019 - Prepping Your Project for Production by Peter Baumgartner](https://www.youtube.com/watch?v=tssYpA6WiQM)
- [DjangoCon 2019 - Pushing the ORM to its limits](https://www.youtube.com/watch?v=MPpPu6c8wsM)
