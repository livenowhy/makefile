#!/usr/bin/python3
# coding=utf-8

import os 

def load_file():
    """ 加载文件 """
    path = '.'
    for root, dirs, files in os.walk(path=path):
        print(root, dirs, files)


if __name__ == "__main__":
    pass