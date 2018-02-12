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

def predict(state, lowstate, gdp, pop):

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
    x1_all = 0
    x2_all = 0
    for i in range(0, 40):
        sublist = []
        sublist.append(.1)
        sublist.append(x1[i])
        sublist.append(x2[i])
        X.append(sublist)
        x1_all += x1[i]
        x2_all += x2[i]
    gdp = (gdp - x2_all/len(x2))/gdp
    pop = (pop - x1_all/len(x1))/pop
    test1 = [[-1. , pop, gdp]]
    # test1.append(.1)
    # test1.append(pop)
    # test1.append(gdp)
    # test1 = np.asarray(test1)
    yvar = ['coalVT','coalVA','coalVC','coalVI','coalVR',
            'ngVT','ngVA','ngVC','ngVI','ngVR',
            'petroVT','petroVA','petroVC','petroVI','petroVR',
            'reVT','reVA','reVC','reVI','reVR','nuVT']
    yvart = ['coalVT','ngVT','petroVT','reVT','nuVT']
    result = []
    sublist = []
    sublist.append('VAR')
    sublist.append('Predict value')
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
        print(x_train)
        # print("x_test")
        print(x_test)

        # 线性模型拟合
        model = linear_model.LinearRegression()
        model.fit(x_train, y_train)

        #预测结果
        y_pret = model.predict(test1)
        print(y_pret)
        sublist.append(y_pret[0])
        print(sublist)
        result.append(sublist)
    print(result)
    with open('data/model_pret2050_'+lowstate+'.csv','w') as fout:
        writer=csv.writer(fout) 
        for i in result:   
            writer.writerows([i])


# we use million
# ca_2016 $2.623 trillion 2623000 Million
# https://en.wikipedia.org/wiki/Economy_of_California
# az_2016 267472 million
# http://www.deptofnumbers.com/gdp/arizona/ 
# ca_2025
# 42326397
# ca_2050
# 49077801
# az
# 7944800
# 10820900

# gdp https://knoema.com/qhswwkc/us-gdp-growth-forecast-2017-2022-and-up-to-2060-data-and-charts
# 2019 2.64
# 2020 2.56
# 2025 2.40
# 2030 2.28
# 2035 2.04
# 2040 1.82
# 2045 1.66
# 2050 1.54

def gdp(start, end):
    rate = 1
    #           16   17    18    19    20    21    22    23    24    25
    growth = [2.64, 2.64, 2.64, 2.64, 2.56, 2.40, 2.40, 2.40, 2.40, 2.40]
    for i in range(0, end-start):
        rate = rate * (1+growth[i]/100.)
        print(rate)
    return rate

def gdp2(start, end):
    rate = 1
    for i in range(0, end-start):
        rate = rate * (1+1.82/100.)
        print(rate)
    return rate

state = ['CA','AZ','TX','NM']
lowstate = ['ca','az','tx','nm']

# for i in range(0,1):
    # main(state[i], lowstate[i])

print(gdp(2016,2025))
ca_gdp_2016 = 2623000
ca_gdp = ca_gdp_2016 * gdp(2016, 2025)
ca_pop = 42326397
ca_gdp2 = ca_gdp * gdp2(2025, 2050)
ca_pop2 = 49077801

az_gdp_2016 = 267472
az_gdp = az_gdp_2016 * gdp(2016, 2025)
az_pop = 7944800 
az_gdp2 = az_gdp * gdp2(2025, 2050)
az_pop2 = 10820900

nm_gdp_2016 = 93600  #https://www.bea.gov/regional/bearfacts/pdf.cfm?fips=35000&areatype=STATE&geotype=3
nm_gdp = nm_gdp_2016 * gdp(2016, 2025)
nm_pop = 2700000 #https://unmwest.unm.edu/common/docs/reports/B_Projections_Summary_Narrative.pdf
nm_gdp2 = nm_gdp * gdp2(2025, 2050)
nm_pop2 = 3318289  #　35年　3018289

tx_gdp_2016 = 1498881 #http://www.deptofnumbers.com/gdp/texas/
tx_gdp = tx_gdp_2016 * gdp(2016, 2025)
tx_pop = (33628653+37736338)/2
tx_gdp2 = tx_gdp * gdp2(2025, 2050)
tx_pop2 = 42928264
# 2050 tx_pop = 41,928,264
# 2040 45000000 #http://www.sahcc.org/wp-content/uploads/Texas-Population-Growth-Projections-and-Implications.pdf

predict(state[3], lowstate[3], tx_gdp2, tx_pop2)
