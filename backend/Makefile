app=yafig

run:
	docker run -it -v $(shell pwd):/app --env PORT=8000 -p 8000:8000 $(app)

ssh:
	docker run -it --env-file ./unittest.env -v $(shell pwd):/app --env PORT=8000 -p 8000:8000 $(app) bash

test:
	docker run -it --env-file ./unittest.env -v $(shell pwd):/app --env PORT=8000 -p 8000:8000 $(app) ./manage.py test --settings=yafig_api.settings.unittest

build-docker:
	docker build -t $(app) .

make-migrations: build-docker
	docker run -it --env-file ./unittest.env -v $(shell pwd):/app --env PORT=8000 -p 8000:8000 $(app) ./manage.py makemigrations --settings=yafig_api.settings.unittest

push-dockerio:
	docker build -t piukul/yafig-monolith .
	docker push piukul/yafig-monolith

dev:
	docker-compose up

build:
	docker-compose build
