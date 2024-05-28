FROM registry.cn-beijing.aliyuncs.com/livenowhy/superset:lean

LABEL description="superset pip 镜像, 基于 superset:lean"

RUN pip install --upgrade setuptools pip
RUN pip install apache-superset==4.0.0
RUN pip install vanna==0.5.5

RUN pip install mysqlclient
RUN pip install Pillow
RUN pip install flask_cors


RUN pip install jupyterlab
RUN pip install PyMySQL

# 预测插件
RUN pip install prophet



WORKDIR /app
