FROM python:3.8

RUN apt-get update
RUN apt-get install vim -y
RUN yes | cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN pip install --upgrade pip
RUN mkdir /root/.pip
ADD pip.conf /root/.pip/
RUN git clone https://github.com/imClumsyPanda/langchain-ChatGLM.git