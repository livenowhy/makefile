#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: livenowhy
@contact: liuzhangpei@126.com
@notes:
https://modelscope.cn 国内CDN加速
https://mirrors.tuna.tsinghua.edu.cn/hugging-face 教育网优化

客户端下载模型:
# huggingface-cli download gpt2 config.json model.safetensors
# huggingface-cli download sentence-transformers/paraphrase-multilingual-mpnet-base-v2 config.json model.safetensors
"""

import sys
import os
from sentence_transformers import SentenceTransformer

# 2023年6月 之后的 huggingface_hub
# from huggingface_hub import configure_hf  # 新增关键配置
# # 关键步骤：在加载模型前设置镜像源
# configure_hf(mirror="https://hf-mirror.com")  # 使用清华大学镜像

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"  # 核心配置

def fetch_model(model):
    """
    获取模型
    model='sentence-transformers/paraphrase-multilingual-mpnet-base-v2'
    """
    # 1. Load a pretrained Sentence Transformer model
    model = SentenceTransformer(model)

    # The sentences to encode
    sentences = [
        "The weather is lovely today.",
        "It's so sunny outside!",
        "He drove to the stadium.",
    ]

    # 2. Calculate embeddings by calling model.encode()
    embeddings = model.encode(sentences)
    print(embeddings.shape)

    # 3. Calculate the embedding similarities
    similarities = model.similarity(embeddings, embeddings)
    print(similarities)

if __name__ == '__main__':
    if 2 != len(sys.argv):
        raise Exception('参数不符合要')
    model = sys.argv[1]
    print(f'准备下载模型 {model} 到本地')
    fetch_model(model)