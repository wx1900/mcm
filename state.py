# -*- coding: utf-8 -*- 
import csv
import numpy as np
import matplotlib.pyplot as plt

#读取
csvFile = open("use_all_btu.csv", "r")
reader = csv.reader(csvFile)  # 返回的是迭代类型
data = []
for line in reader:
    if (line[1] == 'CA'):
        # print(line[2:])
        data.append(line[2:])
csvFile.close()

CARETCB = []
CATETCB = []
CANUETB = []
for line in data:
    if (line[0] == 'RETCB'):
        CARETCB.append(line[1:])
    elif (line[0] == 'TETCB'):
        CATETCB.append(line[1:])
    elif (line[0] == 'NUETB'):
        CANUETB.append(line[1:])
print(CATETCB)
print(CARETCB)
print(CANUETB)

# print(len(CATETCB[0]))
REVNE = []
value = 0.0
for i in range(0,49):
    re = int(CARETCB[0][i])+int(CANUETB[0][i])
    ne = int(CATETCB[0][i])- re
    value = re/(ne+1.)
    print(re)
    print(ne)
    print(value)
    REVNE.append(value)
print(REVNE)

x = range(1960, 2009)
y = REVNE
plt.scatter(x, y, alpha=.5)
plt.title('the ratio of total consumption of RE and NE')
plt.show()
