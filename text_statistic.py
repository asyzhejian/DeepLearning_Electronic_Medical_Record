import nltk
import read_rewrite_text

word_list = read_rewrite_text.read_word_list('text1_wordlist.txt')

noval = nltk.text.Text(word_list)
# 初始化小说数据noval_data为Text类

freq_noval = nltk.FreqDist(noval)
# 词语的频率分布
t = freq_noval.most_common(10)
print(t)
