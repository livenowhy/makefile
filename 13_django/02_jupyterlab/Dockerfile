FROM registry.cn-beijing.aliyuncs.com/livenowhy/django:base

# 1. 代码补全
RUN pip install --no-cache-dir jupyterlab==4.4.2
RUN pip install --no-cache-dir jupyterlab-lsp==5.1.0
RUN pip install --no-cache-dir "python-lsp-server[all]"
ADD jupyter_lab_config.py      /root/.jupyter/jupyter_lab_config.py

