FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-django

LABEL description="django crewai 运行镜像; 基于 3.10.14-bookworm-django"

# 1. crewai 配置
RUN pip install --no-cache-dir crewai
RUN pip install --no-cache-dir crewai-tools
RUN pip install --no-cache-dir duckduckgo_search
RUN pip install --no-cache-dir langchain
RUN curl -fsSL https://ollama.com/install.sh | sh
RUN pip install --no-cache-dir langchain-community

# RUN pip install django-celery
# RUN pip install django-redis

# docker save -o python_crewai.tar registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-django-crewai