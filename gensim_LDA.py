# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 14:14:46 2018

使用LDA方法，分析文本库中的文档

@author: luo yifu
"""
from gensim import corpora, models
from read_rewrite_text import read_word_list
import read_text_database
import pprint as pp

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
# dictionary = corpora.Dictionary.load_from_text('/tmp/MedicalRecord.dict') # 读取存储的词典
dictionary.save(u'C:/Users/Administrator/Desktop/神经网络与医疗数据/DeepLearning_Electronic_Medical_Record/temp/MedicalRecord.dict')  # 将词典存储以备未来使用

corpus = []
for text in text_word_list:
    corpus.append(dictionary.doc2bow(text))

# 将corpus存储到文件中以备未来使用
corpora.MmCorpus.serialize(u'C:/Users/Administrator/Desktop/神经网络与医疗数据/DeepLearning_Electronic_Medical_Record/temp/MecicalRecord.mm', corpus)  

# 读取文件中的corpus
# corpus = corpora.MmCorpus(/tmp/MecicalRecord.mm')


'''
# tfidf&lsi模型

tfidf_model = models.TfidfModel(corpus) 
corpus_tfidf = tfidf_model[corpus]

lsi_model = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=50)
corpus_lsi = lsi_model[corpus_tfidf]

'''

# num_topics: 必须。LDA 模型要求用户决定应该生成多少个主题。由于我们的文档集很小，所以我们只生成15个主题。
# id2word：必须。LdaModel 类要求我们之前的 dictionary 把 id 都映射成为字符串。
# passes：可选。模型遍历语料库的次数。遍历的次数越多，模型越精确。但是对于非常大的语料库，遍历太多次会花费很长的时间
EMR_ldamodel = models.ldamodel.LdaModel(corpus, num_topics=10, id2word=dictionary, passes=30)

# 将LDA模型存储到文件中
lda_model_filename = u'C:/Users/Administrator/Desktop/神经网络与医疗数据/DeepLearning_Electronic_Medical_Record/temp/MedicalRecord_lda.model'
EMR_ldamodel.save(lda_model_filename)

t = EMR_ldamodel.print_topics(num_topics=10, num_words=20)

pp.pprint(EMR_ldamodel.print_topics(5))


# 读取已有的LDA model，输入LDA model的文件路径
def Reload_Existing_Corpus_Model(lda_model_filename):
    ldamodel = models.ldamodel.LdaModel.load(lda_model_filename)
    return ldamodel


# 输入需要建模的文字text_doc，字典dic，和lad模型的文件lda_model_filename
def LDA_Predict(text_doc, Dict, lda_model_filename):
    lda_model = Reload_Existing_Corpus_Model(lda_model_filename)
    # 文档转换成bow
    doc_bow = Dict.doc2bow(text_doc)
    # 得到新文档的主题分布
    doc_lda = lda_model[doc_bow]
    pp.pprint(doc_lda)

LDA_Predict(text_word_list[1], dictionary, lda_model_filename)
