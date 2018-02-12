# -*- coding: utf-8 -*- 
import csv
import numpy as np
import matplotlib.pyplot as plt

#　读取
csvFile = open("data/tx.csv", "r")
reader = csv.reader(csvFile)  # 返回的是迭代类型
data = []
for line in reader:
    data.append(line)
csvFile.close()

# 计算四个行业两种能源的消耗比值
REvar = ['BM','GE','GO','HY','NG','WD','WW','WY']
sectors = ['RCB','CCB','ICB','ACB']
RERCB = []
RECCB = []
REICB = []
REACB = []
NERCB = []
NECCB = []
NEICB = []
NEACB = []
TotRCB = []
TotCCB = []
TotICB = []
TotACB = []
TETCB = []
for line in data:
    isNe = 0;
    for i in range(0, len(REvar)):
        if (line[0] == REvar[i]+sectors[0]):
            RERCB.append(line[1:])
        elif (line[0] == REvar[i]+sectors[1]):
            RECCB.append(line[1:])
        elif (line[0] == REvar[i]+sectors[2]):
            REICB.append(line[1:])
        elif (line[0] == REvar[i]+sectors[3]):
            REACB.append(line[1:])
        else:
            isNe = 1;
    if (line[0] == 'TERCB'):
        TotRCB.append(line[1:])
    elif (line[0] == 'TECCB'):
        TotCCB.append(line[1:])
    elif (line[0] == 'TEICB'):
        TotICB.append(line[1:])
    elif (line[0] == 'TEACB'):
        TotACB.append(line[1:])
    elif (line[0] == 'TETCB'):
        TETCB.append(line[1:])
    elif (isNe == 1):
        if (line[0][2:5] == 'RCB'):
            NERCB.append(line[1:])
        elif (line[0][2:5] == 'CCB'):
            NERCB.append(line[1:])
        elif (line[0][2:5] == 'ICB'):
            NEICB.append(line[1:])
        elif (line[0][2:5] == 'ACB'):
            NEACB.append(line[1:])

RETotRCB = []
RETotCCB = []
RETotICB = []
RETotACB = []
# 加起每行的数据
for i in range(0, len(RERCB)):
    if (i == 0):
        for j in range(0, len(RERCB[0])):
            RETotRCB.append(RERCB[i][j])
    else:
        for j in range(0, len(RERCB[0])):
            RETotRCB[j] = int(RETotRCB[j]) + int(RERCB[i][j])

for i in range(0, len(RECCB)):
    if (i == 0):
        for j in range(0, len(RECCB[0])):
            RETotCCB.append(RECCB[i][j])
    else:
        for j in range(0, len(RECCB[0])):
            RETotCCB[j] = int(RETotCCB[j]) + int(RECCB[i][j])
for i in range(0, len(REICB)):
    if (i == 0):
        for j in range(0, len(REICB[0])):
            RETotICB.append(REICB[i][j])
    else:
        for j in range(0, len(REICB[0])):
            RETotICB[j] = int(RETotICB[j]) + int(REICB[i][j])
for i in range(0, len(REACB)):
    if (i == 0):
        for j in range(0, len(REACB[0])):
            value = int(REACB[i][j])
            RETotACB.append(value)
    else:
        for j in range(0, len(REACB[0])):
            RETotACB[j] = int(RETotACB[j]) + int(REACB[i][j])

print("RETotRCB")
print(RETotRCB)
print("RETotCCB")
print(RETotCCB)
print("RETotICB")
print(RETotICB)
print("RETotACB")
print(RETotACB)

NETotRCB = []
NETotCCB = []
NETotICB = []
NETotACB = []
# 加起每行的数据
for i in range(0, len(NERCB)):
    if (i == 0):
        for j in range(0, len(NERCB[0])):
            value = int(NERCB[i][j])
            NETotRCB.append(value)
    else:
        for j in range(0, len(NERCB[0])):
            if (NERCB[i][j] != ''):
                NETotRCB[j] = int(NETotRCB[j]) + int(NERCB[i][j])

for i in range(0, len(NECCB)):
    if (i == 0):
        for j in range(0, len(NECCB[0])):
            NETotCCB.append(NECCB[i][j])
    else:
        for j in range(0, len(NECCB[0])):
            NETotCCB[j] = int(NETotCCB[j]) + int(NECCB[i][j])
for i in range(0, len(REICB)):
    if (i == 0):
        for j in range(0, len(NEICB[0])):
            NETotICB.append(NEICB[i][j])
    else:
        for j in range(0, len(NEICB[0])):
            NETotICB[j] = int(NETotICB[j]) + int(NEICB[i][j])
for i in range(0, len(NEACB)):
    if (i == 0):
        for j in range(0, len(NEACB[0])):
            NETotACB.append(NEACB[i][j])
    else:
        for j in range(0, len(NEACB[0])):
            NETotACB[j] = int(NETotACB[j]) + int(NEACB[i][j])

print("NETotRCB")
print(NETotRCB)
print("NETotCCB")
print(NETotCCB)
print("NETotICB")
print(NETotICB)
print("NETotACB")
print(NETotACB)

print("TotRCB")
print(TotRCB)
print("TotCCB")
print(TotCCB)
print("TotICB")
print(TotICB)
print("TotACB")
print(TotACB)

REVNERCB = []
REVNECCB = []
REVNEICB = []
REVNEACB = []

# 各部门在总消耗中占的比重
proption = []
for i in range(0, len(TETCB[0])):
    sublist = []
    tot = int(TETCB[0][i])
    rp = int(TotRCB[0][i])/(tot+1.)
    cp = int(TotCCB[0][i])/(tot+1.)
    ip = int(TotICB[0][i])/(tot+1.)
    ap = int(TotACB[0][i])/(tot+1.)
    sublist.append(rp)
    sublist.append(cp)
    sublist.append(ip)
    sublist.append(ap)
    proption.append(sublist)

for i in range(0, len(RETotRCB)):
    # 由于用总的消耗减去可再生能源的消耗做分母结果大于１
    # 所以采用计算出来所有不可再生能源的消耗做分母 
    re = int(RETotRCB[i])
    # ne = int(TotRCB[0][i]) - int(RETotRCB[i])
    ne = int(NETotRCB[i])
    value = re/(ne+1.)
    # print(re)
    # print(ne)
    # print(value)
    # value = int(TotRCB[0][i]) - re - ne 
    REVNERCB.append(value)
print("REVNERCB")
print(REVNERCB)

for i in range(0, len(RETotCCB)):
    re = int(RETotCCB[i])
    ne = int(TotCCB[0][i]) - int(RETotCCB[i])
    value = re/(ne+1.)
    # print(re)
    # print(ne)
    # print(value)
    # value = int(TotCCB[0][i]) - re - ne
    REVNECCB.append(value)
print("REVNECCB")
print(REVNECCB)

for i in range(0, len(RETotICB)):
    re = int(RETotICB[i])
    # ne = int(NETotICB[i])
    ne = int(TotICB[0][i]) - int(RETotICB[i])
    value = re/(ne+1.)
    # print(re)
    # print(ne)
    # print(value)
    # value = int(TotICB[0][1]) - re - ne
    REVNEICB.append(value)
print("REVNEICB")
print(REVNEICB)


for i in range(0, len(RETotACB)):
    re = int(RETotACB[i])
    # ne = int(NETotACB[i])
    ne = int(TotACB[0][i]) - int(RETotACB[i])
    value = re/(ne+1.)
    # print(re)
    # print(ne)
    # print(value)
    # value = int(TotACB[0][i]) - re - ne
    REVNEACB.append(value)
print("REVNEACB")
print(REVNEACB)

# 几乎相等
# all = []
# count = 0
# for i in range(0, len(TotCCB[0])):
    # value = int(TETCB[0][i]) - int(TotRCB[0][i]) - int(TotCCB[0][i]) - int(TotICB[0][i]) - int(TotACB[0][i])
    # all.append(value)
    # count += 1
# print(count)
# print("all")
# print(all)
# print("TETCB")
# print(TETCB)

# print("proption")
# print(proption)
all = []
for i in range(0, len(REVNERCB)):
    value = REVNERCB[i]*proption[i][0] + REVNECCB[i]*proption[i][1] + REVNEICB[i]*proption[i][2] + REVNEACB[i]*proption[i][3]
    all.append(value)

print("result")
print(all)

x = range(1960, 2009)
# y = all[0:49]
# plt.scatter(x, y, alpha=.5)
# plt.title('the ratio of RE consumption in all sectors')
# plt.show()

yr = REVNERCB[0:49]
yc = REVNECCB[0:49]
yi = REVNEICB[0:49]
ya = REVNEACB[0:49]

# plt.scatter(x, yr)
# plt.scatter(x, yc)
# plt.scatter(x, yi)
# plt.scatter(x, ya, alpha=.5)
# plt.show()


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(x, yr, c='b', alpha=0.7, label='Residential')
ax1.scatter(x, yc, c='r', alpha=0.7, label='Commenercial')
ax1.scatter(x, yi, c='g', alpha=0.7, label='Industrial')
ax1.scatter(x, ya, c='y', alpha=0.7, label='Transportion')
plt.legend(loc='upper left');
plt.show()