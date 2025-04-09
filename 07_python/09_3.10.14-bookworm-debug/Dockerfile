FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-pycaret

LABEL description="django pycaret 运行镜像; 基于 3.10.14-bookworm-crewai"

# 1. other
RUN pip install --no-cache-dir django-redis==5.2.0
RUN pip install --no-cache-dir django-cors-headers==4.6.0
RUN pip install --no-cache-dir django-minio-backend==3.7.2
RUN pip install --no-cache-dir sentence-transformers==4.0.2
RUN pip install --no-cache-dir chardet==5.0.0

RUN apt-get autoremove -y --purge build-essential
RUN rm -rf /var/lib/apt/lists/*

# docker save -o ai_debug.tar registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-debug