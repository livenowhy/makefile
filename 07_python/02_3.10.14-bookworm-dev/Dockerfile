FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm

LABEL description="3.10.14-bookworm dev 开发环境, 基于 python:3.10.14-bookworm"

RUN apt-get update                                                      && \
apt-get install -y --no-install-recommends sudo                         && \
apt-get install -y --no-install-recommends curl                         && \
apt-get install -y --no-install-recommends default-libmysqlclient-dev   && \
apt-get install -y --no-install-recommends libsasl2-dev                 && \
apt-get install -y --no-install-recommends libsasl2-modules-gssapi-mit  && \
apt-get install -y --no-install-recommends libpq-dev                    && \
apt-get install -y --no-install-recommends libecpg-dev                  && \
apt-get install -y --no-install-recommends libldap2-dev                 && \
apt-get install -y --no-install-recommends build-essential              && \
apt-get install -y --no-install-recommends vim                          && \
apt-get install -y --no-install-recommends npm                          && \
apt-get install -y --no-install-recommends openssh-server

RUN pip install --upgrade setuptools pip

# 1. supervisor 管理服务
RUN pip3 install supervisor
RUN echo_supervisord_conf > /etc/supervisord.conf
RUN echo '[include]' >> /etc/supervisord.conf && echo 'files = /etc/supervisord.d/*.ini' >> /etc/supervisord.conf
RUN mkdir /etc/supervisord.d/ && mkdir /var/log/supervisor/

# 2. 设置运行路径
WORKDIR /share
RUN echo '/share' >> /usr/local/lib/python3.10/site-packages/my.pth
ADD run-server.sh    /share/run-server.sh
CMD ["/share/run-server.sh"]

# 3. 后期 ssh 登陆
RUN mkdir -p /root/.ssh/
RUN echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config
RUN echo "AuthorizedKeysFile .ssh/authorized_keys" >> /etc/ssh/sshd_config
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

# 4. EXPOSE 暴露端口
EXPOSE 22 80
EXPOSE 8888 8080 
EXPOSE 8081 8082 8083 8084 8085 8086 8087 8088 8089 8090
EXPOSE 8091 8092 8093 8094 8095 8096 8097 8098 8099 8100
EXPOSE 9000 9001 9002 9003 9004 9005 9006 9007 9008 9009
EXPOSE 9010 9011 9012 9013 9014 9015 9016 9017 9018 9019

# RUN apt-get autoremove -y --purge build-essential
# RUN rm -rf /var/lib/apt/lists/*