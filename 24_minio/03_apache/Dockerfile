FROM registry.cn-beijing.aliyuncs.com/livenowhy/alpine:3.16
LABEL description="minio apache 版本 可以商业用"

RUN echo 'Etc/UTC' >/etc/timezone

RUN mkdir /data
ADD minio /bin/minio
RUN chmod a+x /bin/minio

CMD [ "/bin/minio", "server", "/data"]

# export MINIO_ROOT_USER=admin
# export MINIO_ROOT_PASSWORD=admin123
# chmod +x minio
# ./minio server /data