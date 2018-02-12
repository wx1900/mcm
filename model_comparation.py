# -*- coding: utf-8 -*- 
import csv

def comparation(state):
    csvFile = open("data/model_error_"+state+".csv", "r")
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    x1 = []
    for line in reader:
        x1.append(line[2])    
    csvFile.close()
    x1 = x1[1:]
    csvFile = open("data/model2.0_error_"+state+".csv", "r")
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    x2 = []
    for line in reader:
        x2.append(line[2])
    csvFile.close()
    x2 = x2[1:]
    #　越接近于１越好
    count = 0
    for i in range(0, len(x1)):
        if (x2[i] > x1[i]):
            count += 1
    print(count/len(x1))


states = ['ca','az','nm','tx']
for i in range(0, len(states)):
    comparation(states[i])

# 0.7619047619047619
# 0.8095238095238095
# 0.5238095238095238
# 0.6666666666666666
