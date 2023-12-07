FROM registry.cn-beijing.aliyuncs.com/livenowhy/mysql:5.6
LABEL description="基于官方5.6基础镜像扩展的业务镜像"

WORKDIR /tmp
ADD default.sql r.sql
ADD mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf
ADD docker-entrypoint.sh /entrypoint.sh
RUN chmod u+x /entrypoint.sh 

