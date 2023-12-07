FROM registry.cn-beijing.aliyuncs.com/livenowhy/redis:6.0
LABEL description="基于官方6.0基础镜像扩展的业务镜像"

COPY redis.conf /etc/redis/redis.conf
RUN chmod -R a+wr /etc/redis/redis.conf
CMD [ "redis-server", "/etc/redis/redis.conf" ]


