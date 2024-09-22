## 镜像存储

    https://cr.console.aliyun.com/cn-beijing/instance/repositories
    docker login --username=hi35608059@aliyun.com registry.cn-beijing.aliyuncs.com

## 代码存放位置
    
    https://codeup.aliyun.com/
    git clone git@codeup.aliyun.com:666f9ca829ecbe2305351563/makefile.git


## 采用阿里云自动构建

    注意：构建上下文目录 (去除makefile路径, 即 /makefile/01_alpine/3.16/ -> /01_alpine/3.16/)


## Makefile 文件必须字段

    TAG: 镜像标签
    PREFIX: 镜像前缀
    IMAGE_NAME: 镜像名称
    STATUS: 构建状态

    通过 ${PREFIX}/${IMAGE_NAME}:${TAG} 组合成完整镜像名

## Dockerfile 文件必须字段
    
    LABEL description="镜像说明"


## 