all: push

TAG = 8.5.1
PREFIX = registry.cn-beijing.aliyuncs.com
IMAGE_NAME = livenowhy/elasticsearch
CONTAINER_NAME = elasticsearch

container:
	docker build -t ${PREFIX}/${IMAGE_NAME}:${TAG} .

push: container
	docker push ${PREFIX}/${IMAGE_NAME}:${TAG}

clean:
	docker rmi -f ${PREFIX}/${IMAGE_NAME}:${TAG} || true