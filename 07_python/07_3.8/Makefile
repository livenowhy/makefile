all: push

# registry.cn-beijing.aliyuncs.com/livenowhy/python:latest

TAG = 3.8
PREFIX = registry.cn-beijing.aliyuncs.com

IMAGE_NAME = livenowhy/python

container:
	docker build -t ${PREFIX}/${IMAGE_NAME}:${TAG} .

push: container
	docker push ${PREFIX}/${IMAGE_NAME}:${TAG}

clean:
	docker rmi -f $(PREFIX):$(TAG) || true
