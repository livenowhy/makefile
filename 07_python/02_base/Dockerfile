FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:latest

RUN echo '/share/' >> '/usr/local/lib/python3.10/site-packages/my.pth'
RUN apt install mariadb-server mariadb-client -y
RUN pip install --upgrade pip
RUN apt install python3-dev python-dev -y
RUN apt install build-essential gcc -y
RUN apt update
RUN apt install manpages-dev -y
RUN apt install libsasl2-dev libldap2-dev libssl-dev -y