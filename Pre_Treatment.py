# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 14:14:46 2018

清洗文本函数集合，包括清理特殊符号，过滤停止词，建立停止词列表
@author: Administrator
"""
# 清洗文本的函数集合
# 包括过滤多余的空格，过滤停止词
 

# 清洗数据，除去多余的空格以及各种符号和编码
def washdata(text_str):
    import re
    text_str = re.sub(r'[\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*（）]+', '', text_str)
    text_str = re.sub(r'\s+', '', text_str)  # trans 多空格 to空格
    text_str = re.sub(r'\n+', '', text_str)  # trans 换行 to空格
    text_str = re.sub(r'\t+', '', text_str)  # trans Tab to空格
    return text_str


# 过滤停止词，并形成一个列表文件，每一行存储一个词
# 词典格式：一个词占一行；每一行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒
def wash_stopword(text_data, stopwords, **dict_file_name):
    import jieba
    jieba.load_userdict(dict_file_name)  # file_name 为文件类对象或自定义词典的路径
    text_list = jieba.lcut(text_data)
    word_list = []
    for sentence in text_list:
        if sentence not in stopwords:
            word_list.append(sentence)
    return word_list


# 建立停止词列表
def stopwordslist(filepath):
    import io
    stopwords = [line.strip() for line in io.open(
        filepath, 'r', encoding='gbk').readlines()]
    return stopwords


# 如何处理无/否认的信息
# 识别否定关键词“无/否认/正常”，如果存在该关键词，删除该关键词所在条目
def deny_rules(text_str):
    import re
    str_pattern = r'无|否认|正常'
    pattern = re.compile(str_pattern)
    if pattern.search(text_str):
        return False
    else:
        return True
