# -*- coding: utf-8 -*- 
import csv
import numpy as np
import matplotlib.pyplot as plt

# 计算物种主要能源消耗占总行业的比以及每种能源消耗在四个行业中的占比

state = 'ca'

#　读取
csvFile = open("data/"+state+".csv", "r")
reader = csv.reader(csvFile)  # 返回的是迭代类型
data = []
for line in reader:
    data.append(line)
csvFile.close()

# todo : 指标可能与数据不符重新划分

# Coal
coal = ['CL', 'CC']
# Natrual Gas
ng = ['NG']
# Potroleum
potroleum = ['AB','AR','AV','CO','DF','FN','FO','FS','JF','KS',
            'LG','LU','MB','MG','MS','PC','RF',
            'NA','PL','PP','SN','SG','US','WX','UO']
# Renewable energy
re = ['EN','EM','GE','HY','SO','WY','WW','WD']
# Nuclear electric power
nu = ['NU']

coalData = []
ngData = []
potData = []
reData = []
nuData = []
TETCB = []
TERCB = []
TEACB = []
TECCB = []
TEICB = []

for i in data:
    for j in range(0, len(coal)):
        if (i[0][0:2] == coal[j]):
            coalData.append(i)

    for j in range(0, len(ng)):
        if (i[0][0:2] == ng[j]):
            ngData.append(i)

    for j in range(0, len(potroleum)):
        if (i[0][0:2] == potroleum[j]):
            potData.append(i)

    for j in range(0, len(re)):
        if (i[0][0:2] == re[j]):
            reData.append(i)

    for j in range(0, len(nu)):
        if (i[0][0:2] == nu[j]):
            nuData.append(i)
    if (i[0] == 'TETCB'):
        TETCB.append(i[1:])
    elif (i[0] == 'TERCB'):
        TERCB.append(i[1:])
    elif (i[0] == 'TECCB'):
        TECCB.append(i[1:])
    elif (i[0] == 'TEICB'):
        TEICB.append(i[1:])
    elif (i[0] == 'TEACB'):
        TEACB.append(i[1:])
print("\nTETCB\n")
print(TETCB)
print("\ncoal\n")
coalACB = []
coalCCB = []
coalRCB = []
coalICB = []
coalTCB = []
# 分离出每个产业和总的消耗
for i in coalData:
    var = i[0]
    for j in coal:
        if (var == j+'ACB'):
            coalACB.append(i[1:])
        elif (var == j+'CCB'):
            coalCCB.append(i[1:])
        elif (var == j+'ICB'):
            coalICB.append(i[1:])
        elif (var == j+'RCB'):
            coalRCB.append(i[1:])
        elif (var == j+'TCB'):
            coalTCB.append(i[1:])

coalTotACB = []
coalTotCCB = []
coalTotRCB = []
coalTotICB = []
coalTotTCB = []
# 一大类能源中的每个小类相加
for i in range(0, len(coalACB)):
    if (i == 0):
        for j in range(0, len(coalACB[0])):
            value = int(coalACB[i][j])
            coalTotACB.append(value)
    else:
        for j in range(0, len(coalACB[0])):
            coalTotACB = int(coalTotACB[j]) + int(coalACB[j])
print(coalTotACB)
for i in range(0, len(coalCCB)):
    if (i == 0):
        for j in range(0, len(coalCCB[0])):
            value = int(coalCCB[i][j])
            coalTotCCB.append(value)
    else:
        for j in range(0, len(coalCCB[0])):
            coalTotCCB = int(coalTotCCB[j]) + int(coalCCB[j])
print(coalTotCCB)
for i in range(0, len(coalICB)):
    if (i == 0):
        for j in range(0, len(coalICB[0])):
            value = int(coalICB[i][j])
            coalTotICB.append(value)
    else:
        for j in range(0, len(coalICB[0])):
            coalTotICB = int(coalTotICB[j]) + int(coalICB[j])
print(coalTotICB)
for i in range(0, len(coalRCB)):
    if (i == 0):
        for j in range(0, len(coalRCB[0])):
            value = int(coalRCB[i][j])
            coalTotRCB.append(value)
    else:
        for j in range(0, len(coalRCB[0])):
            coalTotRCB = int(coalTotRCB[j]) + int(coalRCB[j])
print(coalTotRCB)
for i in range(0, len(coalTCB)):
    if (i == 0):
        for j in range(0, len(coalTCB[0])):
            value = int(coalTCB[i][j])
            coalTotTCB.append(value)
    else:
        for j in range(0, len(coalTCB[0])):
            coalTotTCB = int(coalTotTCB[j]) + int(coalTCB[j])
print(coalTotTCB)

# 煤在总的消耗中占比
coalVT = []

for i in range(0, len(coalTCB[0])):
    value = int(coalTCB[0][i])/(int(TETCB[0][i])+1.)
    coalVT.append(value)
print(coalVT)

# 煤在各行业消耗中占比
coalVA = []
coalVC = []
coalVI = []
coalVR = []

for i in range(0, len(TEACB[0])):
    value = int(coalTotACB[i]) / (int(TEACB[0][i])+1.)
    coalVA.append(value)
print(coalVA)

for i in range(0, len(TECCB[0])):
    value = int(coalTotCCB[i]) / (int(TECCB[0][i])+1.)
    coalVC.append(value)
print(coalVC)

for i in range(0, len(TEICB[0])):
    value = int(coalTotICB[i]) / (int(TEICB[0][i])+1.)
    coalVI.append(value)
print(coalVI)

for i in range(0, len(TERCB[0])):
    value = int(coalTotRCB[i]) / (int(TERCB[0][i])+1.)
    coalVR.append(value)
print(coalVR)

#

print("\nng\n")
ngACB = []
ngCCB = []
ngRCB = []
ngICB = []
ngTCB = []
# 分离出每个产业和总的消耗
for i in ngData:
    var = i[0]
    for j in ng:
        if (var == j+'ACB'):
            ngACB.append(i[1:])
        elif (var == j+'CCB'):
            ngCCB.append(i[1:])
        elif (var == j+'ICB'):
            ngICB.append(i[1:])
        elif (var == j+'RCB'):
            ngRCB.append(i[1:])
        elif (var == j+'TCB'):
            ngTCB.append(i[1:])

ngTotACB = []
ngTotCCB = []
ngTotRCB = []
ngTotICB = []
ngTotTCB = []
# 一大类能源中的每个小类相加
for i in range(0, len(ngACB)):
    if (i == 0):
        for j in range(0, len(ngACB[0])):
            value = int(ngACB[i][j])
            ngTotACB.append(value)
    else:
        for j in range(0, len(ngACB[0])):
            ngTotACB.append(int(ngTotACB[j]) + int(ngACB[i][j]))
print(ngTotACB)
for i in range(0, len(ngCCB)):
    if (i == 0):
        for j in range(0, len(ngCCB[0])):
            value = int(ngCCB[i][j])
            ngTotCCB.append(value)
    else:
        for j in range(0, len(ngCCB[0])):
            ngTotCCB.append(int(ngTotCCB[j]) + int(ngCCB[i][j]))
print(ngTotCCB)
for i in range(0, len(ngICB)):
    if (i == 0):
        for j in range(0, len(ngICB[0])):
            value = int(ngICB[i][j])
            ngTotICB.append(value)
    else:
        for j in range(0, len(ngICB[0])):
            ngTotICB.append(int(ngTotICB[j]) + int(ngICB[i][j]))
print(ngTotICB)
for i in range(0, len(ngRCB)):
    if (i == 0):
        for j in range(0, len(ngRCB[0])):
            value = int(ngRCB[i][j])
            ngTotRCB.append(value)
    else:
        for j in range(0, len(ngRCB[0])):
            ngTotRCB.append(int(ngTotRCB[j]) + int(ngRCB[i][j]))
print(ngTotRCB)
for i in range(0, len(ngTCB)):
    if (i == 0):
        for j in range(0, len(ngTCB[0])):
            value = int(ngTCB[i][j])
            ngTotTCB.append(value)
    else:
        for j in range(0, len(ngTCB[0])):
            ngTotTCB.append(int(ngTotTCB[j]) + int(ngTCB[i][j]))
print(ngTotTCB)

# 天然气在总的消耗中占比
ngVT = []

for i in range(0, len(ngTCB[0])):
    value = int(ngTCB[0][i])/(int(TETCB[0][i])+1.)
    ngVT.append(value)
print('\nVT\n')
print(ngVT)

# 天然气在各行业消耗中占比
ngVA = []
ngVC = []
ngVI = []
ngVR = []

for i in range(0, len(TEACB[0])):
    value = int(ngTotACB[i]) / (int(TEACB[0][i])+1.)
    ngVA.append(value)
print(ngVA)

for i in range(0, len(TECCB[0])):
    value = int(ngTotCCB[i]) / (int(TECCB[0][i])+1.)
    ngVC.append(value)
print(ngVC)

for i in range(0, len(TEICB[0])):
    value = int(ngTotICB[i]) / (int(TEICB[0][i])+1.)
    ngVI.append(value)
print(ngVI)

for i in range(0, len(TERCB[0])):
    value = int(ngTotRCB[i]) / (int(TERCB[0][i])+1.)
    ngVR.append(value)
print(ngVR)

#

print("\npot\n")
potACB = []
potCCB = []
potRCB = []
potICB = []
potTCB = []
# 分离出每个产业和总的消耗
for i in potData:
    var = i[0]
    for j in potroleum:
        if (var == j+'ACB'):
            potACB.append(i[1:])
        elif (var == j+'CCB'):
            potCCB.append(i[1:])
        elif (var == j+'ICB'):
            potICB.append(i[1:])
        elif (var == j+'RCB'):
            potRCB.append(i[1:])
        elif (var == j+'TCB'):
            potTCB.append(i[1:])

potTotACB = []
potTotCCB = []
potTotRCB = []
potTotICB = []
potTotTCB = []
# 一大类能源中的每个小类相加
for i in range(0, len(potACB)):
    if (i == 0):
        for j in range(0, len(potACB[0])):
            value = int(potACB[i][j])
            potTotACB.append(value)
    else:
        for j in range(0, len(potACB[0])):
            potTotACB.append(int(potTotACB[j]) + int(potACB[i][j]))
print(potTotACB)
for i in range(0, len(potCCB)):
    if (i == 0):
        for j in range(0, len(potCCB[0])):
            value = int(potCCB[i][j])
            potTotCCB.append(value)
    else:
        for j in range(0, len(potCCB[0])):
            potTotCCB.append(int(potTotCCB[j]) + int(potCCB[i][j]))
print(potTotCCB)
for i in range(0, len(potICB)):
    if (i == 0):
        for j in range(0, len(potICB[0])):
            value = int(potICB[i][j])
            potTotICB.append(value)
    else:
        for j in range(0, len(potICB[0])):
            potTotICB.append(int(potTotICB[j]) + int(potICB[i][j]))
print(potTotICB)
for i in range(0, len(potRCB)):
    if (i == 0):
        for j in range(0, len(potRCB[0])):
            value = int(potRCB[i][j])
            potTotRCB.append(value)
    else:
        for j in range(0, len(potRCB[0])):
            potTotRCB.append(int(potTotRCB[j]) + int(potRCB[i][j]))
print(potTotRCB)
for i in range(0, len(potTCB)):
    if (i == 0):
        for j in range(0, len(potTCB[0])):
            value = int(potTCB[i][j])
            potTotTCB.append(value)
    else:
        for j in range(0, len(potTCB[0])):
            potTotTCB.append(int(potTotTCB[j]) + int(potTCB[i][j]))
print(potTotTCB)

# 石油在总的消耗中占比
potVT = []

for i in range(0, len(potTCB[0])):
    value = int(potTCB[0][i])/(int(TETCB[0][i])+1.)
    potVT.append(value)
print('\nVT\n')
print(potVT)

# 石油在各行业消耗中占比
potVA = []
potVC = []
potVI = []
potVR = []

for i in range(0, len(TEACB[0])):
    value = int(potTotACB[i]) / (int(TEACB[0][i])+1.)
    potVA.append(value)
print(potVA)

for i in range(0, len(TECCB[0])):
    value = int(potTotCCB[i]) / (int(TECCB[0][i])+1.)
    potVC.append(value)
print(potVC)

for i in range(0, len(TEICB[0])):
    value = int(potTotICB[i]) / (int(TEICB[0][i])+1.)
    potVI.append(value)
print(potVI)

for i in range(0, len(TERCB[0])):
    value = int(potTotRCB[i]) / (int(TERCB[0][i])+1.)
    potVR.append(value)
print(potVR)

#
print("\nre\n")
reACB = []
reCCB = []
reRCB = []
reICB = []
reTCB = []

# 分离出每个产业和总的消耗
for i in reData:
    var = i[0]
    for j in re:
        if (var == j+'ACB'):
            reACB.append(i[1:])
        elif (var == j+'CCB'):
            reCCB.append(i[1:])
        elif (var == j+'ICB'):
            reICB.append(i[1:])
        elif (var == j+'RCB'):
            reRCB.append(i[1:])
        elif (var == j+'TCB'):
            reTCB.append(i[1:])
    # 数据中缺少WDTCB用其他值计算
    if (var == 'WDACB'):
        reTCB.append(i[1:])
    elif (var =='WDCCB'):
        reTCB.append(i[1:])
    elif (var == 'WDICB'):
        reTCB.append(i[1:])
    elif (var == 'WDRCB'):
        reTCB.append(i[1:])

reTotACB = []
reTotCCB = []
reTotRCB = []
reTotICB = []
reTotTCB = []
# 一大类能源中的每个小类相加
for i in range(0, len(reACB)):
    if (i == 0):
        for j in range(0, len(reACB[0])):
            value = int(reACB[i][j])
            reTotACB.append(value)
    else:
        for j in range(0, len(reACB[0])):
            reTotACB.append(int(reTotACB[j]) + int(reACB[i][j]))
print(reTotACB)
for i in range(0, len(reCCB)):
    if (i == 0):
        for j in range(0, len(reCCB[0])):
            value = int(reCCB[i][j])
            reTotCCB.append(value)
    else:
        for j in range(0, len(reCCB[0])):
            reTotCCB.append(int(reTotCCB[j]) + int(reCCB[i][j]))
print(reTotCCB)
for i in range(0, len(reICB)):
    if (i == 0):
        for j in range(0, len(reICB[0])):
            value = int(reICB[i][j])
            reTotICB.append(value)
    else:
        for j in range(0, len(reICB[0])):
            reTotICB.append(int(reTotICB[j]) + int(reICB[i][j]))
print(reTotICB)
for i in range(0, len(reRCB)):
    if (i == 0):
        for j in range(0, len(reRCB[0])):
            value = int(reRCB[i][j])
            reTotRCB.append(value)
    else:
        for j in range(0, len(reRCB[0])):
            reTotRCB.append(int(reTotRCB[j]) + int(reRCB[i][j]))
print(reTotRCB)
for i in range(0, len(reTCB)):
    if (i == 0):
        for j in range(0, len(reTCB[0])):
            value = int(reTCB[i][j])
            reTotTCB.append(value)
    else:
        for j in range(0, len(reTCB[0])):
            reTotTCB.append(int(reTotTCB[j]) + int(reTCB[i][j]))
print(reTotTCB)

# 可再生能源在总的消耗中占比
reVT = []

for i in range(0, len(reTCB[0])):
    value = int(reTCB[0][i])/(int(TETCB[0][i])+1.)
    reVT.append(value)
print('\nVT\n')
print(reVT)

# 可再生在各行业消耗中占比
reVA = []
reVC = []
reVI = []
reVR = []

for i in range(0, len(TEACB[0])):
    value = int(reTotACB[i]) / (int(TEACB[0][i])+1.)
    reVA.append(value)
print(reVA)

for i in range(0, len(TECCB[0])):
    value = int(reTotCCB[i]) / (int(TECCB[0][i])+1.)
    reVC.append(value)
print(reVC)

for i in range(0, len(TEICB[0])):
    value = int(reTotICB[i]) / (int(TEICB[0][i])+1.)
    reVI.append(value)
print(reVI)

for i in range(0, len(TERCB[0])):
    value = int(reTotRCB[i]) / (int(TERCB[0][i])+1.)
    reVR.append(value)
print(reVR)

# WD数据中缺少TCB 
# NUETB 表示核能的总消耗
# 核能只计算占总能源比例，不计算产业占比
print("nu\n")
NUETB = []
nuVT = []
for i in nuData:
    if (i[0] == 'NUETB'):
        NUETB.append(i[1:])
print(NUETB)
for i in range(0, len(NUETB[0])):
    value = int(NUETB[0][i])/(int(TETCB[0][i])+1.)
    nuVT.append(value)
print(nuVT)

x = range(1960, 2009)
ycoalVT = coalVT[0:49]
yngVT = ngVT[0:49]
ypotVT = potVT[0:49]
yreVT = reVT[0:49]
ynuVT = nuVT[0:49]

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(x, ycoalVT, c='m', alpha=0.7, label='Coal')
ax1.scatter(x, yngVT, c='r', alpha=0.7, label='Natrual Gas')
ax1.scatter(x, ypotVT, c='g', alpha=0.7, label='Potroleum')
ax1.scatter(x, yreVT, c='y', alpha=0.7, label='Renewable Energy')
ax1.scatter(x, ynuVT, c='b', alpha=0.7, label='Nuclear electric')
plt.legend(loc='upper left');
plt.show()

    

