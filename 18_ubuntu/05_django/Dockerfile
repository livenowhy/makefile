FROM registry.cn-beijing.aliyuncs.com/livenowhy/ubuntu:develop

LABEL description="Make Ubuntu Development Environment (django)"

RUN python3 -m pip install --upgrade pip
RUN pip3 install django==4.2.2
RUN pip3 install mysqlclient==2.1.1
RUN pip3 install djangorestframework==3.14.0
RUN pip3 install asgiref==3.6.0
RUN pip3 install sqlparse==0.4.4
RUN pip3 install openpyxl==3.1.
RUN pip3 install loguru==0.7.2

ADD my.pth /usr/lib/python3/dist-packages/my.pth
EXPOSE 8011 8012 8013 8014 8015 8016 8017 8018 8019
ADD run.sh /root/run.sh
ENTRYPOINT ["/bin/bash", "/root/run.sh"]