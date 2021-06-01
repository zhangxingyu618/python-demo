import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import re
from PIL import Image as im
from wordcloud import WordCloud
import numpy as np
import jieba

font_set = FontProperties(fname=r"C:/Windows/Fonts/STKAITI.TTF", size=15)

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

text = pd.read_csv(r'ganjiwang.csv')
columns = ['title', 'type', 'mode', 'size', 'direction', 'floor', 'quxian', 'community', 'address', 'money', 'subway',
           'peizhi', 'describe']
text.columns = ['title', 'type', 'mode', 'size', 'direction', 'floor', 'quxian', 'community', 'address', 'money',
                'subway', 'peizhi', 'describe']
# print(text.min)
# print(text.head(2))


# 1. 分析各城区租赁信息
data_groupby_partition = text.groupby(by='quxian')['quxian'].count()
print(data_groupby_partition)
print(data_groupby_partition.values)
print(data_groupby_partition.index)


# 饼图
explode = [0, 0, 0, 0, 0, 0, 0, 0]
plt.figure(figsize=(6, 6))
plt.pie(x=data_groupby_partition.values, explode=explode, labels=data_groupby_partition.index, autopct='%.1f%%')
plt.title("济南市公共住房租赁数量统计")
# plt.savefig("成都市六大城区公共住房租赁数量统计-饼图.jpg")
plt.show()


# 条形图
x = range(8)
plt.bar(x, data_groupby_partition.values)
for x, y in zip(range(8), data_groupby_partition.values):
    plt.text(x + 0.05, y + 0.05, '%d' % y, ha='center', va='bottom')
plt.title("济南市公共住房租赁数量统计", fontproperties=font_set)
plt.xticks(range(8), data_groupby_partition.index)
# plt.savefig("./成都市六大城区公共住房租赁数量统计-条形图.jpg")
plt.show()


# 2.分析最受欢迎的小区
text.groupby(by=['quxian', 'community'])['community'].count().sort_values(ascending=False).head(15).sort_values().plot(
    kind='barh', figsize=(8, 4))
plt.title("最受欢迎的小区Top-15", fontproperties=font_set)
plt.tight_layout()
plt.ylabel("城区/小区", fontproperties=font_set)
plt.xlabel("租赁数", fontproperties=font_set)
# plt.savefig("./最受欢迎的小区Top-15.jpg")
plt.show()


# 3. 按城区分析最受欢迎的户型
text.groupby(by=['quxian', 'type'])['type'].count().sort_values(ascending=False).head(15).sort_values().plot(
    kind='barh', figsize=(8, 4))
plt.title("济南市最受欢迎的户型Top-15")
plt.tight_layout()
plt.ylabel("城区/户型")
plt.xlabel("数量")
# plt.savefig("./六城区最受欢迎的户型Top15.jpg")
plt.show()

#
# # 1张图-六城区总的房间大小分区统计
# max = text["money"].max()
# min = text["money"].min()
# # 设置分组
# limit = range(int(min - min % 10), int(max + 10), 1000)
# # 进行分组
# size_limit_group = pd.cut(text["money"], limit, right=False)
# # 分组后的计数
# size_group_count = size_limit_group.value_counts()
# # 是否需要取样、排序。。。
# data_sort = size_limit_group.value_counts()#.sample(frac=1)#.sort_values()
# # 按照大小间隔排序，避免重叠
# # 如:1 2 3 4 5 6 7  ->  7 2 5 4 3 6 1
# # print(data_sort)
# for x in data_sort.index:
#     if data_sort[x]==0:
#         del data_sort[x]
# length = len(data_sort.values)
# indexs = [str(x) for x in data_sort.index]
#
# for i, j in zip(range(0, length, 2), range(length-1, 0, -2)):
#     if j <= i:
#         break
#     data_sort.iloc[i],data_sort.iloc[j] = data_sort.iloc[j],data_sort.iloc[i]
#     indexs[i], indexs[j] = indexs[j], indexs[i]
#     data_sort = pd.Series(data_sort.values, index=indexs)
# # print(data_sort)
# # 绘图
# plt.pie(data_sort.values, labels=[str(x) for x in data_sort.index],autopct='%1.1f%%')
# plt.title("租赁房大小比例(m^2)")
# plt.tight_layout()
# plt.savefig("./租赁房大小比例(m^2).jpg")
# plt.show()


# 3. 按城区分析最受欢迎的户型
text.groupby(by=['quxian', 'mode'])['mode'].count().sort_values(ascending=False).head(15).sort_values().plot(
    kind='barh', figsize=(8, 4))
plt.title("济南市最受欢迎的户型Top-15")
plt.tight_layout()
plt.ylabel("城区/户型")
plt.xlabel("数量")
# plt.savefig("./六城区最受欢迎的户型Top15.jpg")
plt.show()

# 3. 按城区分析最受欢迎的户型
text.groupby(by=['quxian', 'floor'])['floor'].count().sort_values(ascending=False).head(15).sort_values().plot(
    kind='barh', figsize=(8, 4))
plt.title("济南市最受欢迎的户型Top-15")
plt.tight_layout()
plt.ylabel("城区/户型")
plt.xlabel("数量")
# plt.savefig("./六城区最受欢迎的户型Top15.jpg")
plt.show()


# 3. 按城区分析最受欢迎的户型
text.groupby(by=['size'])['size'].count().sort_values(ascending=False).head(15).sort_values().plot(kind='barh',
                                                                                                   figsize=(8, 4))
plt.title("济南市最受欢迎的户型Top-15")
plt.tight_layout()
plt.ylabel("城区/户型")
plt.xlabel("数量")
# plt.savefig("./六城区最受欢迎的户型Top15.jpg")
plt.show()


peizhi = {}
for i in text['peizhi']:
    a = re.compile('\'(.*?)\'').findall(i)
    for m in a:
        if m in peizhi.keys():
            peizhi[m] += 1
        else:
            peizhi[m] = 1

xin = sorted(peizhi.items(), key=lambda x: x[1], reverse=True)
print(xin)
mm = [i[0] for i in xin[0:15]][::-1]
mm1 = [i[1] for i in xin[0:15]][::-1]
plt.barh(range(len(mm1)), mm1, tick_label=mm)

plt.title("济南市最受欢迎的户型Top-15")
plt.tight_layout()
plt.ylabel("城区/户型")
plt.xlabel("数量")
plt.show()


stop_file = open('stop_word.txt', 'r', encoding='utf-8')
stop_text = stop_file.readlines()
stop_file.close()
stop_words = str([word for word in stop_text])
a = text.groupby('quxian').count()
data = text.groupby('quxian')['describe'].apply(lambda x: x.str.cat(sep=':')).reset_index()
n = 0
print(stop_words)
for i in data['describe']:
    cut_text = ' '.join(jieba.cut(i))
    words = cut_text.split()
    words2 = [re.sub('[\,\?\.\:\'\"\-1234567890]', '', word) for word in words]
    word_index = set(words2)
    #     print(word_index)
    word_index1 = [word for word in word_index if word not in stop_words]
    print(word_index1)
    dic_words = {word: words2.count(word) for word in word_index1}
    #     print(dic_words)
    image = im.open('danghui.jpg')  # 打开图片
    graph = np.array(image)
    wc = WordCloud(
        background_color='white',
        mask=graph,
        font_path="C:/Windows/Fonts/STKAITI.TTF",
        max_font_size=150,
        min_font_size=5)


    wc.generate_from_frequencies(dic_words)

    wc.to_file(f'wordcloud/s{n}.jpg')
    n += 1
    plt.imshow(wc)
    plt.axis("off")  # 去除坐标轴
    plt.show()

