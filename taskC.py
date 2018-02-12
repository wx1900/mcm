# -*- coding: utf-8 -*- 
import csv
import numpy as np
import matplotlib.pyplot as plt

# state = "ca"
# #　读取
# csvFile = open("data/energyprofile_"+state+".csv", "r")
# reader = csv.reader(csvFile)  # 返回的是迭代类型
# data = []
# for line in reader:
#     data.append(line)
# csvFile.close()

yvar = ['coalVT','coalVA','coalVC','coalVI','coalVR',
        'ngVT','ngVA','ngVC','ngVI','ngVR',
        'petroVT','petroVA','petroVC','petroVI','petroVR',
        'reVT','reVA','reVC','reVI','reVR','nuVT']

# data_09 = []
# for i in range(0, len(yvar)):
#     data_09.append(data[i][49])

# print(data_09)

def loaddata_09(state):
    print(state)
    #　读取
    csvFile = open("data/energyprofile_"+state+".csv", "r")
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    data = []
    for line in reader:
        data.append(line)
    csvFile.close()
    data_09 = []
    for i in range(0, len(yvar)):
        data_09.append(float(data[i][49]))
    print(data_09)
    return data_09

    plt.figure(figsize=(6,9))
    labels = ['Coal', 'Natural Gas', 'Petroleum', 'Renewable Energy', 
            'Nuclear Electric Power']
    sizes = [data_09[0],data_09[5],data_09[10],data_09[15],data_09[20]]
    colors = ['red','yellowgreen','lightskyblue','green','gold']
    explode = (0,0,0.02,0,0)
    patches,text1,text2 = plt.pie(sizes,
                      explode=explode,
                      labels=labels,
                      colors=colors,
                      labeldistance = 1.2,#图例距圆心半径倍距离
                      autopct = '%3.2f%%', #数值保留固定小数位
                      shadow = False, #无阴影设置
                      startangle = 90, #逆时针起始角度设置
                      pctdistance = 0.6) #数值距圆心半径倍数距离
    #patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部文本
    # x，y轴刻度设置一致，保证饼图为圆形
    plt.axis('equal')
    plt.legend()
    plt.savefig('data/energytot_09_'+state+'.png')
    plt.show()
    return data_09



def draw(da_09):
    # 输入数据
    ca = [da_09[0][0],da_09[0][5],da_09[0][10],da_09[0][15],da_09[0][20]]
    az = [da_09[1][0],da_09[1][5],da_09[1][10],da_09[1][15],da_09[1][20]]
    nm = [da_09[2][0],da_09[2][5],da_09[2][10],da_09[2][15],da_09[2][20]]
    tx = [da_09[3][0],da_09[3][5],da_09[3][10],da_09[3][15],da_09[3][20]]

    print(ca)
    labels = ['Coal', 'Natural Gas', 'Petroleum', 'Renewable Energy', 
            'Nuclear Electric Power']
    # labels = ['California', 'Arizona', 'New Mexico', 'Texas']
    # 设置条形图的位置和宽度
    pos = list(range(len(ca)))
    width = 0.2

    # 绘制
    fig, ax = plt.subplots(figsize=(12,6))

    plt.bar(pos, ca, width,
                    alpha=0.5,
                    color='g',
                    label=labels[0])

    plt.bar([p + width for p in pos], az, width,
                    alpha=0.5,
                    color='b',
                    label=labels[1])

    plt.bar([p + width*2 for p in pos], nm, width,
                    alpha=0.5,
                    color='r',
                    label=labels[2])
    plt.bar([p + width*3 for p in pos], tx, width,
                alpha=0.5,
                color='y',
                label=labels[3])

    # 设置标签和距离
    ax.set_ylabel('Ratio')
    ax.set_title('Energy consumption in four states')
    ax.set_xticks([p + 1.5 * width for p in pos])
    ax.set_xticklabels(labels)

    # 设置x，y轴限制
    plt.xlim(min(pos)-width, max(pos)+width*4)
    plt.ylim([0, .8])

    # 绘制
    plt.legend(['California', 'Arizona', 'New Mexico', 'Texas'], loc='upper left')
    plt.grid()
    plt.show()

states = ['ca','az','nm','tx']
da_09 = []
for i in states:
    da_09.append(loaddata_09(i))
# labels = ['Coal', 'Natural Gas', 'Petroleum', 'Renewable Energy', 
            # 'Nuclear Electric Power']
ca = [da_09[0][0],da_09[0][5],da_09[0][10],da_09[0][15],da_09[0][20]]
az = [da_09[1][0],da_09[1][5],da_09[1][10],da_09[1][15],da_09[1][20]]
nm = [da_09[2][0],da_09[2][5],da_09[2][10],da_09[2][15],da_09[2][20]]
tx = [da_09[3][0],da_09[3][5],da_09[3][10],da_09[3][15],da_09[3][20]]

list = []
sublist = ['','California', 'Arizona', 'New Mexico', 'Texas']
list.append(sublist)
sublist = []
sublist.append('Total Energy')
for i in range(0,4):
    print(states[i])
    NGRENU = da_09[i][5] + da_09[i][15] + da_09[i][20]
    rest = da_09[i][0] + da_09[i][10]
    sublist.append(NGRENU) 
    print(NGRENU)
    print(rest)
list.append(sublist)

# ca
# 0.2773151365022739
# 0.7226848036334277
# az
# 0.28050433920922885
# 0.719495399605035
# nm
# 0.19956225567326413
# 0.8004372134701669
# tx
# 0.21174170045885723
# 0.7882582619064501

sector = ['Transportation' , 'Commercial', 'Residential', 'Industry']
for j in range(1,5):
    print(sector[j-1])
    sublist = []
    sublist.append(sector[j-1])
    for i in range(0,4):
        print(states[i])
        NGRENU = da_09[i][5+j] + da_09[i][15+j]
        rest = da_09[i][0+j] + da_09[i][10+j] 
        print(NGRENU)
        sublist.append(NGRENU)
        print(rest)
    list.append(sublist)

sublist=[]
sublist2 = []
sublist.append('Energy Intensity')
sublist2.append('per capita TEC')
CAPstates = ['CA','AZ','NM','TX']
TETCB = [16506589,3880260,1777266,30806649]
id = 0
for i in CAPstates:
    csvFile = open("data/TPOPP.csv", "r")
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    x1 = []
    count = 0
    for line in reader:
        if (line[0] == i):
            count += 1
            if (count > 10):
                x1.append(float(line[2]))    
    csvFile.close()

    csvFile = open("data/GDPRV.csv", "r")
    reader = csv.reader(csvFile)  # 返回的是迭代类型
    x2 = []
    for line in reader:
        if (line[0] == i):
            x2.append(float(line[2]))
    csvFile.close()
    v1 = int(TETCB[id]) / x2[39]
    sublist.append(v1)
    v2 = int(TETCB[id]) / x1[39]
    sublist2.append(v2)
    id += 1
list.append(sublist)
list.append(sublist2)
print(list)
# ca
# 16506589
# az
# 3880260
# nm
# 1777266
# tx
# 30806649

# EI
# print

with open('data/CleanEnergy_09.csv','w') as fout:
    writer=csv.writer(fout)    
    writer.writerows(list)
