ARG PY_VER=3.10-slim-bookworm

FROM python:${PY_VER}

LABEL description="superset 镜像, 基于 3.10-slim-bookworm"

RUN mkdir -p /app
WORKDIR /app
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    SUPERSET_ENV=production \
    FLASK_APP="superset.app:create_app()" \
    PYTHONPATH="/app/pythonpath" \
    SUPERSET_HOME="/app/superset_home" \
    SUPERSET_PORT=8088

RUN mkdir -p ${PYTHONPATH} superset/static requirements superset-frontend apache_superset.egg-info requirements
RUN useradd --user-group -d ${SUPERSET_HOME} -m --no-log-init --shell /bin/bash superset
RUN apt-get update

RUN apt-get install -y --no-install-recommends \
        curl \
        default-libmysqlclient-dev \
        libsasl2-dev \
        libsasl2-modules-gssapi-mit \
        libpq-dev \
        libecpg-dev \
        libldap2-dev \
        build-essential

RUN pip install --upgrade setuptools pip

RUN pip install apache-superset==4.0.0

RUN apt-get autoremove -y --purge build-essential
RUN rm -rf /var/lib/apt/lists/*

COPY --chown=superset:superset superset_config.py /usr/local/lib/python3.10/site-packages/superset/superset_config.py


# 从 node 镜像中把构建产物 copy 出来
# COPY --chown=superset:superset --from=superset-node /app/superset/static/assets superset/static/assets
# ## Lastly, let's install superset itself
# COPY --chown=superset:superset superset superset
# RUN --mount=type=cache,target=/root/.cache/pip \
#     pip install -e . \
#     && flask fab babel-compile --target superset/translations \
#     && chown -R superset:superset superset/translations

# COPY --chmod=755 ./docker/run-server.sh /usr/bin/
# USER superset

# HEALTHCHECK CMD curl -f "http://localhost:${SUPERSET_PORT}/health"

# EXPOSE ${SUPERSET_PORT}

# CMD ["/usr/bin/run-server.sh"]
