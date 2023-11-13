all: push

TAG = 1.5
PREFIX = registry.cn-beijing.aliyuncs.com
IMAGE_NAME = livenowhy/kapacitor
CONTAINER_NAME = kapacitor

container:
	docker build -t ${PREFIX}/${IMAGE_NAME}:${TAG} .

push: container
	docker push ${PREFIX}/${IMAGE_NAME}:${TAG}

clean:
	docker rmi -f ${PREFIX}/${IMAGE_NAME}:${TAG} || true