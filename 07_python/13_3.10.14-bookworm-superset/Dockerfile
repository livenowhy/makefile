FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-codeserver

LABEL description="superset 镜像, 基于 python:3.10.14-bookworm-codeserver"

# 1. 代码补全
RUN pip install --no-cache-dir jupyterlab
RUN pip install --no-cache-dir jupyterlab-lsp
RUN pip install --no-cache-dir "python-lsp-server[all]"

# 2. base pip
RUN pip install --no-cache-dir Flask==2.3.3
RUN pip install --no-cache-dir Flask-Cors==4.0.1
RUN pip install --no-cache-dir apache-superset==4.0.0
RUN pip install --no-cache-dir vanna
RUN pip install --no-cache-dir mysqlclient
RUN pip install --no-cache-dir Pillow
RUN pip install --no-cache-dir PyMySQL
RUN pip install --no-cache-dir ipython
RUN pip install --no-cache-dir prophet
RUN pip install --no-cache-dir yapf
RUN pip install --no-cache-dir flake8
RUN pip install --no-cache-dir mlflow==2.14.1
RUN pip install --no-cache-dir pycaret[full]
RUN pip install --no-cache-dir keras
RUN pip install --no-cache-dir keras-bert
RUN pip install --no-cache-dir tensorflow
RUN pip install --no-cache-dir hyperopt
RUN pip install --no-cache-dir 'shillelagh[all]'

ADD jupyter_lab_config.py      /root/.jupyter/jupyter_lab_config.py

# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  jupyterlab-kite

# sudo docker save -o python_basepip.tar registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-basepip