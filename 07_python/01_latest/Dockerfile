FROM python:latest

RUN apt-get update
RUN apt-get install vim -y
RUN yes | cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN pip install --upgrade pip
RUN mkdir /root/.pip
ADD pip.conf /root/.pip/

RUN pip3 install supervisor
RUN echo_supervisord_conf > /etc/supervisord.conf
RUN echo '[include]' >> /etc/supervisord.conf
RUN echo 'files = /etc/supervisord.d/*.ini' >> /etc/supervisord.conf
RUN mkdir /etc/supervisord.d/
RUN mkdir /var/log/supervisor/
RUN supervisord -c /etc/supervisord.conf