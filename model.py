# -*- coding: utf-8 -*- 
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler    #引入缩放的包
from sklearn.metrics import mean_squared_error
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split # 分割数据模块
import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 取数据

def main(state, lowstate):

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

    # X数据集　对比之后发现线性回归残差最小
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

    yvar = ['coalVT','coalVA','coalVC','coalVI','coalVR',
            'ngVT','ngVA','ngVC','ngVI','ngVR',
            'petroVT','petroVA','petroVC','petroVI','petroVR',
            'reVT','reVA','reVC','reVI','reVR','nuVT']
    yvart = ['coalVT','ngVT','petroVT','reVT','nuVT']
    result = []
    sublist = []
    sublist.append('VAR')
    sublist.append('MBE')
    sublist.append('R2')
    result.append(sublist)
    itr = len(yvar)
    for k in range(0, len(yvar)):
        print(yvar[k])
        sublist = []
        str = yvar[k]
        sublist.append(str)
        csvFile = open("data/energyprofile_"+lowstate+".csv", "r")
        reader = csv.reader(csvFile)  # 返回的是迭代类型
        y = []
        count = 0
        for line in reader:
            count += 1
            if (count == (k+1)):
                for i in range(10, 50):
                    y.append(float(line[i]))
        csvFile.close()

        #　分割数据
        X_TRAIN, X_TEST, y_train, y_test = train_test_split(X, y, random_state=4)

        # 归一化操作
        scaler = StandardScaler()   
        scaler.fit(X)
        x_train = scaler.transform(X_TRAIN)
        x_test = scaler.transform(X_TEST)
        # print("x_train")
        # print(x_train)
        # print("x_test")
        # print(x_test)

        # 线性模型拟合
        model = linear_model.LinearRegression()
        model.fit(x_train, y_train)

        #预测结果
        # y_pret = model.predict(x_test)
        # # y_true = np.array(y_true)
        # y_test = np.array(y_test)
        # y_pret = np.array(y_pret)
        # print(y_pret)
        # print(y_test)
        # print(x_test)
        fig = plt.figure()
        ax = Axes3D(fig)
        plot_X = np.arange(0, 1, 0.05)
        plot_Y = np.arange(0, 1, 0.05)
        plot_X, plot_Y = np.meshgrid(plot_X, plot_Y)
        plot_X_test = []
        # print(plot_X)
        # print(plot_Y)
        for i in range(0, len(plot_X)):
            col = []
            for j in range(0, len(plot_Y)):
                sublist = []
                sublist.append(.1)
                sublist.append(float(plot_X[i][j]))
                sublist.append(float(plot_Y[i][j]))
                sublist.append(float(plot_X[i][j])*float(plot_Y[i][j]))
                # print(plot_X[i][j])
                # print(plot_Y[i][j])
                # print(plot_X_test)
                col.append(sublist)
            pret = model.predict(col)
            plot_X_test.append(pret)
        # print(plot_X_test)
        plot_Z = np.array(plot_X_test)
        # plot_Z = model.predict(plot_X_test)
        # plot_X, plot_Y = np.meshgrid(plot_X, plot_Y)
        ax.plot_surface(plot_X, plot_Y, plot_Z, rstride=1, cstride=1, cmap='rainbow')
        plt.xlabel('TPOPP')
        plt.ylabel('GDPRV')
        plt.title(yvar[k])
        # plt.show()
        # plt.savefig('fig/'+state+'_'+yvar[k]+'.png')
        plt.close()
        # break
    #     error = mean_absolute_error(y_test, y_pret)
    #     print(error)
    #     sublist.append(error)
    #     # error = mean_squared_error(y_test, y_pret)
    #     # print(error)
    #     # error = explained_variance_score(y_test, y_pret)
    #     # print(error)
    #     error = r2_score(y_test, y_pret)
    #     print(error)
    #     sublist.append(error)
    #     result.append(sublist)

    # with open('data/model_error_'+lowstate+'.csv','w') as fout:
    #     writer=csv.writer(fout) 
    #     for i in result:   
    #         writer.writerows([i])

    # 用mbe而不用mse的原因是数据很小，平方后减小了误差
    # 用r2的原因（上网查）


state = ['CA','AZ','TX','NM']
lowstate = ['ca','az','tx','nm']

for i in range(0,1):
    main(state[i], lowstate[i])

# population
# ca_2025
# 42326397
# ca_2050
# 49077801
# 
# gdp https://knoema.com/qhswwkc/us-gdp-growth-forecast-2017-2022-and-up-to-2060-data-and-charts
# 2019 2.64
# 2020 2.56
# 2025 2.40
# 2030 2.28
# 2035 2.04
# 2040 1.82
# 2045 1.66
# 2050 1.54

