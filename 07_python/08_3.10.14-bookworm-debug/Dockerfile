FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-pycaret

LABEL description="django pycaret 运行镜像; 基于 3.10.14-bookworm-crewai"

# 1. ollama 
RUN curl -fsSL https://ollama.com/install.sh | sh

# 2. other
RUN pip install --no-cache-dir django-redis==5.2.0
RUN pip install --no-cache-dir django-cors-headers==4.6.0

# registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-debug
# docker save -o python_ai.tar registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-ai