run:
	docker run -it -v $(shell pwd):/app --env PORT=8000 -p 8000:8000 registry.heroku.com/yafig-django/web

ssh:
	docker run -it --env-file ./unittest.env -v $(shell pwd):/app --env PORT=8000 -p 8000:8000 registry.heroku.com/yafig-django/web bash

test:
	docker run -it --env-file ./unittest.env -v $(shell pwd):/app --env PORT=8000 -p 8000:8000 registry.heroku.com/yafig-django/web ./manage.py test --settings=yafig_api.settings.unittest

make-migrations:
	docker run -it --env-file ./unittest.env -v $(shell pwd):/app --env PORT=8000 -p 8000:8000 registry.heroku.com/yafig-django/web ./manage.py makemigrations --settings=yafig_api.settings.unittest

build-dockerio:
	docker build -t registry.heroku.com/yafig-django/web .
	docker build -t piukul/yafig-monolith .

push-dockerio:
	docker build -t piukul/yafig-monolith .
	docker push piukul/yafig-monolith

dev:
	docker-compose up

build:
	docker-compose build
