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

def main(state, lowstate, TETCB):
    # print(TETCB)
    TETCB = TETCB[10:50]
    # print(len(x3))
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

    x3 = []
    for i in range(0, len(x2)):
        value = TETCB[i]/x2[i]
        x3.append(value)
    

    # X数据集　对比之后发现线性回归残差最小
    X = []
    for i in range(0, 40):
        sublist = []
        sublist.append(.1)
        sublist.append(x1[i])
        # sublist.append(x1[i]*x1[i])
        sublist.append(x2[i])
        sublist.append(x3[i])
        # sublist.append(x2[i]*x2[i])
        # sublist.append(x1[i]*x2[i])
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

        # 预测结果
        y_pret = model.predict(x_test)
        # y_true = np.array(y_true)
        y_test = np.array(y_test)
        y_pret = np.array(y_pret)
        print(y_pret)
        print(y_test)
   
        error = mean_absolute_error(y_test, y_pret)
        print(error)
        sublist.append(error)
        # error = mean_squared_error(y_test, y_pret)
        # print(error)
        # error = explained_variance_score(y_test, y_pret)
        # print(error)
        error = r2_score(y_test, y_pret)
        print(error)
        sublist.append(error)
        result.append(sublist)

    with open('data/model2.0_error_'+lowstate+'.csv','w') as fout:
        writer=csv.writer(fout) 
        for i in result:   
            writer.writerows([i])

    # 用mbe而不用mse的原因是数据很小，平方后减小了误差
    # 用r2的原因（上网查）


state = ['CA','AZ','TX','NM']
lowstate = ['ca','az','tx','nm']
TETCB_CA = [7829908, 8220888, 8454960, 8898981, 9615445, 9952396, 10613232, 10994485, 11687466, 12089963, 12379229, 12822900, 13140407, 13671746, 12884583, 13232657, 13589692, 14416114, 14398485, 15221394, 14449249, 13811082, 12895309, 13000760, 13960107, 14190992, 13734790, 14863050, 15151486, 16137891, 16066308, 15702018, 15931904, 15622595, 16107473, 15826507, 15940110, 16067866, 16776255, 16863840, 17325415, 17377789, 17220287, 16964213, 17703917, 17551890, 17900955, 17924834, 17329902, 16704446, 16584634, 16451866, 16222783, 16428480, 16327611, 16506589]
TETCB_AZ = [652609, 705735, 752425, 795125, 818235, 813138, 883901, 898968, 1002779, 1097799, 1135127, 1211580, 1352244, 1482406, 1539817, 1506694, 1647438, 1819115, 1831871, 1998636, 1949565, 2095969, 1997238, 1987219, 2141999, 2238397, 2222107, 2242337, 2427659, 2440921, 2492732, 2553599, 2658367, 2658581, 2799125, 2781878, 2890351, 3022916, 3191995, 3304692, 3488935, 3527825, 3548521, 3594083, 3845536, 3858147, 3965239, 4091210, 4126357, 3828692, 3839197, 3827588, 3793364, 3883128, 3860962, 3880260]
TETCB_TX = [712129, 735436, 810284, 831975, 858084, 875977, 910415, 993100, 1045567, 1049150, 1203737, 1247629, 1334314, 1323706, 1342401, 1302583, 1403973, 1360296, 1323030, 1344197, 1424206, 1382270, 1405050, 1478711, 1430382, 1425828, 1336816, 1432468, 1493808, 1571136, 1679036, 1584958, 1635558, 1683423, 1677948, 1641966, 1685962, 1788131, 1786452, 1805016, 1867804, 1847900, 1787589, 1834383, 1874625, 1914357, 1954559, 1976391, 1902381, 1883747, 1815657, 1888561, 1843675, 1837127, 1777128, 1777266]
TETCB_NM = [9868859, 9974309, 10500846, 11224380, 11583254, 12016438, 12864482, 13591693, 14510123, 15467470, 16088365, 16855849, 17931473, 19306714, 19080983, 17914808, 18783504, 20501939, 21727978, 22779326, 23214807, 22407398, 20834444, 20678143, 21935710, 22103463, 22150079, 22637250, 24016641, 24841661, 25371477, 25326176, 25783319, 26170853, 26735960, 27070041, 28867171, 29926756, 30416497, 29715582, 30548129, 30004636, 30688709, 30219360, 30456714, 29302936, 29429793, 29103982, 27685333, 26571227, 28193366, 28843111, 28848216, 30297068, 30320166, 30806649]
TETCB = []
TETCB.append(TETCB_CA)
TETCB.append(TETCB_AZ)
TETCB.append(TETCB_NM)
TETCB.append(TETCB_TX)
for i in range(0,len(state)):
    main(state[i], lowstate[i], TETCB[i])