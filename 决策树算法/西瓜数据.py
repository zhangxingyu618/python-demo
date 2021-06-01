import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.neural_network import MLPClassifier

import graphviz

watermelon = pd.read_csv('西瓜集.csv')
# print(watermelon)
cat_features = ['色泽', '根蒂', '敲声', '纹理', '脐部', '触感']
# print(cat_features)
watermelon_oneHot = pd.get_dummies(watermelon, columns=cat_features)
# print(watermelon_oneHot)
watermelon_oneHot["好瓜"] = watermelon_oneHot["好瓜"].map({"是": 1, "否": 0}).astype(int)
# print(watermelon_oneHot)
watermelon_data_tr_in = watermelon_oneHot.drop(columns=["好瓜"])
# print(watermelon_data_tr_in)

watermelon_data_tr_out = watermelon_oneHot["好瓜"]
# print(watermelon_data_tr_out)
x_train, x_test, y_train, y_test = train_test_split(watermelon_data_tr_in, watermelon_data_tr_out, test_size=0.3, random_state=1)

# 模型训练
model = tree.DecisionTreeClassifier(criterion="entropy").fit(x_train,y_train)
res = model.predict(x_test)

print(res)
print(y_test)
print(sum(res==y_test)/len(res))

dot_data = tree.export_graphviz(model, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("watermelon")
