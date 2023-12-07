FROM registry.cn-beijing.aliyuncs.com/livenowhy/centos:latest
LABEL description="基于官方 centos latest 制作的业务镜像"

RUN yum update -y && yum upgrade -y
RUN yum -y groupinstall "Development tools"

RUN yum install mysql-devel python-devel openldap-devel libevent-devel libxslt-devel libxml2-devel epel-release -y
RUN yum install bzip2-devel libffi-devel ncurses-devel unixODBC-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel -y
RUN yum install net-tools zlib psmisc wget make vim redis python-simplejson -y
RUN yum install python36 python36-devel MySQL-python -y

RUN mkdir /share
RUN wget https://bootstrap.pypa.io/pip/3.6/get-pip.py -O /share/get-pip.py
RUN python3.6 /share/get-pip.py
RUN rm -rf /share/get-pip.py

# docker 支持中文
RUN yum install kde-l10n-Chinese -y && yum update -y && yum upgrade -y && yum reinstall glibc-common -y && localedef -c -f UTF-8 -i zh_CN zh_CN.utf8
ENV LC_ALL zh_CN.UTF-8

RUN yum install libxml* uwsgi-plugin-python36 -y
RUN rm -rf /home/* && ln -sv /usr/lib64/uwsgi/python36_plugin.so /usr/lib64/uwsgi/python_plugin.so

# 设置包路径
RUN touch /usr/lib/python2.7/site-packages/my.pth && echo '/share' > /usr/lib/python2.7/site-packages/my.pth
RUN touch /usr/lib/python3.6/site-packages/my.pth && echo '/share' > /usr/lib/python3.6/site-packages/my.pth

# 配置 supervisor
RUN yum install supervisor -y
RUN echo_supervisord_conf > /etc/supervisord.conf
RUN echo '[include]' >> /etc/supervisord.conf && echo 'files = /etc/supervisord.d/*.ini' >> /etc/supervisord.conf
# RUN mkdir /etc/supervisord.d/ && mkdir /var/log/supervisor/
RUN supervisord -c /etc/supervisord.conf
RUN yum install -y crontabs
RUN yum update -y && yum clean all

RUN mkdir /root/.pip
COPY ./pip.conf /root/.pip/pip.conf

COPY ./requirements.txt /home/
RUN pip install -r /home/requirements.txt && rm -rf /home/*

# RUN pip install requests -i https://pypi.mirrors.ustc.edu.cn/simple/