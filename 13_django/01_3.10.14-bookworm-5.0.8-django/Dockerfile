FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-codeserver

LABEL description="django 运行镜像; 基于 python:3.10.14-bookworm-codeserver"

# 1. django
RUN pip install --upgrade pip
RUN pip install --no-cache-dir django==5.2.1
RUN pip install --no-cache-dir djangorestframework==3.16.0
RUN pip install --no-cache-dir django-redis==5.4.0
RUN pip install --no-cache-dir django-cors-headers==4.7.0
RUN pip install --no-cache-dir django-minio-backend==3.8.0
RUN pip install --no-cache-dir pandas==2.2.3
RUN pip install --no-cache-dir celery==5.5.2
RUN pip install --no-cache-dir ipython==8.36.0
RUN pip install --no-cache-dir gunicorn==23.0.0
RUN pip install --no-cache-dir mlflow==2.22.0
RUN pip install --no-cache-dir redis==6.1.0
RUN pip install --no-cache-dir requests==2.32.3
RUN pip install --no-cache-dir pillow==11.2.1
RUN pip install --no-cache-dir PyMySQL==1.1.1
RUN pip install --no-cache-dir mysqlclient==2.2.7
RUN pip install --no-cache-dir asgiref==3.8.1
RUN pip install --no-cache-dir sqlparse==0.5.3
RUN pip install --no-cache-dir openpyxl==3.1.5
RUN pip install --no-cache-dir loguru==0.7.3
RUN pip install --no-cache-dir sqlalchemy==2.0.41
RUN pip install --no-cache-dir tornado==6.5
RUN pip install --no-cache-dir tzdata==2025.2
RUN pip install --no-cache-dir bs4==0.0.2
RUN pip install --no-cache-dir pytest==8.3.5
RUN pip install --no-cache-dir flower==2.0.1
RUN pip install --no-cache-dir flasgger==0.9.7.1
RUN pip install --no-cache-dir jieba==0.42.1
RUN pip install --no-cache-dir flake8==7.2.0
RUN pip install --no-cache-dir pyjwt==2.10.1

# 2. flask
RUN pip install --no-cache-dir Flask==3.1.1
RUN pip install --no-cache-dir Flask-AppBuilder
RUN pip install --no-cache-dir Flask-Cors
RUN pip install --no-cache-dir flask-restful-swagger-2


# 3. superset; prophet -> superset 预测插件
RUN pip install --no-cache-dir apache-superset==4.0.0
RUN pip install --no-cache-dir vanna==0.5.5
RUN pip install --no-cache-dir prophet==1.1.5