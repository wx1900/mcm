# -*- coding: utf-8 -*- 
import csv
import numpy as np
import matplotlib.pyplot as plt

# 从总数据中区分出　每个州的数据

#　读取
csvFile = open("data/use_all_btu.csv", "r")
reader = csv.reader(csvFile)  # 返回的是迭代类型
data = []
for line in reader:
    if (line[1] == 'TX'):
        # print(line[2:])
        data.append(line[2:])
csvFile.close()

# 写入
with open('data/tx.csv','w') as fout:
    writer=csv.writer(fout)    
    for row in data:
        writer.writerows([row])