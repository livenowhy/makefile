FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-django

LABEL description="django crewai 运行镜像; 基于 3.10.14-bookworm-django"

# 1. crewai 配置
RUN pip install --no-cache-dir crewai
RUN pip install --no-cache-dir crewai-tools
RUN pip install --no-cache-dir duckduckgo_search
RUN pip install --no-cache-dir langchain
RUN curl -fsSL https://ollama.com/install.sh | sh
RUN pip install --no-cache-dir langchain-community



# 2. 代码补全
RUN pip install --no-cache-dir jupyterlab
RUN pip install --no-cache-dir jupyterlab-lsp
RUN pip install --no-cache-dir "python-lsp-server[all]"

# 3. base pip
RUN pip install --no-cache-dir apache-superset==4.0.0
RUN pip install --no-cache-dir vanna==0.5.5

# # superset 预测插件
RUN pip install --no-cache-dir prophet
RUN pip install --no-cache-dir yapf
#pycaret[full]
#keras
#keras-bert
#tensorflow
#hyperopt

# docker save -o python_crewai.tar registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-django-crewai