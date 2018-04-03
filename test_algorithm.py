# -*- coding: utf-8 -*-
'''
为了测试算法分词效果
'''

import Pre_Treatment
import jieba.analyse

# 自定义字典可以更好的进行分词
dict_filename = ('')  # 输入自定义字典路径
stopwords = Pre_Treatment.stopwordslist('stopword.txt')

raw = open('roommate.txt')

temp_str = raw.read()
temp_str = Pre_Treatment.washdata(temp_str)
word_list = Pre_Treatment.wash_stopword(temp_str, stopwords)


jieba.analyse.set_stop_words('stopword.txt')
tags = jieba.analyse.extract_tags(temp_str, withWeight=True, topK=30)

print(",".join(tags))
