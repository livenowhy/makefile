FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-codeserver

LABEL description="django 运行镜像; 基于 python:3.10.14-bookworm-codeserver"

# 1. django 普通配置
RUN pip install --upgrade pip
RUN pip install --no-cache-dir django==5.0.8
RUN pip install --no-cache-dir djangorestframework
RUN pip install --no-cache-dir django-redis
RUN pip install --no-cache-dir django-cors-headers
RUN pip install --no-cache-dir django-minio-backend
RUN pip install --no-cache-dir pandas
RUN pip install --no-cache-dir celery
RUN pip install --no-cache-dir ipython
RUN pip install --no-cache-dir gunicorn
RUN pip install --no-cache-dir mlflow
RUN pip install --no-cache-dir redis
RUN pip install --no-cache-dir requests
RUN pip install --no-cache-dir pillow
RUN pip install --no-cache-dir PyMySQL
RUN pip install --no-cache-dir mysqlclient
RUN pip install --no-cache-dir asgiref
RUN pip install --no-cache-dir sqlparse
RUN pip install --no-cache-dir openpyxl
RUN pip install --no-cache-dir loguru
RUN pip install --no-cache-dir sqlalchemy
RUN pip install --no-cache-dir tornado
RUN pip install --no-cache-dir tzdata
RUN pip install --no-cache-dir bs4
RUN pip install --no-cache-dir pytest
RUN pip install --no-cache-dir flower
RUN pip install --no-cache-dir flasgger
RUN pip install --no-cache-dir jieba
RUN pip install --no-cache-dir flake8

# RUN pip install --no-cache-dir pandas==2.1.4
# RUN pip install --no-cache-dir celery==5.4.0
# RUN pip install --no-cache-dir ipython==8.26.0
# RUN pip install --no-cache-dir gunicorn==22.0.0
# RUN pip install --no-cache-dir mlflow==2.14.1
# RUN pip install --no-cache-dir redis==5.0.7
# RUN pip install --no-cache-dir requests==2.32.3
# RUN pip install --no-cache-dir pillow==10.3.0
# RUN pip install --no-cache-dir PyMySQL==1.1.1
# RUN pip install --no-cache-dir mysqlclient==2.2.4
# RUN pip install --no-cache-dir asgiref==3.6.0
# RUN pip install --no-cache-dir django==4.2
# RUN pip install --no-cache-dir sqlparse==0.4.4
# RUN pip install --no-cache-dir openpyxl==3.1.2
# RUN pip install --no-cache-dir djangorestframework==3.14.0
# RUN pip install --no-cache-dir loguru==0.7.2
# RUN pip install --no-cache-dir sqlalchemy==2.0.23
# RUN pip install --no-cache-dir tornado==6.3.3
# RUN pip install --no-cache-dir tzdata==2024.1
# RUN pip install --no-cache-dir bs4==0.0.2
# RUN pip install --no-cache-dir pytest==8.3.2
# RUN pip install --no-cache-dir flower
# RUN pip install --no-cache-dir flasgger
# RUN pip install --no-cache-dir flake
# RUN pip install --no-cache-dir django-redis==5.2.0
# RUN pip install --no-cache-dir django-cors-headers==4.6.0
# RUN pip install --no-cache-dir django-minio-backend==3.7.2

# # 2. flask
# RUN pip install --no-cache-dir Flask==2.3.3
# RUN pip install --no-cache-dir Flask-AppBuilder==4.5.0
# RUN pip install --no-cache-dir Flask-Cors==4.0.1
# RUN pip install --no-cache-dir flask-restful-swagger-2
# # 2. othen
# RUN pip install --no-cache-dir django-redis==5.2.0
# RUN pip install --no-cache-dir django-cors-headers==4.6.0
# RUN pip install --no-cache-dir django-minio-backend==3.7.2