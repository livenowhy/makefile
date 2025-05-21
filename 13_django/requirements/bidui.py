#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author: livenowhy
@contact: liuzhangpei@126.com
"""


import os


if __name__ == "__main__":

    # 1. 获取 Dockerfile 版本
    with open('/Users/zpliu/Desktop/share/makefile/13_django/requirements/dockerfile.txt') as fp:
        dockerfile_lines = [line.replace('\n', '').upper() for line in fp.readlines()]
        
    # 1. 获取 镜像中 pip 版本
    with open('/Users/zpliu/Desktop/share/makefile/13_django/requirements/image.txt') as fp:
        image_lines = [line.replace('\n', '').upper() for line in fp.readlines()]

    
    print(set(dockerfile_lines) - set(image_lines))

    # print(set(image_lines) - set(dockerfile_lines))
# docker run registry.cn-beijing.aliyuncs.com/livenowhy/django:pycaret pip freeze > image.txt
