FROM centos:7.6.1810
LABEL description="官方 centos 7.6.1810"

RUN yes | cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN yum update -y && yum upgrade -y
RUN rm -rf /home/*

