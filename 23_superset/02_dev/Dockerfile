FROM registry.cn-beijing.aliyuncs.com/livenowhy/superset:lean

LABEL description="superset 镜像, 基于 superset 前置镜像"


ADD superset_config.py /usr/local/lib/python3.10/site-packages/superset/superset_config.py

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


# sduo docker save -o alpine.tar alpine:latest
# sudo docker save -o superset_lean.tar registry.cn-beijing.aliyuncs.com/livenowhy/superset:lean
# sudo docker save registry.cn-beijing.aliyuncs.com/livenowhy/superset:lean | gzip > superset_lean.tar.gz
