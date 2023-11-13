FROM docker.io/centos:centos7.6.1810

RUN yes | cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN yum update -y && yum upgrade -y
RUN rm -rf /home/*

# 已配置自动构建