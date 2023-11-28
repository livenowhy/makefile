FROM registry.cn-beijing.aliyuncs.com/livenowhy/ubuntu:22.04

LABEL description="Make Ubuntu Development Environment"

RUN apt-get update -y && apt-get upgrade -y

RUN apt-get install passwd openssl openssh-server openssh-client -y
RUN apt-get install gcc curl vim git curl zip rar -y
RUN apt-get install python3-pip python3-dev default-libmysqlclient-dev build-essential -y
RUN apt-get install mariadb-server mariadb-client -y
RUN apt-get install manpages-dev -y
RUN apt-get install libsasl2-dev libldap2-dev libssl-dev -y


RUN pip3 install --upgrade pip
RUN mkdir /root/.ssh
RUN ssh-keygen -q -t rsa -b 4096 -C "docker-develop@livenowhy.com" -N '' -f /root/.ssh/id_rsa