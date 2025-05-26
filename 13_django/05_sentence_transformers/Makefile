all: push

TAG = sentence_transformers
PREFIX = registry.cn-beijing.aliyuncs.com
IMAGE_NAME = livenowhy/django
STATUS = 已构建   # 状态: 已自动构建, 未构建

OPEN_IMAGE = registry.cn-beijing.aliyuncs.com/oopen/django:debug

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


gitpush:
	git add .
	git commit -m "..."
	git push origin superset

# docker pull registry.cn-beijing.aliyuncs.com/oopen/django:debug
# docker save -o ai_debug.tar registry.cn-beijing.aliyuncs.com/oopen/django:debug