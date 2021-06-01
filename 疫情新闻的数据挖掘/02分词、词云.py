import webbrowser
import jieba
import pandas as pd
from collections import Counter
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType

# 读取csv，保存txt中
data = pd.read_csv('中国社会组织_疫情防控.csv', encoding='utf-8')
with open('news_data.txt', 'w', encoding='utf-8') as f:
    for line in data.values:
        f.write((str(line[0]) + ',' + str(line[3]) + '\n'))

# 分词
cut_words = ""
all_words = ""
f = open('news_data_fenci.txt', 'w', encoding='utf-8')
for line in open('news_data.txt', encoding='utf-8'):
    line.strip('\n')
    seg_list = jieba.cut(line, cut_all=False)
    # print(" ".join(seg_list))
    cut_words = (" ".join(seg_list))
    f.write(cut_words)
    all_words += cut_words
else:
    f.close()

# 输出结果
all_words = all_words.split()
print(all_words)

# 词频统计
c = Counter()
for x in all_words:
    if len(x) > 1 and x != '\r\n':
        c[x] += 1
print(c.most_common(10))
# 输出词频最高的前10个词
print('\n词频统计结果：')
for (k, v) in c.most_common(10):
    print("%s:%d" % (k, v))

# 存储数据
name = "分词统计结果.csv"
fw = open(name, 'w', encoding='utf-8')
i = 1
for (k, v) in c.most_common(len(c)):
    fw.write(str(i) + ',' + str(k) + ',' + str(v) + '\n')
    i = i + 1
else:
    print("统计结果保存完毕")
    fw.close()

# 词云
words = []
for (k, v) in c.most_common(1000):
    # print(k, v)
    words.append((k, v))


# py echarts的词云图
def wordcloud_base() -> WordCloud:
    c = (
        WordCloud()
            .add("疫情词云图", words, word_size_range=[20, 100], shape=SymbolType.ROUND_RECT)
            .set_global_opts(title_opts=opts.TitleOpts(title='全国新型冠状病毒疫情词云图'))
    )
    return c


# 生成图
wordcloud_base().render('疫情词云图.html')
webbrowser.open("疫情词云图.html")
