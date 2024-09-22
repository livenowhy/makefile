FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-flask

LABEL description="crewai 镜像, 基于 python:3.10.14-bookworm-flask"

RUN pip install --no-cache-dir crewai
RUN pip install --no-cache-dir duckduckgo_search
RUN pip install --no-cache-dir langchain
RUN curl -fsSL https://ollama.com/install.sh | sh
RUN pip install --no-cache-dir langchain-community


# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  jupyterlab-kite