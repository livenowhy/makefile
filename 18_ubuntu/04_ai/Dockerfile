FROM registry.cn-beijing.aliyuncs.com/livenowhy/ubuntu:jupyter

LABEL description="Make Ubuntu Development Environment (ai)"

RUN python3 -m pip install --upgrade pip
RUN pip3 install django==4.2.2
RUN pip3 install openai==0.27.8
RUN pip3 install langchain==0.0.193
RUN pip3 install chromadb==0.3.26
RUN pip3 install tiktoken==0.4.0
RUN pip3 install mysqlclient==2.1.1
RUN pip3 install djangorestframework==3.14.0
RUN pip3 install asgiref==3.6.0
RUN pip3 install sqlparse==0.4.4
RUN pip3 install openpyxl==3.1.2

# RUN pip3 install gradio==3.34.0
# 
# RUN pip3 install pytest==7.3.1
# RUN pip3 install num2words==0.5.12
# RUN pip3 install matplotlib==3.7.1
# RUN pip3 install plotly==5.15.0
# RUN pip3 install scipy==1.10.1
# RUN pip3 install scikit-learn==1.2.2
# RUN pip3 install pandas==2.0.2
# RUN pip3 install unstructured==0.7.2
# RUN pip3 install pinecone-client==2.2.2
# RUN pip3 install pdf2image==1.16.3


ADD my.pth /usr/lib/python3/dist-packages/my.pth
EXPOSE 8001 8002 8003 8004 8005 8007 8008 8009 8010