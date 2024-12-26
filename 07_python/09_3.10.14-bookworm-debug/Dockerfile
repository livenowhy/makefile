FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-ollama

LABEL description="django pycaret 运行镜像; 基于 3.10.14-bookworm-crewai"

# 1. other
RUN pip install --no-cache-dir django-redis==5.2.0
RUN pip install --no-cache-dir django-cors-headers==4.6.0
RUN pip install --no-cache-dir django-minio-backend==3.7.2

# registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-debug

# registry.cn-beijing.aliyuncs.com/livenowhy/minio:dev
# docker save -o minio_dev.tar registry.cn-beijing.aliyuncs.com/livenowhy/minio:dev