FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-dev

LABEL description="flask 运行镜像; 基于 python:3.10.14-bookworm-dev"

RUN pip install --no-cache-dir Flask==2.3.3
RUN pip install --no-cache-dir Flask-AppBuilder==4.5.0
RUN pip install --no-cache-dir Flask-Cors==4.0.1
RUN pip install --no-cache-dir celery==5.4.0
RUN pip install --no-cache-dir ipython==8.26.0
RUN pip install --no-cache-dir gunicorn==22.0.0
RUN pip install --no-cache-dir pandas==2.1.4
RUN pip install --no-cache-dir mlflow==2.14.1
RUN pip install --no-cache-dir redis==5.0.7
RUN pip install --no-cache-dir requests==2.32.3
RUN pip install --no-cache-dir pycaret==3.3.2
RUN pip install --no-cache-dir pillow==10.3.0
RUN pip install --no-cache-dir flower
RUN pip install --no-cache-dir flasgger
RUN pip install --no-cache-dir flask-restful-swagger-2
RUN pip install --no-cache-dir PyMySQL
RUN pip install --no-cache-dir mysqlclient

RUN apt-get autoremove -y --purge build-essential
RUN rm -rf /var/lib/apt/lists/*

# registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-flask