FROM registry.cn-beijing.aliyuncs.com/livenowhy/redis:6.0

LABEL description="redis 6.0"

COPY redis.conf /etc/redis/redis.conf
RUN chmod -R a+wr /etc/redis/redis.conf
CMD [ "redis-server", "/etc/redis/redis.conf" ]


# 已配置自动构建