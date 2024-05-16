ARG PY_VER=3.10-slim-bookworm

FROM python:${PY_VER}

LABEL description="superset 镜像, 基于 3.10-slim-bookworm"

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
        libldap2-dev

RUN touch superset/static/version_info.json \
RUN chown -R superset:superset ./* \
RUN rm -rf /var/lib/apt/lists/*

# COPY --chown=superset:superset pyproject.toml setup.py MANIFEST.in README.md ./

# # setup.py uses the version information in package.json
# COPY --chown=superset:superset superset-frontend/package.json superset-frontend/
# COPY --chown=superset:superset requirements/base.txt requirements/
# RUN --mount=type=cache,target=/root/.cache/pip \
#     apt-get update && apt-get install -y --no-install-recommends \
#       build-essential \
#     && pip install --upgrade setuptools pip \
#     && pip install -r requirements/base.txt \
#     && apt-get autoremove -y --purge build-essential \
#     && rm -rf /var/lib/apt/lists/*

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
