import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
import graphviz

watermelon = pd.read_csv('西瓜集.csv')
# print(watermelon)

watermelon['色泽'] = watermelon['色泽'].map({"乌黑": 0, "浅白": 1, "青绿": 2}).astype(int)
watermelon['根蒂'] = watermelon['根蒂'].map({"硬挺": 0, "稍蜷": 1, "蜷缩": 2}).astype(int)
watermelon['敲声'] = watermelon['敲声'].map({"沉闷": 0, "浊响": 1, "清脆": 2}).astype(int)
watermelon['纹理'] = watermelon['纹理'].map({"模糊": 0, "清晰": 1, "稍糊": 2}).astype(int)
watermelon['脐部'] = watermelon['脐部'].map({"凹陷": 0, "平坦": 1, "稍凹": 2}).astype(int)
watermelon['触感'] = watermelon['触感'].map({"硬滑": 0, "软粘": 1}).astype(int)
watermelon['好瓜'] = watermelon['好瓜'].map({"否": 0, "是": 1}).astype(int)

# print(watermelon)

watermelon_data_tr_in = watermelon.drop(columns=["好瓜"])
# print(watermelon_data_tr_in)

watermelon_data_tr_out = watermelon["好瓜"]
# print(watermelon_data_tr_out)
x_train, x_test, y_train, y_test = train_test_split(watermelon_data_tr_in, watermelon_data_tr_out, test_size=0.3, random_state=1)

# 模型训练
model = tree.DecisionTreeClassifier(criterion="entropy").fit(x_train,y_train)
res = model.predict(x_test)
print(res)
print(y_test)
print(sum(res==y_test)/len(res))

# dot_data = tree.export_graphviz(model, out_file=None)
# graph = graphviz.Source(dot_data)
# graph.render("watermelon")
dot_data = tree.export_graphviz(model, out_file=None,
                                feature_names=['SeZe', 'GenDi', 'QiangSheng', 'WenLi', 'QiBu', 'ChuGan'],
                                class_names=['YES', 'NO'],
                                filled=True, rounded=True,
                                special_characters=True,)
graph = graphviz.Source(dot_data)
graph.render("watermelon2")
