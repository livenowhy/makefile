FROM registry.cn-beijing.aliyuncs.com/livenowhy/node:10.22.0-buster-slim
LABEL description="gitbook镜像"

ARG VERSION=3.0.0
LABEL version=$VERSION
RUN npm install --global gitbook-cli
RUN gitbook fetch ${VERSION}

EXPOSE 4000 35729

# gitbook serve