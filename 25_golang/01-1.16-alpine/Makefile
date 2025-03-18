all: push

TAG = 1.16-alpine
PREFIX = registry.cn-beijing.aliyuncs.com
IMAGE_NAME = livenowhy/golang
STATUS = 已构建   # 状态: 已自动构建, 未构建

container:
	docker build -t ${PREFIX}/${IMAGE_NAME}:${TAG} .

push: container
	docker push ${PREFIX}/${IMAGE_NAME}:${TAG}

clean:
	docker rmi -f $(PREFIX):$(TAG) || true


# /25_golang/01-1.16-alpine/
# makefile
