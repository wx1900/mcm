# -*- coding: utf-8 -*- 
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler    #引入缩放的包
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split # 分割数据模块
from sklearn.cross_validation import cross_val_score # K折交叉验证模块
import csv
import numpy as np

# 取数据
state = 'TX'
csvFile = open("data/TPOPP.csv", "r")
reader = csv.reader(csvFile)  # 返回的是迭代类型
x1 = []
count = 0
for line in reader:
    if (line[0] == state):
        count += 1
        if (count > 10):
            x1.append(float(line[2]))    
csvFile.close()

csvFile = open("data/GDPRV.csv", "r")
reader = csv.reader(csvFile)  # 返回的是迭代类型
x2 = []
for line in reader:
    if (line[0] == state):
        x2.append(float(line[2]))
csvFile.close()
# 取potVT做实验
csvFile = open("data/energyprofile_tx.csv", "r")
reader = csv.reader(csvFile)  # 返回的是迭代类型
y = []
y_true = []
count = 0
for line in reader:
    count += 1
    if (count == 11):
        for i in range(10, 50):
            y.append(float(line[i]))
csvFile.close()

X = []
for i in range(0, 40):
    sublist = []
    sublist.append(.1)
    sublist.append(x1[i])
    # sublist.append(x1[i]*x1[i])
    sublist.append(x2[i])
    # sublist.append(x2[i]*x2[i])
    sublist.append(x1[i]*x2[i])
    X.append(sublist)

#　分割数据
X_TRAIN, X_TEST, y_train, y_test = train_test_split(X, y, random_state=4)

# 归一化操作
scaler = StandardScaler()   
scaler.fit(X)
x_train = scaler.transform(X_TRAIN)
x_test = scaler.transform(X_TEST)
print("x_train")
print(x_train)
print("x_test")
print(x_test)

# 线性模型拟合
model = linear_model.LinearRegression()
model.fit(x_train, y_train)

#预测结果
y_pret = model.predict(x_test)
# y_true = np.array(y_true)
y_test = np.array(y_test)
y_pret = np.array(y_pret)
print(y_pret)
print(y_test)
error = mean_squared_error(y_test, y_pret)
print(error)