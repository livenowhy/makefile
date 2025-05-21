FROM registry.cn-beijing.aliyuncs.com/livenowhy/django:pycaret


# 1. sentence-transformers
RUN pip install --no-cache-dir sentence-transformers==4.0.2
RUN pip install --no-cache-dir chardet==5.0.0
RUN pip install --no-cache-dir tf-keras==2.19.0
RUN pip install hf-xet==1.0.3
ADD fetch_model.py /share/fetch_model.py

# 2. 下载模型 'sentence-transformers/paraphrase-multilingual-mpnet-base-v2'
RUN python /share/fetch_model.py sentence-transformers/paraphrase-multilingual-mpnet-base-v2

RUN apt-get autoremove -y --purge build-essential
RUN rm -rf /var/lib/apt/lists/*


# 2. superset; prophet -> superset 预测插件
# RUN pip install --no-cache-dir apache-superset==4.1.2
# RUN pip install --no-cache-dir vanna==0.7.9
# RUN pip install --no-cache-dir prophet==1.1.6


# # 2. flask
# # superset 要求 Flask 版本
# RUN pip install --no-cache-dir Flask==2.3.3
# RUN pip install --no-cache-dir Flask-AppBuilder==4.6.4
# RUN pip install --no-cache-dir Flask-Cors==6.0.0
# RUN pip install --no-cache-dir flask-restful-swagger-2==0.35

