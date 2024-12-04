FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-django

LABEL description="django ai 运行镜像; 基于 3.10.14-bookworm-django"



# 4. pycaret
RUN pip install --no-cache-dir pycaret==3.3.2
RUN pip install --no-cache-dir pycaret[full]
RUN pip install --no-cache-dir yapf==0.40.2
RUN pip install --no-cache-dir keras==3.5.0
RUN pip install --no-cache-dir keras-bert==0.89.0
RUN pip install --no-cache-dir tensorflow==2.17.0
RUN pip install --no-cache-dir hyperopt==0.2.7
RUN pip install --no-cache-dir 'shillelagh[all]'

# 5. other
RUN pip install --no-cache-dir django-redis==5.2.0
RUN pip install --no-cache-dir django-cors-headers==4.6.0

# docker save -o python_ai.tar registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-ai