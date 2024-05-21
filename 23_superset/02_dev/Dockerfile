FROM registry.cn-beijing.aliyuncs.com/livenowhy/superset:lean

LABEL description="superset 镜像, 基于 superset 前置镜像"

ADD superset_config.py /usr/local/lib/python3.10/site-packages/superset/superset_config.py
ADD gunicore_superset.sh /app/gunicore_superset.sh