all: push

TAG = 2.7.18-ansible
PREFIX = registry.cn-beijing.aliyuncs.com
IMAGE_NAME = livenowhy/python
STATUS = 无法自动构建   # 状态: 已自动构建, 未构建

container:
	docker build -t ${PREFIX}/${IMAGE_NAME}:${TAG} .

push: container
	docker push ${PREFIX}/${IMAGE_NAME}:${TAG}

clean:
	docker rmi -f $(PREFIX):$(TAG) || true
