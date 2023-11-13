FROM registry.cn-beijing.aliyuncs.com/livenowhy/ubuntu:develop

LABEL description="Make Ubuntu Development Environment (jupyter)"

# 先设置 后续需要的路径及暴露的端口
RUN mkdir -p /share/notebooks
EXPOSE 8006

# 安装 jupyter
ADD requirements.txt /root/requirements.txt
RUN pip3 install -r /root/requirements.txt
RUN rm -rf /root/requirements.txt

# 设置 jupyter notebook 的代码自动补全
RUN pip3 install jupyter_contrib_nbextensions
RUN jupyter contrib nbextension install --user
RUN pip3 install jupyter_nbextensions_configurator
RUN jupyter nbextensions_configurator enable --user

ADD jupyter_run.sh /jupyter_run.sh
ENTRYPOINT ["/bin/bash", "/jupyter_run.sh"]