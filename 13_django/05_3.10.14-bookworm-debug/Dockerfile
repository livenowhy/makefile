FROM registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-pycaret

LABEL description="django pycaret 运行镜像; 基于 3.10.14-bookworm-crewai"

# 1. other
RUN pip install --no-cache-dir sentence-transformers==4.0.2
RUN pip install --no-cache-dir chardet==5.0.0
RUN pip install --no-cache-dir tf-keras==2.19.0
RUN pip install hf-xet==1.0.3
ADD fetch_model.py /share/fetch_model.py

# 2. 下载模型 'sentence-transformers/paraphrase-multilingual-mpnet-base-v2'
RUN python /share/fetch_model.py sentence-transformers/paraphrase-multilingual-mpnet-base-v2

RUN apt-get autoremove -y --purge build-essential
RUN rm -rf /var/lib/apt/lists/*


# docker save -o ai_pycaret.tar registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-pycaret
# docker save -o ai_debug.tar registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.14-bookworm-debug