FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-dev

LABEL description="mlflow 镜像, 基于 python:3.10.14-bookworm-dev"

RUN pip install --no-cache-dir mlflow
RUN pip install --no-cache-dir pycaret[full]

# registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-mlflow