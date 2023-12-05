#!/bin/bash

mkdir -p /bigdata
chmod -R a+wr /bigdata

# 创建 mysql 5.6 需要的文件夹
mkdir -p /bigdata/mysql
chmod -R a+wr /bigdata/mysql

# 创建 mysql 8.0 需要的文件夹
mkdir -p /bigdata/mysql8
chmod -R a+wr /bigdata/mysql8

# 创建 mongo 需要的文件夹
mkdir -p /bigdata/mongo
chmod -R a+wr /bigdata/mongo

# 创建 rabbitmq 需要的文件夹
mkdir -p /bigdata/rabbitmq
chmod -R a+wr /bigdata/rabbitmq

# 创建 Jupyter Notebook 文件夹
mkdir -p /bigdata/jupyter
chmod -R a+wr /bigdata/jupyter

# 创建 jenkins 需要的文件夹
mkdir -p /bigdata/jenkins
chmod -R a+wr /bigdata/jenkins

mkdir -p /bigdata/jenkinshome/
chmod -R a+wr /bigdata/jenkinshome/