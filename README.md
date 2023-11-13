## 镜像存储

    https://cr.console.aliyun.com/cn-beijing/instance/repositories
    docker login --username=hi35608059@aliyun.com registry.cn-beijing.aliyuncs.com

## 采用阿里云自动构建

    注意：构建上下文目录 (去除makefile路径, 即 /makefile/01_alpine/3.16/ -> /01_alpine/3.16/)

## 项目列表

### 01_alpine

  `3.16`: alpine 基础镜像

    registry.cn-beijing.aliyuncs.com/livenowhy/alpine:3.16

### 02_mysql

  `01_5.6` 官方 mysql 5.6

    registry.cn-beijing.aliyuncs.com/livenowhy/mysql:5.6

  `02_5.6.base` 基于 5.6 配置的 mysql 镜像

    registry.cn-beijing.aliyuncs.com/livenowhy/mysql:5.6.base

  `03_8.0` 官方 mysql 8.0

    registry.cn-beijing.aliyuncs.com/livenowhy/mysql:8.0

### 03_redis

  `01_6.0` 官方 redis 6.0

    registry.cn-beijing.aliyuncs.com/livenowhy/redis:6.0

  `02_6.0.base` 基于 redis 6.0 进行优化配置的镜像

    registry.cn-beijing.aliyuncs.com/livenowhy/redis:6.0.base

### 04_mongo

  `01_6.0.1` 官方 mongo 6.0.1

    registry.cn-beijing.aliyuncs.com/livenowhy/mongo:6.0.1

  `02_mongo-express` 官方 mongo-express

    registry.cn-beijing.aliyuncs.com/livenowhy/mongo-express:1.0.0-alpha.4

### 05_rabbitmq

  `01_3.8` 官方 rabbitmq 3.8

    registry.cn-beijing.aliyuncs.com/livenowhy/rabbitmq:3.8

  `02_rabbitmq_management` 官方 rabbitmq 3.8 management

    registry.cn-beijing.aliyuncs.com/livenowhy/rabbitmq:3.8-management


### 06_centos

  `01_7.6` centos 7.6 
    
    registry.cn-beijing.aliyuncs.com/livenowhy/centos:7.6

  `02_tools` 基于 centos 7.6 配置的开放环境(集成各种工具)

    registry.cn-beijing.aliyuncs.com/livenowhy/centos:tools

### 07_python

  `01_latest`: python latest 官方镜像

    registry.cn-beijing.aliyuncs.com/livenowhy/python:latest

  `02_base`:   基于 latest 配置了基础环境的镜像

    registry.cn-beijing.aliyuncs.com/livenowhy/python:base

  `03_ethnic`: 基于 base 配置 的 ethnic 镜像

    registry.cn-beijing.aliyuncs.com/livenowhy/python:ethnic

  `04_temporalio`: 基于 base 配置的 temporalio 镜像
    
    registry.cn-beijing.aliyuncs.com/livenowhy/python:temporalio

  `05_3.6-alpine`  python:3.6-alpine
    
    registry.cn-beijing.aliyuncs.com/livenowhy/python:3.6-alpine

