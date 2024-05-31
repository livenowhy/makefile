FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm

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
RUN apt-get install -y --no-install-recommends npm

# RUN apt-get autoremove -y --purge build-essential
# RUN rm -rf /var/lib/apt/lists/*


# /23_superset/01_lean/
