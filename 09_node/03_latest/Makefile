all: push

TAG = latest
PREFIX = registry.cn-beijing.aliyuncs.com
IMAGE_NAME = livenowhy/node

container:
	docker build -t ${PREFIX}/${IMAGE_NAME}:${TAG} .

push: container
	docker push ${PREFIX}/${IMAGE_NAME}:${TAG}

clean:
	docker rmi -f $(PREFIX):$(TAG) || true