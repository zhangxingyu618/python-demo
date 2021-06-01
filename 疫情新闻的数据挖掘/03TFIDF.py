import pandas as pd
import numpy as np
import jieba.analyse
import matplotlib.pyplot as plt


# 分词
cut_words = ""
for line in open('news_data.txt', encoding='utf-8'):
    line.strip('\n')
    seg_list = jieba.cut(line, cut_all=False)
    # print(" ".join(seg_list))
    cut_words += (" ".join(seg_list))

# print(cut_words)

# 提取主题词 返回的词频其实就是TF-IDF 利用tfidf算法
keywords = jieba.analyse.extract_tags(cut_words,
                                      topK=50,  # 前50个关键词
                                      withWeight=True,  # 返回关键词的权重
                                      allowPOS=('a', 'e', 'n', 'nr', 'ns', 'v'))
                                      # 词性   形容词 叹词 名词 人名 地名 动词

print(keywords)
# 返回形式为列表

# 前五十数据存储到文件中
pd.DataFrame(keywords, columns=['词语', '重要性']).to_excel('TF_IDF 前50.xlsx')

# keyword本身包含两列数据
ss = pd.DataFrame(keywords, columns=['词语', '重要性'])
print(range(len(ss.重要性[:25][::-1])))
print("============================")
print(ss.重要性[:25][::-1])
print("============================")
print(ss.词语[:25][::-1])

# 画图 水平直方图
# 解决plt画图不显示中文问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(10, 6))
plt.title('TF-IDF')
fig = plt.axes()
plt.barh(range(len(ss.重要性[:25][::-1])), ss.重要性[:25][::-1])  # 前25个字符 倒序 0-25,坐标
fig.set_yticks(np.arange(len(ss.重要性[:25][::-1])))  # y轴的数值
fig.set_yticklabels(ss.词语[:25][::-1])  # y轴的标签
fig.set_xlabel('TF-IDF值')
plt.show()
