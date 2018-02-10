# -*- coding: utf-8 -*- 
import csv
import numpy as np
import matplotlib.pyplot as plt

# 计算物种主要能源消耗占总行业的比以及每种能源消耗在四个行业中的占比

state = 'nm'

#　读取
csvFile = open("data/"+state+".csv", "r")
reader = csv.reader(csvFile)  # 返回的是迭代类型
data = []
for line in reader:
    data.append(line)
csvFile.close()

# Coal
coal = ['CL', 'CC']
# Natrual Gas
ng = ['NG','NN']
# Potroleum
potroleum = ['AB','AR','AV','CO','DF','DK','FF','FN','FO','FS',
            'JF','JK','KS','LG','LO','LU','MB','MG','MS','NA',
            'P1','PC','PO','PP','PL','RF','SN','SG','SN',
            'US','WX','UO']
# PMTCB 所有除乙醇外的石油制品 'P1','PA','PC','PO','PP','PL'
# Renewable energy
re = ['EN','EM','ES','GE','GO','HY','SO','WY','WW','WD','BM']
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
PMTCB = []
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
            coalTotACB[j] = int(coalTotACB[j]) + int(coalACB[j])

for i in range(0, len(coalCCB)):
    if (i == 0):
        for j in range(0, len(coalCCB[0])):
            value = int(coalCCB[i][j])
            coalTotCCB.append(value)
    else:
        for j in range(0, len(coalCCB[0])):
            coalTotCCB[j] = int(coalTotCCB[j]) + int(coalCCB[j])

for i in range(0, len(coalICB)):
    if (i == 0):
        for j in range(0, len(coalICB[0])):
            value = int(coalICB[i][j])
            coalTotICB.append(value)
    else:
        for j in range(0, len(coalICB[0])):
            coalTotICB[j] = int(coalTotICB[j]) + int(coalICB[j])

for i in range(0, len(coalRCB)):
    if (i == 0):
        for j in range(0, len(coalRCB[0])):
            value = int(coalRCB[i][j])
            coalTotRCB.append(value)
    else:
        for j in range(0, len(coalRCB[0])):
            coalTotRCB[j] = int(coalTotRCB[j]) + int(coalRCB[j])

for i in range(0, len(coalTCB)):
    if (i == 0):
        for j in range(0, len(coalTCB[0])):
            value = int(coalTCB[i][j])
            coalTotTCB.append(value)
    else:
        for j in range(0, len(coalTCB[0])):
            coalTotTCB[j] = int(coalTotTCB[j]) + int(coalTCB[j])

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
            ngTotACB[j] = int(ngTotACB[j]) + int(ngACB[i][j])
# print(ngTotACB)
for i in range(0, len(ngCCB)):
    if (i == 0):
        for j in range(0, len(ngCCB[0])):
            value = int(ngCCB[i][j])
            ngTotCCB.append(value)
    else:
        for j in range(0, len(ngCCB[0])):
            ngTotCCB[j] = int(ngTotCCB[j]) + int(ngCCB[i][j])
# print(ngTotCCB)
for i in range(0, len(ngICB)):
    if (i == 0):
        for j in range(0, len(ngICB[0])):
            value = int(ngICB[i][j])
            ngTotICB.append(value)
    else:
        for j in range(0, len(ngICB[0])):
            ngTotICB[j] = int(ngTotICB[j]) + int(ngICB[i][j])
# print(ngTotICB)
for i in range(0, len(ngRCB)):
    if (i == 0):
        for j in range(0, len(ngRCB[0])):
            value = int(ngRCB[i][j])
            ngTotRCB.append(value)
    else:
        for j in range(0, len(ngRCB[0])):
            ngTotRCB[j] = int(ngTotRCB[j]) + int(ngRCB[i][j])
# print(ngTotRCB)
for i in range(0, len(ngTCB)):
    if (i == 0):
        for j in range(0, len(ngTCB[0])):
            value = int(ngTCB[i][j])
            ngTotTCB.append(value)
    else:
        for j in range(0, len(ngTCB[0])):
            ngTotTCB[j] = int(ngTotTCB[j]) + int(ngTCB[i][j])
# print(ngTotTCB)

# potroleum
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
            value = int(potACB[0][j])
            potTotACB.append(value)
    else:
        for j in range(0, len(potACB[0])):
            a = int(potTotACB[j])
            b = int(potACB[i][j])
            potTotACB[j] = a + b

for i in range(0, len(potCCB)):
    if (i == 0):
        for j in range(0, len(potCCB[0])):
            value = int(potCCB[i][j])
            potTotCCB.append(value)
    else:
        for j in range(0, len(potCCB[0])):
            potTotCCB[j] = int(potTotCCB[j]) + int(potCCB[i][j])

for i in range(0, len(potICB)):
    if (i == 0):
        for j in range(0, len(potICB[0])):
            value = int(potICB[i][j])
            potTotICB.append(value)
    else:
        for j in range(0, len(potICB[0])):
            potTotICB[j] = int(potTotICB[j]) + int(potICB[i][j])

for i in range(0, len(potRCB)):
    if (i == 0):
        for j in range(0, len(potRCB[0])):
            value = int(potRCB[i][j])
            potTotRCB.append(value)
    else:
        for j in range(0, len(potRCB[0])):
            potTotRCB[j] = int(potTotRCB[j]) + int(potRCB[i][j])

for i in range(0, len(potTCB)):
    if (i == 0):
        for j in range(0, len(potTCB[0])):
            value = int(potTCB[i][j])
            potTotTCB.append(value)
    else:
        for j in range(0, len(potTCB[0])):
            potTotTCB[j] = int(potTotTCB[j]) + int(potTCB[i][j])

print("\npotTotTCB\n")
print(potTotTCB)

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
    elif (var == 'GOCCB'):
        reTCB.append(i[1:])
    elif (var == 'GORCB'):
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
            reTotACB[j] = int(reTotACB[j]) + int(reACB[i][j])
# print(reTotACB)
for i in range(0, len(reCCB)):
    if (i == 0):
        for j in range(0, len(reCCB[0])):
            value = int(reCCB[i][j])
            reTotCCB.append(value)
    else:
        for j in range(0, len(reCCB[0])):
            reTotCCB[j] = int(reTotCCB[j]) + int(reCCB[i][j])
# print(reTotCCB)
for i in range(0, len(reICB)):
    if (i == 0):
        for j in range(0, len(reICB[0])):
            value = int(reICB[i][j])
            reTotICB.append(value)
    else:
        for j in range(0, len(reICB[0])):
            reTotICB[j] = int(reTotICB[j]) + int(reICB[i][j])
# print(reTotICB)
for i in range(0, len(reRCB)):
    if (i == 0):
        for j in range(0, len(reRCB[0])):
            value = int(reRCB[i][j])
            reTotRCB.append(value)
    else:
        for j in range(0, len(reRCB[0])):
            reTotRCB[j] = int(reTotRCB[j]) + int(reRCB[i][j])
# print(reTotRCB)
for i in range(0, len(reTCB)):
    if (i == 0):
        for j in range(0, len(reTCB[0])):
            value = int(reTCB[i][j])
            reTotTCB.append(value)
    else:
        for j in range(0, len(reTCB[0])):
            reTotTCB[j] = int(reTotTCB[j]) + int(reTCB[i][j])
# print(reTotTCB)

# WD数据中缺少TCB 
# NUETB 表示核能的总消耗
# 核能只计算占总能源比例，不计算产业占比
print("nu\n")
NUETB = []
nuVT = []
for i in nuData:
    if (i[0] == 'NUETB'):
        NUETB.append(i[1:])
# print('\nNUETB\n')
# print(NUETB)


# 重新计算总量
for i in range(0, len(TETCB[0])):
    TETCB[0][i] = int(coalTotTCB[i]) + int(ngTotTCB[i]) + int(potTotTCB[i]) + int(reTotTCB[i]) + int(NUETB[0][i])
    TEACB[0][i] = int(coalTotACB[i]) + int(ngTotACB[i]) + int(potTotACB[i]) + int(reTotACB[i]) 
    TECCB[0][i] = int(coalTotCCB[i]) + int(ngTotCCB[i]) + int(potTotCCB[i]) + int(reTotCCB[i]) 
    TEICB[0][i] = int(coalTotICB[i]) + int(ngTotICB[i]) + int(potTotICB[i]) + int(reTotICB[i])
    TERCB[0][i] = int(coalTotRCB[i]) + int(ngTotRCB[i]) + int(potTotRCB[i]) + int(reTotRCB[i])  
print("\nTETCB\n")
print(TETCB)
# 煤在总的消耗中占比
coalVT = []

for i in range(0, len(TETCB[0])):
    value = int(coalTotTCB[i])/(int(TETCB[0][i])+1.)
    coalVT.append(value)
print("\ncoalVT\n")
print(coalVT)
# 煤在各行业消耗中占比
coalVA = []
coalVC = []
coalVI = []
coalVR = []

for i in range(0, len(TEACB[0])):
    value = int(coalTotACB[i]) / (int(TEACB[0][i])+1.)
    coalVA.append(value)
print("\ncoalVA\n")
print(coalVA)

for i in range(0, len(TECCB[0])):
    value = int(coalTotCCB[i]) / (int(TECCB[0][i])+1.)
    coalVC.append(value)
print("\ncoalVC\n")
print(coalVC)

for i in range(0, len(TEICB[0])):
    value = int(coalTotICB[i]) / (int(TEICB[0][i])+1.)
    coalVI.append(value)
print("\ncoalVI\n")
print(coalVI)

for i in range(0, len(TERCB[0])):
    value = int(coalTotRCB[i]) / (int(TERCB[0][i])+1.)
    coalVR.append(value)
print("\ncoalVR\n")
print(coalVR)

# 天然气在总的消耗中占比
ngVT = []

for i in range(0, len(TETCB[0])):
    value = int(ngTotTCB[i])/(int(TETCB[0][i])+1.)
    ngVT.append(value)
print('\nngVT\n')
print(ngVT)

# 天然气在各行业消耗中占比
ngVA = []
ngVC = []
ngVI = []
ngVR = []

for i in range(0, len(TEACB[0])):
    value = int(ngTotACB[i]) / (int(TEACB[0][i])+1.)
    ngVA.append(value)
print("\nngVA\n")
print(ngVA)

for i in range(0, len(TECCB[0])):
    value = int(ngTotCCB[i]) / (int(TECCB[0][i])+1.)
    ngVC.append(value)
print("\nngVC\n")
print(ngVC)

for i in range(0, len(TEICB[0])):
    value = int(ngTotICB[i]) / (int(TEICB[0][i])+1.)
    ngVI.append(value)
print("\nngVI\n")
print(ngVI)

for i in range(0, len(TERCB[0])):
    value = int(ngTotRCB[i]) / (int(TERCB[0][i])+1.)
    ngVR.append(value)
print("\nngVR")
print(ngVR)

# 石油在总的消耗中占比
potVT = []

for i in range(0, len(TETCB[0])):
    value = int(potTotTCB[i])/(int(TETCB[0][i])+1.)
    potVT.append(value)
print('\npotVT\n')
print(potVT)

# 石油在各行业消耗中占比
potVA = []
potVC = []
potVI = []
potVR = []

for i in range(0, len(TEACB[0])):
    value = int(potTotACB[i]) / (int(TEACB[0][i])+1.)
    potVA.append(value)
print('\npotVA\n')
print(potVA)

for i in range(0, len(TECCB[0])):
    value = int(potTotCCB[i]) / (int(TECCB[0][i])+1.)
    potVC.append(value)
print('\npotVC\n')
print(potVC)

for i in range(0, len(TEICB[0])):
    value = int(potTotICB[i]) / (int(TEICB[0][i])+1.)
    potVI.append(value)
print('\npotVI\n')
print(potVI)

for i in range(0, len(TERCB[0])):
    value = int(potTotRCB[i]) / (int(TERCB[0][i])+1.)
    potVR.append(value)
print('\npotVR\n')
print(potVR)

# 可再生能源在总的消耗中占比
reVT = []

for i in range(0, len(TETCB[0])):
    value = int(reTotTCB[i])/(int(TETCB[0][i])+1.)
    reVT.append(value)
print('\nreVT\n')
print(reVT)

# 可再生在各行业消耗中占比
reVA = []
reVC = []
reVI = []
reVR = []

for i in range(0, len(TEACB[0])):
    value = int(reTotACB[i]) / (int(TEACB[0][i])+1.)
    reVA.append(value)
print('\nreVA\n')
print(reVA)

for i in range(0, len(TECCB[0])):
    value = int(reTotCCB[i]) / (int(TECCB[0][i])+1.)
    reVC.append(value)
print('\nreVC\n')
print(reVC)

for i in range(0, len(TEICB[0])):
    value = int(reTotICB[i]) / (int(TEICB[0][i])+1.)
    reVI.append(value)
print('\nreVI\n')
print(reVI)

for i in range(0, len(TERCB[0])):
    value = int(reTotRCB[i]) / (int(TERCB[0][i])+1.)
    reVR.append(value)
print('\nreVR\n')
print(reVR)

# Nuclear electric
for i in range(0, len(NUETB[0])):
    value = int(NUETB[0][i])/(int(TETCB[0][i])+1.)
    nuVT.append(value)
print('\nnuVT\n')
print(nuVT)

x = range(1960, 2009)
ycoalVT = coalVT[0:49]
yngVT = ngVT[0:49]
ypotVT = potVT[0:49]
yreVT = reVT[0:49]
ynuVT = nuVT[0:49]
plt.xlabel('Time(year)')
plt.ylabel('Ratio')
# plt.scatter(x, ycoalVT, c='y', alpha=0.7, label='Coal')
# plt.scatter(x, yngVT, c='r', alpha=0.7, label='Natrual Gas')
# plt.scatter(x, ypotVT, c='g', alpha=0.7, label='Petroleum')
# plt.scatter(x, yreVT, c='m', alpha=0.7, label='Renewable Energy')
# plt.scatter(x, ynuVT, c='b', alpha=0.7, label='Nuclear electric')
# art = []
# lgd = plt.legend(loc=9, bbox_to_anchor=(0.5,-0.1),ncol = 2)
# art.append(lgd)
# plt.savefig("fig/energyprofile_"+state+".png", additional_artists=art, bbox_inches = "tight")
# plt.show()

ycoalVA = coalVA[0:49]
ycoalVC = coalVC[0:49]
ycoalVI = coalVI[0:49]
ycoalVR = coalVR[0:49]

yngVA = ngVA[0:49]
yngVC = ngVC[0:49]
yngVI = ngVI[0:49]
yngVR = ngVR[0:49]
    
ypotVA = potVA[0:49]
ypotVC = potVC[0:49]
ypotVI = potVI[0:49]
ypotVR = potVR[0:49]

yreVA = reVA[0:49]
yreVC = reVC[0:49]
yreVI = reVI[0:49]
yreVR = reVR[0:49]

plt.scatter(x, ycoalVA, c='y', alpha=.7, label='Coal')
plt.scatter(x, yngVA, c='r', alpha=.7, label='Natrual Gas')
plt.scatter(x, ypotVA, c='g', alpha=.7, label='Petroleum')
plt.scatter(x, yreVA, c='m', alpha=.7, label='Renewable Energy')
art = []
lgd = plt.legend(loc=9, bbox_to_anchor=(0.5,-0.1),ncol = 2)
art.append(lgd)
plt.savefig("fig/transportation_"+state+".png", additional_artists=art, bbox_inches = "tight")
plt.close()

plt.scatter(x, ycoalVC, c='y', alpha=.7, label='Coal')
plt.scatter(x, yngVC, c='r', alpha=.7, label='Natrual Gas')
plt.scatter(x, ypotVC, c='g', alpha=.7, label='Petroleum')
plt.scatter(x, yreVC, c='m', alpha=.7, label='Renewable Energy')
art = []
lgd = plt.legend(loc=9, bbox_to_anchor=(0.5,-0.1),ncol = 2)
art.append(lgd)
plt.savefig("fig/commercial_"+state+".png", additional_artists=art, bbox_inches = "tight")
plt.close()

plt.scatter(x, ycoalVI, c='y', alpha=.7, label='Coal')
plt.scatter(x, yngVI, c='r', alpha=.7, label='Natrual Gas')
plt.scatter(x, ypotVI, c='g', alpha=.7, label='Petroleum')
plt.scatter(x, yreVI, c='m', alpha=.7, label='Renewable Energy')
art = []
lgd = plt.legend(loc=9, bbox_to_anchor=(0.5,-0.1),ncol = 2)
art.append(lgd)
plt.savefig("fig/Industrial_"+state+".png", additional_artists=art, bbox_inches = "tight")
plt.close()

plt.scatter(x, ycoalVR, c='y', alpha=.7, label='Coal')
plt.scatter(x, yngVR, c='r', alpha=.7, label='Natrual Gas')
plt.scatter(x, ypotVR, c='g', alpha=.7, label='Petroleum')
plt.scatter(x, yreVR, c='m', alpha=.7, label='Renewable Energy')
art = []
lgd = plt.legend(loc=9, bbox_to_anchor=(0.5,-0.1),ncol = 2)
art.append(lgd)
plt.savefig("fig/Residential_"+state+".png", additional_artists=art, bbox_inches = "tight")
plt.close()