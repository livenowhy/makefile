FROM registry.cn-beijing.aliyuncs.com/livenowhy/superset:lean

LABEL description="superset pip 镜像, 基于 superset:lean"

RUN pip install --upgrade setuptools pip
RUN pip install apache-superset==4.0.0
RUN pip install vanna==0.5.5
RUN pip install mysqlclient
RUN pip install Pillow
RUN pip install flask_cors
RUN pip install PyMySQL
RUN pip install prophet
RUN pip install ipython

RUN pip3 install supervisor
RUN echo_supervisord_conf > /etc/supervisord.conf
RUN echo '[include]' >> /etc/supervisord.conf
RUN echo 'files = /etc/supervisord.d/*.ini' >> /etc/supervisord.conf
RUN mkdir /etc/supervisord.d/
RUN mkdir /var/log/supervisor/


# 代码补全
RUN pip install jupyterlab
RUN pip install jupyterlab-lsp
RUN pip install "python-lsp-server[all]"
# RUN jupyter labextension install @krassowski/jupyterlab-lsp
# RUN pip install jupyterlab-language-pack-zh-CN
# RUN pip install jupyterlab-kite
# RUN pip install ipykernel

# 预测插件
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  jupyterlab-kite


WORKDIR /app
