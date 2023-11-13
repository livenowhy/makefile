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