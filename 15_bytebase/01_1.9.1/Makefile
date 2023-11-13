all: push

TAG = 1.9.1
PREFIX = registry.cn-beijing.aliyuncs.com
IMAGE_NAME = livenowhy/bytebase
CONTAINER_NAME = 'bytebase'


container:
	docker build -t ${PREFIX}/${IMAGE_NAME}:${TAG} .

push: container
	docker push ${PREFIX}/${IMAGE_NAME}:${TAG}

clean:
	docker rmi -f $(PREFIX):$(TAG) || true

start:
	docker run -d --init \
	--name=${CONTAINER_NAME} \
	--add-host=base.livenowhy.com:10.2.31.9 \
	--restart always \
	--publish 5678:8080 \
	--health-cmd "curl --fail http://localhost:5678/healthz || exit 1" \
	--health-interval 5m \
	--health-timeout 60s \
	--volume ~/.bytebase/data:/var/opt/bytebase \
	${PREFIX}/${IMAGE_NAME}:${TAG} \
	--data /var/opt/bytebase \
	--port 8080

stop:
	docker stop ${CONTAINER_NAME} || true

rm: stop
	docker rm -f ${CONTAINER_NAME} || true

restart: stop rm start

# https://www.bytebase.com/docs/get-started/install/deploy-with-docker?source=console

# https://www.modb.pro/db/491964
