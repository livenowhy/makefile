FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10-alpine
LABEL description="基于官方 python 3.10-alpine 版本制作的开发镜像"

RUN apk add --update --no-cache curl jq py3-configobj py3-pip py3-setuptools python3 python3-dev
RUN apk add --no-cache gcc g++ jpeg-dev zlib-dev libc-dev libressl-dev musl-dev libffi-dev
RUN python -m pip install --upgrade pip
RUN apk del curl jq py3-configobj py3-pip py3-setuptools python3 python3-dev
RUN apk del gcc g++ jpeg-dev zlib-dev libc-dev libressl-dev musl-dev libffi-dev
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' > /etc/timezone
RUN rm -rf /var/cache/apk/*