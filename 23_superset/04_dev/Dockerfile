FROM registry.cn-beijing.aliyuncs.com/livenowhy/superset:extendpip

LABEL description="superset 镜像, 基于 superset 前置镜像"

WORKDIR /app

# jupyter 扩展
RUN mkdir -p /usr/local/lib/python3.10/site-packages/superset/jupyterlab/
ADD extend/initialization__init__.py  /usr/local/lib/python3.10/site-packages/superset/initialization/__init__.py
ADD extend/jupyterlab.html            /usr/local/lib/python3.10/site-packages/superset/templates/jupyterlab.html
ADD extend/views_extend.py            /usr/local/lib/python3.10/site-packages/superset/views/extend.py
ADD extend/views__init__.py           /usr/local/lib/python3.10/site-packages/superset/views/__init__.py
ADD extend/models_extend.py           /usr/local/lib/python3.10/site-packages/superset/models/extend.py
ADD extend/models__init__.py          /usr/local/lib/python3.10/site-packages/superset/models/__init__.py
ADD extend/jupyter_lab_config.py      /root/.jupyter/jupyter_lab_config.py
ADD extend/config.yaml                /root/.config/code-server/config.yaml
ADD extend/jupyter_lab_config.py      /usr/local/lib/python3.10/site-packages/superset/jupyterlab/jupyter_lab_config.py
ADD extend/superset_config.py         /usr/local/lib/python3.10/site-packages/superset/superset_config.py

RUN mkdir -p /usr/local/lib/python3.10/site-packages/superset/static/assets/images/matplotlib

EXPOSE 8088
EXPOSE 8888
EXPOSE 8080
EXPOSE 8081
EXPOSE 8082
EXPOSE 8083
EXPOSE 8084
EXPOSE 8085
EXPOSE 8086
EXPOSE 8087

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV FLASK_APP="superset.app:create_app()"
ENV FLASK_AP=superset
ENV SUPERSET_CONFIG_PATH=/usr/local/lib/python3.10/site-packages/superset/superset_config.py

RUN superset init

CMD ["/app/run-server.sh"]
# ENTRYPOINT ["/bin/bash", "/app/run-server.sh"]
# sudo docker save -o superset_dev.tar registry.cn-beijing.aliyuncs.com/livenowhy/superset:dev