FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-dev

LABEL description="code server镜像, 基于 python:3.10.14-bookworm-dev"

# 1. 安装 code-server 
COPY install_code_server.sh    /share/install_code_server.sh
RUN chmod +x /share/install_code_server.sh  &&  /share/install_code_server.sh

#!/bin/sh
RUN code-server --install-extension ms-python.python
RUN code-server --install-extension EricSia.pythonsnippets3
RUN code-server --install-extension ms-toolsai.jupyter
RUN code-server --install-extension tht13.python
RUN code-server --install-extension magicstack.MagicPython
RUN code-server --install-extension Yseop.vscode-yseopml
RUN code-server --install-extension ecmel.vscode-html-css
RUN code-server --install-extension abusaidm.html-snippets

ADD config.yaml /root/.config/code-server/config.yaml