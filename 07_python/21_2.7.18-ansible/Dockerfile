FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:2.7.18

RUN apt-get update
RUN apt-get install sshpass -y
RUN apt-get install telnet -y
RUN pip install --upgrade pip
RUN pip install --no-cache-dir ansible
RUN pip install --no-cache-dir ansible-core
