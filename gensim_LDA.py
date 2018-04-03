# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 14:14:46 2018

@author: luo yifu
"""
from gensim import corpora, models
from read_rewrite_text import read_word_list
import read_text_database

# 定义处理后的语料仓库地址
filepath_after_treatment_text_database = (
    u'C:/Users/Administrator/Desktop/神经网络与医疗数据/处理后的主诉及病史/database_treated/')
# 获取语料仓库中所有.txt文件的名称
filenames_full_path = read_text_database.get_full_filename(
    filepath_after_treatment_text_database, '.txt')


text_word_list = []
for i in filenames_full_path:
    text_word_list.append(read_word_list(i))

dictionary = corpora.Dictionary(text_word_list)

corpus = []
for text in text_word_list:
    corpus.append(dictionary.doc2bow(text))

# tfidf = models.TfidfModel(corpus)
# corpus_tfidf = tfidf[corpus]

# num_topics: 必须。LDA 模型要求用户决定应该生成多少个主题。由于我们的文档集很小，所以我们只生成15个主题。
# id2word：必须。LdaModel 类要求我们之前的 dictionary 把 id 都映射成为字符串。
# passes：可选。模型遍历语料库的次数。遍历的次数越多，模型越精确。但是对于非常大的语料库，遍历太多次会花费很长的时间
ldamodel = models.ldamodel.LdaModel(corpus, num_topics=50, id2word=dictionary, passes=30)

t = ldamodel.print_topics(num_topics=50, num_words=30)
ldamodel.print_topic(20)
for x in t:
    print(x)
