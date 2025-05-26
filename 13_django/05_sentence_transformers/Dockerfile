FROM registry.cn-beijing.aliyuncs.com/livenowhy/django:pycaret


# 1. sentence-transformers
RUN pip install --no-cache-dir sentence-transformers==4.0.2
RUN pip install --no-cache-dir chardet==5.0.0
RUN pip install --no-cache-dir tf-keras==2.19.0
RUN pip install --no-cache-dir hf-xet==1.0.3
RUN pip install --no-cache-dir huggingface_hub
RUN pip install --no-cache-dir huggingface_hub[hf_xet]

ENV HF_ENDPOINT=https://hf-mirror.com
ADD fetch_model.py /share/fetch_model.py

# # 2. 下载模型 'sentence-transformers/paraphrase-multilingual-mpnet-base-v2'
# RUN huggingface-cli download --resume-download sentence-transformers/paraphrase-multilingual-mpnet-base-v2

# 3. 验证模型是否下载完成; 是否可用
RUN python /share/fetch_model.py sentence-transformers/paraphrase-multilingual-mpnet-base-v2

RUN apt-get autoremove -y --purge build-essential
RUN rm -rf /var/lib/apt/lists/*