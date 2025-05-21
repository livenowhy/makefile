FROM registry.cn-beijing.aliyuncs.com/livenowhy/django:base

LABEL description="django jupyterlab 运行镜像; 基于 3.10.14-bookworm-django base"

# 1. 代码补全
RUN pip install --no-cache-dir jupyterlab==4.4.2
RUN pip install --no-cache-dir jupyterlab-lsp==5.1.0
RUN pip install --no-cache-dir "python-lsp-server[all]"
ADD jupyter_lab_config.py      /root/.jupyter/jupyter_lab_config.py

# 2. superset; prophet -> superset 预测插件
# RUN pip install --no-cache-dir apache-superset==4.1.2
# RUN pip install --no-cache-dir vanna==0.7.9
# RUN pip install --no-cache-dir prophet==1.1.6


# # 2. flask
# # superset 要求 Flask 版本
# RUN pip install --no-cache-dir Flask==2.3.3
# RUN pip install --no-cache-dir Flask-AppBuilder==4.6.4
# RUN pip install --no-cache-dir Flask-Cors==6.0.0
# RUN pip install --no-cache-dir flask-restful-swagger-2==0.35


