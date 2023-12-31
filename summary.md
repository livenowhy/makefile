### 01_alpine

  `3.16`: alpine 基础镜像

    registry.cn-beijing.aliyuncs.com/livenowhy/alpine:3.16  (已构建)

### 02_mysql

  `01_5.6` 官方 mysql 5.6

    registry.cn-beijing.aliyuncs.com/livenowhy/mysql:5.6  (已构建)

  `02_5.6.base` 基于 5.6 配置的 mysql 镜像

    registry.cn-beijing.aliyuncs.com/livenowhy/mysql:5.6.base  (已构建)

  `03_8.0` 官方 mysql 8.0

    registry.cn-beijing.aliyuncs.com/livenowhy/mysql:8.0  (已构建)

  `04_8.0.base` 基于 8.0 配置的 mysql 镜像

    registry.cn-beijing.aliyuncs.com/livenowhy/mysql:8.0.base  (已构建)

### 03_redis

  `01_6.0` 官方 redis 6.0

    registry.cn-beijing.aliyuncs.com/livenowhy/redis:6.0  (已构建)

  `02_6.0.base` 基于 redis 6.0 进行优化配置的镜像

    registry.cn-beijing.aliyuncs.com/livenowhy/redis:6.0.base  (已构建)

### 04_mongo

  `01_6.0.1` 官方 mongo 6.0.1

    registry.cn-beijing.aliyuncs.com/livenowhy/mongo:6.0.1  (已构建)

  `02_mongo-express` 官方 mongo-express

    registry.cn-beijing.aliyuncs.com/livenowhy/mongo-express:1.0.0-alpha.4  (已构建)

### 05_rabbitmq

  `01_3.8` 官方 rabbitmq 3.8

    registry.cn-beijing.aliyuncs.com/livenowhy/rabbitmq:3.8  (已构建)

  `02_rabbitmq_management` 官方 rabbitmq 3.8 management

    registry.cn-beijing.aliyuncs.com/livenowhy/rabbitmq:3.8-management  (已构建)

### 06_centos

  `01_7.6` centos 7.6 
    
    registry.cn-beijing.aliyuncs.com/livenowhy/centos:7.6  (已构建)

  `02_tools` 基于 centos 7.6 配置的开放环境(集成各种工具)

    registry.cn-beijing.aliyuncs.com/livenowhy/centos:tools  (已构建)

### 07_python (无法自动构建)

  `01_3.10`: python 3.10 官方镜像

    registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10  (无法自动构建, 已经手动构建)

  `02_3.10.base`:   基于 3.10 配置了基础环境的镜像

    registry.cn-beijing.aliyuncs.com/livenowhy/python:3.10.base

  `03_ethnic`: 基于 3.10.base 配置 的 ethnic 镜像

    registry.cn-beijing.aliyuncs.com/livenowhy/python:ethnic

  `04_temporalio`: 基于 3.10.base 配置的 temporalio 镜像
    
    registry.cn-beijing.aliyuncs.com/livenowhy/python:temporalio

  `05_3.10-alpine`  python:3.6-alpine
    
    registry.cn-beijing.aliyuncs.com/livenowhy/python:3.6-alpine

  `06_3.6-alpine-base`  基于 3.6-alpine 配置的 python 镜像
    
    registry.cn-beijing.aliyuncs.com/livenowhy/python:3.6-alpine-base


### 08_nas

  `01_calibre` 优化官方 calibre-web

    registry.cn-beijing.aliyuncs.com/livenowhy/calibre-web:latest

  `02_certbot` 免费证书
    
    registry.cn-beijing.aliyuncs.com/livenowhy/certbot:latest


### 09_node

  `01_14.3.0`  官方 nodejs alpine3.10

    registry.cn-beijing.aliyuncs.com/livenowhy/node:14.3.0-alpine3.10  (已构建)

  `02_19.0.0` 官方 nodejs 19.0.0-alpine3.15
    
    registry.cn-beijing.aliyuncs.com/livenowhy/node:19.0.0-alpine3.15  (已构建)

  `03_latest` 官方 最新 nodejs
     
     registry.cn-beijing.aliyuncs.com/livenowhy/node:latest  (已构建)

  `04_10.22.0-buster-slim` 用于安装 gitbook 的 nodejs 版本

    registry.cn-beijing.aliyuncs.com/livenowhy/node:10.22.0-buster-slim  (已构建)

  `05_gitbook` gitbook 版本

    registry.cn-beijing.aliyuncs.com/livenowhy/node:gitbook  (已构建)

  `06_lts-alpine3.18`
      
    registry.cn-beijing.aliyuncs.com/livenowhy/node:lts-alpine3.18  (已构建)


### 10_k8s

  `01_alertmanager` 官方 alertmanager:v0.15.3

    registry.cn-beijing.aliyuncs.com/livenowhy/alertmanager:v0.15.3

  `02_remote_storage_adapter` 官方 remote_storage_adapter

    registry.cn-beijing.aliyuncs.com/livenowhy/remote_storage_adapter:lastest

  `03_kapacitor` kapacitor:1.5

    registry.cn-beijing.aliyuncs.com/livenowhy/kapacitor:1.5

  `04_telegraf` telegraf:1.16
    
    registry.cn-beijing.aliyuncs.com/livenowhy/telegraf:1.16

  `05_pushgateway` pushgateway:v1.3.0

    registry.cn-beijing.aliyuncs.com/livenowhy/pushgateway:v1.3.0

### 11_elasticsearch
    
### 12_influxdb

  `01_1.8` influxdb:1.8

    registry.cn-beijing.aliyuncs.com/livenowhy/influxdb:1.8

  `02_2.0` influxdb:2.0.0-rc

    registry.cn-beijing.aliyuncs.com/livenowhy/influxdb:2.0

### 13_golang

  `01_1.15.5-alpine3.12`

    registry.cn-beijing.aliyuncs.com/livenowhy/golang:1.15.5-alpine3.12

### 14_nginx

  `01_1.18`

    registry.cn-beijing.aliyuncs.com/livenowhy/nginx:1.18

### 15_bytebase

### 16_adminer

  `4.8.1-standalone` 官方 4.8.1-standalone 

    registry.cn-beijing.aliyuncs.com/livenowhy/adminer:4.8.1-standalone  (已构建)


### 18_ubuntu

### 19_squid

### 20_jenkins
  
  `01_2.303.2` 官方 2.303.2 jenkins 镜像

    registry.cn-beijing.aliyuncs.com/livenowhy/jenkins:2.303.2 (已构建)