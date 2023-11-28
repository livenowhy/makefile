all: push

TAG = 3.10-alpine-base
PREFIX = registry.cn-beijing.aliyuncs.com
IMAGE_NAME = livenowhy/python

container:
	docker build -t ${PREFIX}/${IMAGE_NAME}:${TAG} .

push: container
	docker push ${PREFIX}/${IMAGE_NAME}:${TAG}

clean:
	docker rmi -f $(PREFIX):$(TAG) || true
