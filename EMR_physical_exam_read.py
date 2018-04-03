# -*- coding: utf-8 -*-
'''
处理电子病历中“体格检查”部分

2018-4-2 Luo Yifu
'''

# numpy包引入用来构建向量和向量计算
import numpy as np

filename = 'patient_physical_exam.txt'
filename2 = 'patient_physical_exam2.txt'


# 读取体格检查数据，并根据“。，”进行分割。分割成的每项特征写入word_list列表中
def read_physical_exam_file(filename):
    import re
    word_list = []
    f = open(filename)
    t = f.read()
    t = re.sub(r'\s+', '', t)  # 去除多空格 to空格
    t = re.sub(r'\n+', '', t)
    for x in re.split(r'[，。]', t):  # 按照“。，”对字符串进行切割
        word_list.append(x)
    return word_list


# ---提取病历中非重复特征---
# 输入wordlist列表，如果列表中有元素并未在featrue_list列表中出现，
# 则在feature_list列表中添加该元素
# 最终返回feature_list列表
def find_unique_feature(feature_list, wordlist):
    for x in wordlist:
        if x not in feature_list:
            feature_list.append(x)
    return feature_list


# ---提取某个病历的特征---
# 提取某个体格检查病历的特征，表述为一个0,1值的向量
# 输入feature_list(总病历特征)列表，如果该病历有某个特征，则该特征值记为1，否则记为0
# wordlist为某个病例。是经过分割后的词列表
# 返回值feature_EMR是一个numpy array(向量)
def feature_EMR_physical_exam(feature_list, wordlist):
    feature_EMR = []
    for x in feature_list:
        if x in wordlist:
            feature_EMR.append('1')
        else:
            feature_EMR.append('0')
    feature_EMR = np.array(feature_EMR, dtype='int')
    return feature_EMR


# tf-idf方法

# 计算特征的idf值
# 输入所有文档的特征向量，wordlist是列表的列表
# featrue_list是所有特征的向量
# 输出feature_idf_list是每个特征的idf值
def feature_idf(feature_list, wordlist):
    n = len(wordlist)  # 文档总数
    feature_idf_list = []
    for i in feature_list:
        count = 0
        for j in wordlist:
            if i in j:
                count = count + 1
        t = np.log10(n/count)
        feature_idf_list.append(t)
    feature_idf_list = np.array(feature_idf_list, dtype='float')
    return feature_idf_list


# 计算某个病历的每个特征的tfidf值

# 输入某个病历的特征向量wordlist
# 输出该病历每个特征的tfidf值
def feature_tfidf(wordlist, feature_idf_list):
    nl = len(wordlist)
    feature_tfidf = np.zeros(nl)
    n_word = np.sum(wordlist)
    wordlist_t = wordlist/n_word
    for num in range(nl):
        feature_tfidf[num] = wordlist_t[num]*feature_idf_list[num]
    return feature_tfidf


'''
测试部分

'''

word_list = []
word_list.append(read_physical_exam_file(filename))
word_list.append(read_physical_exam_file(filename2))

physical_exam_feature_list = []

physical_exam_feature_list = find_unique_feature(
    physical_exam_feature_list, word_list[0])
physical_exam_feature_list = find_unique_feature(
    physical_exam_feature_list, word_list[1])

# 计算physical_exam_feature_list中每个特征的idf值
feature_idf_list = feature_idf(physical_exam_feature_list, word_list) 

feature_EMR_p1 = feature_EMR_physical_exam(
    physical_exam_feature_list, word_list[0])

# 计算word_list[0]病历的每个特征的tfidf值
feature_tfidf_1 = feature_tfidf(feature_EMR_p1, feature_idf_list)

print(physical_exam_feature_list)
