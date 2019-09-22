#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/11

from gensim import corpora, models, similarities  # 语料库，模型，文本分析
import jieba
from  collections import defaultdict

text_1 = "E:/Pycharm 文件/数据挖掘/文本分析/dmbj.txt"
text_2 = "E:/Pycharm 文件/数据挖掘/文本分析/gcd.txt"

# 读取文档
w1 = open(text_1, 'rb').read().decode('utf-8')
w2 = open(text_2, 'rb').read().decode('utf-8')

# 分词
d1 = jieba.cut(w1)
d2 = jieba.cut(w2)

# 对文档进行整理成指定格式
data_1 = ""
for item in d1:
    data_1 += item + " "

data_2 = ""
for item in d1:
    data_2 += item + " "

documents = [data_1, data_2]

# 将文本从字符串转换为数组（列表）
texts = [[word for word in document.split()] for document in documents]  # 逐字逐句   split切片

# 计算频数
frequency = defaultdict(int)

for text in texts:
    for token in text:
        frequency[token] += 1

'''
当数据过大时，应对数据进行过滤
texts = [[word for word in text if frequency[key]>3] for text in texts]
'''

# 建立词典
dic = corpora.Dictionary(texts)
# 保存词典
dic.save("E:/Pycharm 文件/数据挖掘/文本分析/d_g词典.txt")

# 建立对比文档
text_3 = "E:/Pycharm 文件/数据挖掘/文本分析/ljm.txt"
w3 = open(text_3, 'rb').read().decode('utf-8')
d3 = jieba.cut(w3)

data_3 = ""
for item in d3:
    data_3 += item + " "
new_documents = data_3

# 将对比文档用doc2bow转换为稀疏向量
new_vector = dic.doc2bow(new_documents.split())

# 对稀疏向量进行进一步处理，得到新语料库
new_cor = [dic.doc2bow(text) for text in texts]

# 新语料库通过tfidfmodel进行处理
tf_idf = models.TfidfModel(new_cor)

# 通过token2id得到特征数
feature_Num = len(dic.token2id.keys())

# 建立稀疏矩阵相似度
new_array = similarities.SparseMatrixSimilarity(tf_idf[new_cor], num_features=feature_Num)

# 最终结果：相似度
similar = new_array[tf_idf[new_vector]]
print(similar)
