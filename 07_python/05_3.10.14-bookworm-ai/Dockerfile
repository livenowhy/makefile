FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-django

LABEL description="django ai 运行镜像; 基于 3.10.14-bookworm-django"

# 1. 代码补全
RUN pip install --no-cache-dir jupyterlab
RUN pip install --no-cache-dir jupyterlab-lsp
RUN pip install --no-cache-dir "python-lsp-server[all]"

# 2. crewai 配置
RUN pip install --no-cache-dir crewai
RUN pip install --no-cache-dir crewai-tools
RUN pip install --no-cache-dir duckduckgo_search
RUN pip install --no-cache-dir langchain
RUN curl -fsSL https://ollama.com/install.sh | sh
RUN pip install --no-cache-dir langchain-community

# 3. superset; prophet -> superset 预测插件
RUN pip install --no-cache-dir apache-superset==4.0.0
RUN pip install --no-cache-dir vanna==0.5.5
RUN pip install --no-cache-dir prophet

# 4. pycaret
RUN pip install --no-cache-dir pycaret==3.3.2
RUN pip install --no-cache-dir pycaret[full]
RUN pip install --no-cache-dir yapf
RUN pip install --no-cache-dir keras
RUN pip install --no-cache-dir keras-bert
RUN pip install --no-cache-dir tensorflow
RUN pip install --no-cache-dir hyperopt
RUN pip install --no-cache-dir vanna
RUN pip install --no-cache-dir 'shillelagh[all]'

ADD jupyter_lab_config.py      /root/.jupyter/jupyter_lab_config.py

# docker save -o python_crewai.tar registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-django-crewai
# sudo docker save -o python_basepip.tar registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-basepip