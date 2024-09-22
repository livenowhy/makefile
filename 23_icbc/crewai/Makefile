all: push

# mlops 操作
restart: stop
	docker-compose up -d

stop: 
	docker-compose stop && docker-compose rm -f
