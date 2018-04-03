# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 14:14:46 2018
获取某路径下所有文件的名称及完整路径

@author: luo yifu
"""
# 批量获取目录下文件的文件名和文件的全目录

import os


# 获取path目录下，filetype类型的所有文件的名称，写入name列表
def get_filename(path, filetype):
    name = []
    for root, dirs, files in os.walk(path):
        for i in files:
            if filetype in i:
                name.append(i.replace(filetype, ''))
    return name


# 获取完整的文件名称路径，结果存储在filename列表中
def get_full_filename(path, filetype):
    filename = []
    for root, dirs, files in os. walk(path):
        for i in files:
            if filetype in i:
                templist = [path, i]
                tempname = ''.join(templist)
                filename.append(tempname)
    return filename
