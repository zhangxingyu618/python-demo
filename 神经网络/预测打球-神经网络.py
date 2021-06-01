import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

ball_data = pd.read_csv('ball.csv')

# print(ball_data)
cat_features = ['Outlook', 'Temperature', 'Humidity', 'Windy']
# print(cat_features)
ball_data_oneHot = pd.get_dummies(ball_data, columns=cat_features)
# print(ball_data_oneHot)
ball_data_oneHot["Play"] = ball_data_oneHot['Play'].map({"No": 0, "Yes": 1}).astype(int)
# print(ball_data_oneHot["Play"])

ball_data_tr_in = ball_data_oneHot.drop(columns=["Play"])
# print(ball_data_tr_in)
ball_data_tr_out = ball_data_oneHot["Play"]
# print(ball_data_tr_out)
X_train, X_test, Y_train, Y_test = train_test_split(ball_data_tr_in, ball_data_tr_out, test_size=0.3, random_state=1)
# print(X_train)
# print(Y_train)
net = MLPClassifier(hidden_layer_sizes=10, max_iter=500).fit(X_train, Y_train)
# print(model)

res = net.predict(X_test)
print(res)
print(Y_test)
print(sum(res == Y_test)/len(res))

