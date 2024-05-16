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

COPY superset_config.py /usr/local/lib/python3.10/site-packages/superset/superset_config.py

# RUN apt-get autoremove -y --purge build-essential
# RUN rm -rf /var/lib/apt/lists/*


WORKDIR /app
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    FLASK_APP="superset.app:create_app()" \
    SUPERSET_PORT=8088

EXPOSE ${SUPERSET_PORT}

# sudo apt-get install -y   python-pip  python-dev-is-python3

#         RUN mkdir -p ${PYTHONPATH} superset/static requirements superset-frontend apache_superset.egg-info requirements
#         RUN useradd --user-group -d ${SUPERSET_HOME} -m --no-log-init --shell /bin/bash superset

# 


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
