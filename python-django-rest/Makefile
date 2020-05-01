run-local:
	docker run -it -v $(shell pwd):/app --env PORT=8000 -p 8000:8000 --env DATABASE_URL=$(DB_URL) registry.heroku.com/yafig-django/web

build-local:
	docker build -t registry.heroku.com/yafig-django/web .

deploy-heroku:
	heroku container:push web -a yafig-django
	heroku container:release web -a yafig-django