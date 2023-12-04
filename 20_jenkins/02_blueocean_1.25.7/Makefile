all: push

TAG = blueocean1.25.7
PREFIX = registry.cn-beijing.aliyuncs.com

IMAGE_NAME = livenowhy/jenkins

container:
	docker build -t ${PREFIX}/${IMAGE_NAME}:${TAG} .

push: container
	docker push ${PREFIX}/${IMAGE_NAME}:${TAG}

clean:
	docker rmi -f $(PREFIX):$(TAG) || true

# registry.cn-beijing.aliyuncs.com/livenowhy/jenkins:2.303.2