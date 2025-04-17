all: restart

restart: rm stop run

stop:
	docker-compose stop

rm: stop
	docker-compose rm -f

run:
	docker-compose up -d