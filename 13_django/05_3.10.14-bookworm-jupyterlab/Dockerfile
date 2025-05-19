FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-django

LABEL description="django jupyterlab 运行镜像; 基于 3.10.14-bookworm-django"

# 1. 代码补全
RUN pip install --no-cache-dir jupyterlab==4.2.5
RUN pip install --no-cache-dir jupyterlab-lsp==5.1.0
RUN pip install --no-cache-dir "python-lsp-server[all]"
ADD jupyter_lab_config.py      /root/.jupyter/jupyter_lab_config.py

# 2. superset; prophet -> superset 预测插件
RUN pip install --no-cache-dir apache-superset==4.0.0
RUN pip install --no-cache-dir vanna==0.5.5
RUN pip install --no-cache-dir prophet==1.1.5

# registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-jupyterlab