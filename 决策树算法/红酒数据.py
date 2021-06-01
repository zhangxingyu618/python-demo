from sklearn.datasets import load_wine
from random import sample
from sklearn.tree import DecisionTreeClassifier

wine = load_wine()
# print(wine)
tr_index = sample(range(0, 50), 40)
tr_index.extend(sample(range(50, 100), 40))
tr_index.extend(sample(range(100, 150), 40))
te_index = [i for i in range(0, 150) if i not in tr_index]
# 训练集的输入
tr_in = wine.data[tr_index]
# 训练集的输出
tr_out = wine.target[tr_index]
# 测试集的输入
te_in = wine.data[te_index]
# 模型训练
model = DecisionTreeClassifier(criterion="entropy").fit(tr_in, tr_out)
res = model.predict(te_in)
print(res)
print(wine.target[te_index])
print(sum(res == wine.target[te_index])/len(res))