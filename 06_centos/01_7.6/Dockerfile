FROM centos:latest
LABEL description="官方 centos latest"

RUN yes | cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN yum update -y && yum upgrade -y
RUN rm -rf /home/*

