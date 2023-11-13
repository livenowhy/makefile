## 镜像存储

    https://cr.console.aliyun.com/cn-beijing/instance/repositories
    docker login --username=hi35608059@aliyun.com registry.cn-beijing.aliyuncs.com

## 采用阿里云自动构建

    注意：构建上下文目录 (去除makefile路径, 即 /makefile/01_alpine/3.16/ -> /01_alpine/3.16/)

## 项目列表

### 01_alpine

  `3.16`: alpine 基础镜像

    registry.cn-beijing.aliyuncs.com/livenowhy/alpine:3.16