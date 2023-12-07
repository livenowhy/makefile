all: push

TAG = 1.0.0-alpha.4
PREFIX = registry.cn-beijing.aliyuncs.com
IMAGE_NAME = livenowhy/mongo-express

container:
	docker build -t ${PREFIX}/${IMAGE_NAME}:${TAG} .

push: container
	docker push ${PREFIX}/${IMAGE_NAME}:${TAG}

clean:
	docker rmi -f $(PREFIX):$(TAG) || true