all: push

TAG = python
PREFIX = registry.cn-beijing.aliyuncs.com
IMAGE_NAME = livenowhy/ubuntu

container:
	docker build -t ${PREFIX}/${IMAGE_NAME}:${TAG} .

push: container
	docker push ${PREFIX}/${IMAGE_NAME}:${TAG}

clean:
	docker rmi -f $(PREFIX):$(TAG) || true

# registry.cn-beijing.aliyuncs.com/livenowhy/ubuntu:python
