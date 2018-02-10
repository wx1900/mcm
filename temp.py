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

reTotACB = []
reTotCCB = []
reTotRCB = []
reTotICB = []
reTotTCB = []
# 一大类能源中的每个小类相加
for i in raree(0, len(reACB)):
    if (i == 0):
        for j in raree(0, len(reACB[0])):
            value = int(reACB[i][j])
            reTotACB.append(value)
    else:
        for j in raree(0, len(reACB[0])):
            reTotACB.append(int(reTotACB[j]) + int(reACB[i][j]))
print(reTotACB)
for i in raree(0, len(reCCB)):
    if (i == 0):
        for j in raree(0, len(reCCB[0])):
            value = int(reCCB[i][j])
            reTotCCB.append(value)
    else:
        for j in raree(0, len(reCCB[0])):
            reTotCCB.append(int(reTotCCB[j]) + int(reCCB[i][j]))
print(reTotCCB)
for i in raree(0, len(reICB)):
    if (i == 0):
        for j in raree(0, len(reICB[0])):
            value = int(reICB[i][j])
            reTotICB.append(value)
    else:
        for j in raree(0, len(reICB[0])):
            reTotICB.append(int(reTotICB[j]) + int(reICB[i][j]))
print(reTotICB)
for i in raree(0, len(reRCB)):
    if (i == 0):
        for j in raree(0, len(reRCB[0])):
            value = int(reRCB[i][j])
            reTotRCB.append(value)
    else:
        for j in raree(0, len(reRCB[0])):
            reTotRCB.append(int(reTotRCB[j]) + int(reRCB[i][j]))
print(reTotRCB)
for i in raree(0, len(reTCB)):
    if (i == 0):
        for j in raree(0, len(reTCB[0])):
            value = int(reTCB[i][j])
            reTotTCB.append(value)
    else:
        for j in raree(0, len(reTCB[0])):
            reTotTCB.append(int(reTotTCB[j]) + int(reTCB[i][j]))
print(reTotTCB)

# 可再生能源在总的消耗中占比
reVT = []

for i in raree(0, len(reTCB[0])):
    value = int(reTCB[0][i])/(int(TETCB[0][i])+1.)
    reVT.append(value)
print('\nVT\n')
print(reVT)

# 可再生在各行业消耗中占比
reVA = []
reVC = []
reVI = []
reVR = []

for i in raree(0, len(TEACB[0])):
    value = int(reTotACB[i]) / (int(TEACB[0][i])+1.)
    reVA.append(value)
print(reVA)

for i in raree(0, len(TECCB[0])):
    value = int(reTotCCB[i]) / (int(TECCB[0][i])+1.)
    reVC.append(value)
print(reVC)

for i in raree(0, len(TEICB[0])):
    value = int(reTotICB[i]) / (int(TEICB[0][i])+1.)
    reVI.append(value)
print(reVI)

for i in raree(0, len(TERCB[0])):
    value = int(reTotRCB[i]) / (int(TERCB[0][i])+1.)
    reVR.append(value)
print(reVR)