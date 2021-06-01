import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

if __name__ == "__main__":

    # 计算TFIDF

    # 文档预料 空格连接
    corpus = []
    # 读取预料 一行预料为一个文档
    for line in open('news_data_fenci.txt', 'r', encoding='utf-8').readlines():
        corpus.append(line.strip())
    # 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
    vectorizer = CountVectorizer()
    # 该类会统计每个词语的tf-idf权值
    transformer = TfidfTransformer()
    # 第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    # print(vectorizer.fit_transform(corpus))
    # 将tf-idf矩阵抽取出来 元素a[i][j]表示j词在i类文本中的tf-idf权重
    weight = tfidf.toarray()

    # 获取词袋模型中的所有词语
    word = vectorizer.get_feature_names()
    print(word)
    print("=================")
    print(weight)
    # 打印特征向量文本内容
    # print('Features length: ' + str(len(word)))

    # 聚类 K-means
    print('K-means聚类')
    from sklearn.cluster import KMeans
    # 聚类k值
    clf = KMeans(n_clusters=2)
    # print(clf)
    pre = clf.fit_predict(weight)
    # print(pre)

    # 中心点
    # print(clf.cluster_centers_)
    # print(clf.inertia_)

    # 图形输出 降维
    # PCA算法其表现形式是降维，同时也是一种特征融合算法
    from sklearn.decomposition import PCA

    pca = PCA(n_components=2)  # 输出两维
    newData = pca.fit_transform(weight)  # 载入N维
    # print(newData)

    x = [n[0] for n in newData]
    y = [n[1] for n in newData]

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.scatter(x, y, c=pre, s=100)
    # plt.legend()
    plt.title("k-means 聚类")
    plt.show()
