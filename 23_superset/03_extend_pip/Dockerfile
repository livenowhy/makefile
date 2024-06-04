FROM registry.cn-beijing.aliyuncs.com/livenowhy/superset:basepip

LABEL description="superset pip 镜像, 基于 superset:basepip"

RUN curl -fsSL https://code-server.dev/install.sh | sh

RUN code-server --install-extension ms-python.python
RUN code-server --install-extension Kelvin.vscode-sshfs
RUN code-server --install-extension ms-toolsai.jupyter
RUN code-server --install-extension tht13.python
RUN code-server --install-extension magicstack.MagicPython
RUN code-server --install-extension EricSia.pythonsnippets3
RUN code-server --install-extension Yseop.vscode-yseopml