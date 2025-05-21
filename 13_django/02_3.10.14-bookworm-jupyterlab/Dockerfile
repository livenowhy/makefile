FROM registry.cn-beijing.aliyuncs.com/livenowhy/django:3.10.14-bookworm-5.0.8-django

LABEL description="django jupyterlab 运行镜像; 基于 3.10.14-bookworm-django"

RUN pip install --no-cache-dir jupyterlab
RUN pip install --no-cache-dir jupyterlab-lsp
RUN pip install --no-cache-dir "python-lsp-server[all]"

# 1. 代码补全
# RUN pip install --no-cache-dir jupyterlab==4.2.5
# RUN pip install --no-cache-dir jupyterlab-lsp==5.1.0
# RUN pip install --no-cache-dir "python-lsp-server[all]"
# ADD jupyter_lab_config.py      /root/.jupyter/jupyter_lab_config.py
