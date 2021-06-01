import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from random import sample
import graphviz
from sklearn import tree

data = pd.read_csv('Iris.csv')
# print(data)
iris_in = np.array(data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']])
target = np.array(data['class'])

# print(iris_in)
# print(type(iris_in))
# print(target)

tr_index = sample(range(0, 50), 40)
tr_index.extend(sample(range(50, 100), 40))
tr_index.extend(sample(range(100, 150), 40))
te_index = [i for i in range(0, 150) if i not in tr_index]
# print(te_index)
# 训练集的输入
tr_in = iris_in[tr_index]
# 训练集的输出
tr_out = target[tr_index]
# 测试集的输入
te_in = iris_in[te_index]
# print(type(tr_in))
# 模型训练
model = DecisionTreeClassifier(criterion='entropy').fit(tr_in, tr_out)
# 模型输出
res = model.predict(te_in)
print(res)
# 真实值
print(target[te_index])
# 准确率
print(sum(res == target[te_index])/len(res))
#

# dot_data = tree.export_graphviz(model, out_file=None)
# graph = graphviz.Source(dot_data)
# graph.render("iris")

dot_data = tree.export_graphviz(model, out_file=None,
                                feature_names=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'],
                                class_names=['setosa', 'versicolor', 'virginica'],
                                filled=True, rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("iris")
