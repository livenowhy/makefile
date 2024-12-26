FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-jupyterlab

LABEL description="django crewai 运行镜像; 基于 3.10.14-bookworm-jupyterlab"

# 1. crewai 配置
RUN pip install --no-cache-dir crewai==0.51.1
RUN pip install --no-cache-dir crewai-tools==0.8.3
RUN pip install --no-cache-dir duckduckgo_search==6.2.12
RUN pip install --no-cache-dir langchain==0.2.14
RUN pip install --no-cache-dir langchain-community==0.2.12
RUN pip install --no-cache-dir ollama==0.4.1

# 2. othen
RUN pip install --no-cache-dir django-redis==5.2.0
RUN pip install --no-cache-dir django-cors-headers==4.6.0
RUN pip install --no-cache-dir django-minio-backend==3.7.2

# registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-crewai