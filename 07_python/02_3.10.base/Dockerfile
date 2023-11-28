FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10

# 安装基本开发包
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install vim gcc -y
RUN apt-get install build-essential -y
RUN apt-get install mariadb-server mariadb-client -y
RUN apt-get install python3-dev -y
RUN apt-get install manpages-dev -y
RUN apt-get install libsasl2-dev libldap2-dev libssl-dev -y
RUN pip install --upgrade pip

# 修改配置
RUN yes | cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
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
