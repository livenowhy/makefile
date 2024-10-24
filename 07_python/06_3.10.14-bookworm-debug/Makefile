all: push

TAG = 3.10.14-bookworm-debug
PREFIX = registry.cn-beijing.aliyuncs.com
IMAGE_NAME = livenowhy/python
STATUS = 已构建   # 状态: 已自动构建, 未构建
SAVE_NAME = python-3.10.14-bookworm-debug

CONTAINER_NAME = superset

container:
	docker build -t ${PREFIX}/${IMAGE_NAME}:${TAG} .

push: container
	docker push ${PREFIX}/${IMAGE_NAME}:${TAG}

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


save:
	docker save -o ${SAVE_NAME}.tar ${PREFIX}/${IMAGE_NAME}:${TAG}