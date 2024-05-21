FROM registry.cn-beijing.aliyuncs.com/livenowhy/superset:lean

LABEL description="superset 镜像, 基于 superset 前置镜像"

ADD superset_config.py /usr/local/lib/python3.10/site-packages/superset/superset_config.py

#ADD gunicore_superset.sh /app/gunicore_superset.sh

ENV FLASK_AP=superset
ENV SUPERSET_CONFIG_PATH=/usr/local/lib/python3.10/site-packages/superset/superset_config.py
RUN superset superset init
COPY --chmod=755 gunicore_superset.sh /app/gunicore_superset.sh
CMD ["/app/gunicore_superset.sh", "start"]
