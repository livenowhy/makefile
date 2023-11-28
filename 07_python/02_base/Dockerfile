FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10

# 获取 gpg 公钥 (多次执行不会改变也不会影响)
RUN apt-get install dirmngr -y
RUN gpg --keyserver keyserver.ubuntu.com --recv-keys 0E98404D386FA1D9 F8D2585B8783D481 6ED0E7B82643E131 54404762BBB6E853 BDE6D2B9216EC7A8

# gpg --export --armor 0E98404D386FA1D9 > /etc/apt/trusted.gpg.d/0E98404D386FA1D9.gpg
# gpg --export --armor 0E98404D386FA1D9 F8D2585B8783D481 6ED0E7B82643E131 54404762BBB6E853 BDE6D2B9216EC7A8 | apt-key add -

# /etc/apt/trusted.gpg.d

RUN apt-get update
RUN apt-get install vim -y
RUN apt-get install build-essential -y
RUN apt-get install gcc -y
RUN apt-get install mariadb-server mariadb-client -y
RUN apt-get install python3-dev -y
RUN apt-get install manpages-dev -y
RUN apt-get install libsasl2-dev libldap2-dev libssl-dev -y

RUN yes | cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN pip install --upgrade pip
RUN mkdir /root/.pip
ADD pip.conf /root/.pip/

# 配置 supervisor
RUN pip3 install supervisor
RUN echo_supervisord_conf > /etc/supervisord.conf
RUN echo '[include]' >> /etc/supervisord.conf
RUN echo 'files = /etc/supervisord.d/*.ini' >> /etc/supervisord.conf
RUN mkdir /etc/supervisord.d/  && mkdir /var/log/supervisor/
RUN supervisord -c /etc/supervisord.conf

# 配置开发路径
RUN echo '/share/' >> '/usr/local/lib/python3.10/site-packages/my.pth'
