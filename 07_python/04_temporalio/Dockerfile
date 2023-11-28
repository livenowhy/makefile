FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10

RUN pip install --upgrade pip
ADD requirements.txt /home/requirements.txt
RUN pip install --no-cache-dir -r /home/requirements.txt

RUN mkdir -p /share/bin
ADD bin/mysqldump /share/bin/mysqldump

RUN chmod a+x /share/bin/mysqldump

# registry.cn-beijing.aliyuncs.com/livenowhy/python:temporalio