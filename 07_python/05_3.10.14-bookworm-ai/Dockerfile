FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-django

LABEL description="django ai 运行镜像; 基于 3.10.14-bookworm-django"

# 1. 代码补全
RUN pip install --no-cache-dir jupyterlab==4.2.5
RUN pip install --no-cache-dir jupyterlab-lsp==5.1.0
RUN pip install --no-cache-dir "python-lsp-server[all]"

# 2. crewai 配置
RUN pip install --no-cache-dir crewai==0.51.1
RUN pip install --no-cache-dir crewai-tools==0.8.3
RUN pip install --no-cache-dir duckduckgo_search==6.2.12
RUN pip install --no-cache-dir langchain==0.2.14
RUN curl -fsSL https://ollama.com/install.sh | sh
RUN pip install --no-cache-dir langchain-community==0.2.12
RUN pip install --no-cache-dir ollama==0.4.1

# 3. superset; prophet -> superset 预测插件
RUN pip install --no-cache-dir apache-superset==4.0.0
RUN pip install --no-cache-dir vanna==0.5.5
RUN pip install --no-cache-dir prophet==1.1.5

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

ADD jupyter_lab_config.py      /root/.jupyter/jupyter_lab_config.py

# docker save -o python_crewai.tar registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-django-crewai