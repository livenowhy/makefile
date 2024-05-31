FROM registry.cn-beijing.aliyuncs.com/livenowhy/superset:extendpip

LABEL description="superset 镜像, 基于 superset 前置镜像"

WORKDIR /app

# jupyter 扩展
ADD extend/initialization__init__.py /usr/local/lib/python3.10/site-packages/superset/initialization/__init__.py
ADD extend/jupyterlab.html /usr/local/lib/python3.10/site-packages/superset/templates/jupyterlab.html
ADD extend/views_extend.py /usr/local/lib/python3.10/site-packages/superset/views/extend.py
ADD extend/views__init__.py /usr/local/lib/python3.10/site-packages/superset/views/__init__.py
ADD extend/models_extend.py /usr/local/lib/python3.10/site-packages/superset/models/extend.py
ADD extend/models__init__.py /usr/local/lib/python3.10/site-packages/superset/models/__init__.py


- /share/makefile/23_superset/03_dev/jupyter_lab_config.py:/root/.jupyter/jupyter_lab_config.py
- /share/makefile/23_superset/03_dev/jupyter_lab_config.py:/usr/local/lib/python3.10/site-packages/superset/jupyterlab/jupyter_lab_config.py


ADD superset_config.py /usr/local/lib/python3.10/site-packages/superset/superset_config.py
RUN mkdir -p /usr/local/lib/python3.10/site-packages/superset/static/assets/images/matplotlib
EXPOSE 8088
EXPOSE 8888

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV FLASK_APP="superset.app:create_app()" 

ENV FLASK_AP=superset
ENV SUPERSET_CONFIG_PATH=/usr/local/lib/python3.10/site-packages/superset/superset_config.py
RUN superset superset init
RUN mkdir -p /usr/local/lib/python3.10/site-packages/superset/jupyterlab/

COPY --chmod=755 gunicore_superset.sh /app/gunicore_superset.sh
COPY --chmod=755 run-server.sh        /app/run-server.sh

CMD ["/app/run-server.sh"]


# ADD django.ini /etc/supervisord.d/django.ini
# ADD run.sh /root/run.sh
# ENTRYPOINT ["/bin/bash", "/root/run.sh"]

# sduo docker save -o alpine.tar alpine:latest
# sudo docker save -o superset_lean.tar registry.cn-beijing.aliyuncs.com/livenowhy/superset:lean
# sudo docker save registry.cn-beijing.aliyuncs.com/livenowhy/superset:lean | gzip > superset_lean.tar.gz
