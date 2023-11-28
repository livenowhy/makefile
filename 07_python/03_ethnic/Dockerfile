FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10

ADD requirements.txt /home/requirements.txt
RUN pip install --no-cache-dir -r /home/requirements.txt

RUN pip install oss2
RUN mkdir -p /share/bin
ADD bin/mysqldump /share/bin/mysqldump

RUN chmod a+x /share/bin/mysqldump
