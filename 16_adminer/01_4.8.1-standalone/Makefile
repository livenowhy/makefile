all: push

TAG = 4.8.1-standalone
PREFIX = registry.cn-beijing.aliyuncs.com
IMAGE_NAME = livenowhy/adminer
STATUS = 已构建   # 状态: 已自动构建, 未构建

container:
	docker build -t ${PREFIX}/${IMAGE_NAME}:${TAG} .

push: container
	docker push ${PREFIX}/${IMAGE_NAME}:${TAG}

clean:
	docker rmi -f ${PREFIX}/${IMAGE_NAME}:${TAG} || true