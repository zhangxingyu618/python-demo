from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from random import sample
from sklearn.metrics import precision_score

iris = load_iris()
print(iris)
tr_index = sample(range(0, 50), 40)
tr_index.extend(sample(range(50, 100), 40))
tr_index.extend(sample(range(100, 150), 40))
te_index = [i for i in range(0, 150) if i not in tr_index]
# print(te_index)
# 训练集的输入
tr_in = iris.data[tr_index]
# 训练集的输出
tr_out = iris.target[tr_index]
# 测试集的输入
te_in = iris.data[te_index]
# print(type(tr_in))
# 模型训练
model = DecisionTreeClassifier(criterion='entropy').fit(tr_in, tr_out)
# 模型输出
res = model.predict(te_in)
print(res)
# 真实值
print(iris.target[te_index])
# 准确率
print(sum(res == iris.target[te_index])/len(res))

print(precision_score(iris.target[te_index], res, average='micro'))
# 导出模型
# joblib.dump(model, 'DTC.model')
# model_DTC = joblib.load('DTC.model')
# model_DTC.predict(te_in)

