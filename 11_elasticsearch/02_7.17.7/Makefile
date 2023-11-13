all: push

TAG = 7.17.7
PREFIX = registry.cn-beijing.aliyuncs.com
IMAGE_NAME = livenowhy/elasticsearch
CONTAINER_NAME = elasticsearch

container:
	docker build -t ${PREFIX}/${IMAGE_NAME}:${TAG} .

push: container
	docker push ${PREFIX}/${IMAGE_NAME}:${TAG}

clean:
	docker rmi -f ${PREFIX}/${IMAGE_NAME}:${TAG} || true