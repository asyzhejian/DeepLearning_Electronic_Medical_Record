# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 14:37:54 2018

对字符串进行分词，过滤停止词，并将结果写入文件当中
读取之前写入的分词完毕的文件

@author: Administrator
"""


# 函数读取text_str，过滤掉stopwords, 分词并标注词性，将结果写入filename文件中
# 格式为每个词占一行，词 词性
def write_word_to_file(text_str, stopwords, filename):
    import jieba.posseg as pseg
    with open(filename, 'w+') as f:
        for x in pseg.cut(text_str):
            if x.word not in stopwords:
                f.write('{0}\t{1}\n'.format(x.word, x.flag))


# 将text_str文件分词后得到的word_list列表，写入文件filename
# 格式为每行一个词
def write_word_list_to_file(word_list, filename):
    with open(filename, 'w+') as f:
        for x in word_list:
            f.write('{0}\n'.format(x))


# 读取进行过分词和划分词性的filename，将数据导入word_list中
def read_cut_result(filename):
    word_list = []
    with open(filename, 'r') as f:
        for x in f.readlines():
            p = x.split()
            word_list.append((p[0], p[1]))
    return word_list


# 读取存入文件中的word_list
def read_word_list(filename):
    word_list = []
    with open(filename, 'r') as f:
        word_list = f.read().splitlines()
    return word_list
