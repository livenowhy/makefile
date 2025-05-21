FROM registry.cn-beijing.aliyuncs.com/livenowhy/django:3.10.14-bookworm-jupyterlab

LABEL description="django crewai 运行镜像; 基于 3.10.14-bookworm-jupyterlab"

# 1. crewai 配置
RUN pip install --no-cache-dir crewai
RUN pip install --no-cache-dir crewai-tools
RUN pip install --no-cache-dir duckduckgo_search
RUN pip install --no-cache-dir langchain
RUN pip install --no-cache-dir langchain-community
RUN pip install --no-cache-dir ollama
RUN pip install --no-cache-dir pymilvus

# # 1. crewai 配置
# RUN pip install --no-cache-dir crewai==0.51.1
# RUN pip install --no-cache-dir crewai-tools==0.8.3
# RUN pip install --no-cache-dir duckduckgo_search==6.2.12
# RUN pip install --no-cache-dir langchain==0.2.14
# RUN pip install --no-cache-dir langchain-community==0.2.12
# RUN pip install --no-cache-dir ollama==0.4.1
# RUN pip install --no-cache-dir pymilvus==2.5.6