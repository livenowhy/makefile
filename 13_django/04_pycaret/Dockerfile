FROM registry.cn-beijing.aliyuncs.com/livenowhy/django:crewai

# 1. pycaret
RUN pip install --no-cache-dir pycaret==3.3.2
RUN pip install --no-cache-dir pycaret[full]
RUN pip install --no-cache-dir yapf==0.43.0
RUN pip install --no-cache-dir keras==3.10.0
RUN pip install --no-cache-dir keras-bert==0.89.0
RUN pip install --no-cache-dir tensorflow==2.19.0
RUN pip install --no-cache-dir hyperopt==0.2.7
RUN pip install --no-cache-dir 'shillelagh[all]'