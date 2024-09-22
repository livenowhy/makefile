FROM registry.cn-beijing.aliyuncs.com/livenowhy/node:20.16.0-bookworm
LABEL description="node vue 镜像 基于 node:20.16.0-bookworm"

RUN /bin/sh -c set -ex; apt-get update; apt-get install -y --no-install-recommends vim ; rm -rf /var/lib/apt/lists/*

RUN mkdir /share && mkdir /share/modules
WORKDIR /share
RUN npm install -g pnpm
RUN npm install -g @vue/cli
RUN pnpm config set registry https://registry.npmmirror.com

ADD package.json /share/modules/package.json
RUN cd /share/modules && pnpm install

EXPOSE 9001 9002 9003 9004 9005 9006 9007 9008 9009 9010

ADD run-server.sh /share/run-server.sh

CMD ["/share/run-server.sh"]

# registry.cn-beijing.aliyuncs.com/livenowhy/node:20.16.0-bookworm-vue
