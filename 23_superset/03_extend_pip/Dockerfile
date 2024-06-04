FROM registry.cn-beijing.aliyuncs.com/livenowhy/superset:basepip

LABEL description="superset pip 镜像, 基于 superset:basepip"

RUN pip install yapf flake8
RUN curl -fsSL https://code-server.dev/install.sh | sh

RUN code-server --install-extension ms-python.python
RUN code-server --install-extension EricSia.pythonsnippets3
RUN code-server --install-extension ms-toolsai.jupyter
RUN code-server --install-extension tht13.python
RUN code-server --install-extension magicstack.MagicPython
RUN code-server --install-extension Yseop.vscode-yseopml
RUN code-server --install-extension ecmel.vscode-html-css
RUN code-server --install-extension abusaidm.html-snippets

cweijan.vscode-mysql-client2

# RUN code-server --install-extension Kelvin.vscode-sshfs
# 启动命令: code-server