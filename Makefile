run:
	docker run -it -v $(shell pwd):/app --env PORT=8000 -p 8000:8000 --env DATABASE_URL=$(DB_URL) registry.heroku.com/yafig-django/web
	
make-migrations:
	docker run -it -v $(shell pwd):/app --env PORT=8000 -p 8000:8000 --env DATABASE_URL=$(DB_URL) registry.heroku.com/yafig-django/web ./manage.py makemigrations

build:
	docker build -t registry.heroku.com/yafig-django/web .

build-dockerio:
	docker build -t piukul/yafig-monolith .

push-dockerio:
	docker build -t piukul/yafig-monolith .
	docker push piukul/yafig-monolith

deploy-fly:
	docker build -t piukul/yafig-monolith .
	docker push piukul/yafig-monolith
	flyctl deploy --image piukul/yafig-monolith --app yafig-monolith

deploy-heroku:
	heroku container:push web -a yafig-django
	heroku container:release web -a yafig-django
