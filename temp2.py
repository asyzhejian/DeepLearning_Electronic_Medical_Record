# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 09:27:21 2018

@author: Administrator
"""

import jieba
import nltk
import re

raw=open(u'C:/Users/Administrator/Desktop/神经网络与医疗数据/语料仓库/roommate.txt')
temp_str=raw.read()

# 创建停用词list  
def stopwordslist(filepath):  
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]  
    return stopwords  

# 分词
def seg_sentence(textdata):  
    sentence_seged = jieba.lcut(textdata)  
    stopwords = stopwordslist(u'C:/Users/Administrator/Desktop/神经网络与医疗数据/语料仓库/stopword.txt')  # 这里加载停用词的路径  
    outstr = ''  
    for word in sentence_seged:  
        if word not in stopwords:  
            if word != '\t':  
                outstr += word  
                outstr += " "  
    return outstr  




def Word_cut_list(self,word_str):
        #利用正则表达式去掉一些一些标点符号之类的符号。
        word_str = re.sub(r'\s+', ' ', word_str)  # trans 多空格 to空格
        word_str = re.sub(r'\n+', ' ', word_str)  # trans 换行 to空格
        word_str = re.sub(r'\t+', ' ', word_str)  # trans Tab to空格
        word_str = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——；！，”。《》，。：“？、~@#￥%……&*（）1234567①②③④)]+".\
                          decode("utf8"), "".decode("utf8"), word_str)
  
        wordlist = list(jieba.cut(word_str))#jieba.cut  把字符串切割成词并添加至一个列表
        wordlist_N = []
        chinese_stopwords=self.Chinese_Stopwords()
        for word in wordlist:
            if word not in chinese_stopwords:#词语的清洗：去停用词
                if word != '\r\n'  and word!=' ' and word != '\u3000'.decode('unicode_escape') \
                        and word!='\xa0'.decode('unicode_escape'):#词语的清洗：去全角空格
                    wordlist_N.append(word)
        return wordlist_N

# temp_str=Word_cut_list(temp_str)

noval_data=jieba.lcut(temp_str)



noval=nltk.text.Text(noval_data) #初始化小说数据noval_data为Text类
#text=nltk.text.Text(jieba.lcut(raw))
print (noval.concordance(u'性感'))
# noval.plot(30)
# noval.dispersion_plot([u'性感',u'美丽'])

jieba.analyse.set_stop_words(u'C:/Users/Administrator/Desktop/神经网络与医疗数据/语料仓库/stopword.txt')
tags = jieba.analyse.extract_tags(text,20)