FROM registry.cn-beijing.aliyuncs.com/livenowhy/ubuntu:develop

LABEL description="Make Ubuntu Development Environment (python)"

RUN python3 -m pip install --upgrade pip
RUN pip3 install django==4.2.2
RUN pip3 install mysqlclient==2.1.1
RUN pip3 install djangorestframework==3.14.0
RUN pip3 install asgiref==3.6.0
RUN pip3 install sqlparse==0.4.4
RUN pip3 install openpyxl==3.1.2
RUN pip3 install loguru==0.7.2
RUN pip3 install requests==2.31.0
RUN pip3 install pandas==2.1.3
RUN pip3 install sqlalchemy==2.0.23
RUN pip3 install tornado==6.3.3
RUN pip3 install ipython==8.18.0
RUN pip3 install tzdata==2024.1

ADD my.pth /usr/lib/python3/dist-packages/my.pth

RUN pip3 install supervisor
RUN echo_supervisord_conf > /etc/supervisord.conf
RUN echo '[include]' >> /etc/supervisord.conf
RUN echo 'files = /etc/supervisord.d/*.ini' >> /etc/supervisord.conf
RUN mkdir /etc/supervisord.d/
RUN mkdir /var/log/supervisor/
ADD django.ini /etc/supervisor/conf.d/django.ini
RUN supervisord -c /etc/supervisord.conf


EXPOSE 8000 8001 8002 8003 8004 8005 8006 8007 8008
ADD run.sh /root/run.sh
ENTRYPOINT ["/bin/bash", "/root/run.sh"]

# docker-compose stop && docker-compose rm -f