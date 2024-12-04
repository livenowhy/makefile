FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-jupyterlab

LABEL description="django ai 运行镜像; 基于 3.10.14-bookworm-jupyterlab"


# 2. crewai 配置
RUN pip install --no-cache-dir crewai==0.51.1
RUN pip install --no-cache-dir crewai-tools==0.8.3
RUN pip install --no-cache-dir duckduckgo_search==6.2.12
RUN pip install --no-cache-dir langchain==0.2.14
RUN curl -fsSL https://ollama.com/install.sh | sh
RUN pip install --no-cache-dir langchain-community==0.2.12
RUN pip install --no-cache-dir ollama==0.4.1


# 4. pycaret
RUN pip install --no-cache-dir pycaret==3.3.2
RUN pip install --no-cache-dir pycaret[full]
RUN pip install --no-cache-dir yapf==0.40.2
RUN pip install --no-cache-dir keras==3.5.0
RUN pip install --no-cache-dir keras-bert==0.89.0
RUN pip install --no-cache-dir tensorflow==2.17.0
RUN pip install --no-cache-dir hyperopt==0.2.7
RUN pip install --no-cache-dir 'shillelagh[all]'

# 5. other
RUN pip install --no-cache-dir django-redis==5.2.0
RUN pip install --no-cache-dir django-cors-headers==4.6.0

# docker save -o python_ai.tar registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-ai