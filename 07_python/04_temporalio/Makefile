all: push

PREFIX = registry.cn-beijing.aliyuncs.com

TAG = temporalio
IMAGE_NAME = livenowhy/python

container:
	docker build -t ${PREFIX}/${IMAGE_NAME}:${TAG} .

push: container
	docker push ${PREFIX}/${IMAGE_NAME}:${TAG}

clean:
	docker rmi -f $(PREFIX):$(TAG) || true
