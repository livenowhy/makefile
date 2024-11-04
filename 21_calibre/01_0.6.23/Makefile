all: push

TAG = 0.6.23
PREFIX = registry.cn-beijing.aliyuncs.com
IMAGE_NAME = livenowhy/calibre-web

container:
	docker build -t ${PREFIX}/${IMAGE_NAME}:${TAG} .

push: container
	docker push ${PREFIX}/${IMAGE_NAME}:${TAG}

clean:
	docker rmi -f $(PREFIX):$(TAG) || true