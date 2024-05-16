FROM python:3.10.14-bookworm

LABEL description="superset 镜像, 基于 3.10.14-bookworm"

RUN apt-get update

RUN apt-get install -y --no-install-recommends curl
RUN apt-get install -y --no-install-recommends default-libmysqlclient-dev
RUN apt-get install -y --no-install-recommends libsasl2-dev
RUN apt-get install -y --no-install-recommends libsasl2-modules-gssapi-mit
RUN apt-get install -y --no-install-recommends libpq-dev
RUN apt-get install -y --no-install-recommends libecpg-dev
RUN apt-get install -y --no-install-recommends libldap2-dev
RUN apt-get install -y --no-install-recommends build-essential
RUN apt-get install -y --no-install-recommends vim
RUN pip install --upgrade setuptools pip
RUN pip install apache-superset==4.0.0
RUN pip install mysqlclient
RUN pip install Pillow
# RUN apt-get autoremove -y --purge build-essential
# RUN rm -rf /var/lib/apt/lists/*

COPY superset_config.py /usr/local/lib/python3.10/site-packages/superset/superset_config.py

RUN echo "export SUPERSET_CONFIG_PATH=/usr/local/lib/python3.10/site-packages/superset/superset_config.py" >> /etc/profile
RUN source /etc/profile

WORKDIR /app
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    FLASK_APP="superset.app:create_app()" \
    SUPERSET_PORT=8088

EXPOSE ${SUPERSET_PORT}

# # 1. 初始化数据
# RUN superset db upgrade

# # 2. 创建超级管理员
# RUN superset fab create-admin --username admin --firstname Superset --lastname Admin --email admin@superset.com --password admin

# # 3. 初始化
# RUN superset init

# HEALTHCHECK CMD curl -f "http://localhost:${SUPERSET_PORT}/health"

# CMD ["/usr/bin/run-server.sh"]
