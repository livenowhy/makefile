all: push

TAG = 3.10.14-bookworm-debug
PREFIX = registry.cn-beijing.aliyuncs.com
IMAGE_NAME = livenowhy/python
STATUS = 已构建   # 状态: 已自动构建, 未构建

CONTAINER_NAME = superset
OPEN_IMAGE = registry.cn-beijing.aliyuncs.com/oopen/python:3.10.14-bookworm-debug


# docker tag registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-debug registry.cn-beijing.aliyuncs.com/oopen/python:3.10.14-bookworm-debug
 

container:
	docker build -t ${PREFIX}/${IMAGE_NAME}:${TAG} .
	docker tag ${PREFIX}/${IMAGE_NAME}:${TAG} ${OPEN_IMAGE}
 
push: container
	docker push ${PREFIX}/${IMAGE_NAME}:${TAG}
	docker push ${OPEN_IMAGE}

pull: 
	docker pull ${PREFIX}/${IMAGE_NAME}:${TAG}

clean:
	docker rmi -f $(PREFIX):$(TAG) || true

run: rm pull
	docker run --name=${CONTAINER_NAME} -d -p 9088:8088 ${PREFIX}/${IMAGE_NAME}:${TAG}

stop:
	docker stop ${CONTAINER_NAME} || true

rm: stop
	docker rm -f ${CONTAINER_NAME} || true

gitpush:
	git add .
	git commit -m "..."
	git push origin superset