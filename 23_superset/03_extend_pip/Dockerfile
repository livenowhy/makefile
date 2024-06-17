FROM registry.cn-beijing.aliyuncs.com/livenowhy/superset:basepip

LABEL description="superset pip 镜像, 基于 superset:basepip"

RUN pip install yapf flake8
RUN pip install mlflow
RUN pip install pycaret
RUN curl -fsSL https://code-server.dev/install.sh | sh

RUN code-server --install-extension ms-python.python
RUN code-server --install-extension EricSia.pythonsnippets3
RUN code-server --install-extension ms-toolsai.jupyter
RUN code-server --install-extension tht13.python
RUN code-server --install-extension magicstack.MagicPython
RUN code-server --install-extension Yseop.vscode-yseopml
RUN code-server --install-extension ecmel.vscode-html-css
RUN code-server --install-extension abusaidm.html-snippets

RUN pip install keras tensorflow hyperopt keras-bert

# RUN code-server --install-extension Kelvin.vscode-sshfs
# 启动命令: code-server

# AttributeError: module 'keras.src.backend' has no attribute 'convert_to_numpy'
# import tensorflow.keras as keras