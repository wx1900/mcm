# -*- coding: utf-8 -*- 
import xdrlib ,sys
import xlrd

#打开excel文件
def open_excel(file= 'ProblemCData.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的索引  ，by_name：Sheet1名称
def excel_table_byname(file= 'ProblemCData.xlsx', colnameindex=0, by_name=u'seseds'):
    data = open_excel(file) #打开excel文件
    table = data.sheet_by_name(by_name) #根据sheet名字来获取excel中的sheet
    nrows = table.nrows #行数 
    colnames = table.row_values(colnameindex) #某一行数据 
    list =[] #装读取结果的序列
    for rownum in range(0, nrows): #遍历每一行的内容
         row = table.row_values(rownum) #根据行号获取行
         if row: #如果行存在
             app = [] #一行的内容
             for i in range(len(colnames)): #一列列地读取行的内容
                app.append(row[i])
             list.append(app) #装载数据
    return list

#函数
def main():
   tables = excel_table_byname()
   sublist = []
   samecode = ""
   first = 0
   samecount = 0
   index = 0
   for row in tables[1:]: 
        if (first==0):
            print(row[0]+","+row[1])
            samecode = row[0][0:2]
            first = 1

        if (row[0][0:2] == samecode):
            samecount += 1
        else:
            first = 0
            sublist.append(str(samecount)+","+str(index))
            print(str(samecount)+","+str(index))
            # print(row[0])
            samecount = 0
        index += 1

def CalcTCB():
    tables = excel_table_byname()
    CATETCB = []
    CARETCB = []
    AZTETCB = []
    AZRETCB = []
    NMTETCB = []
    NMRETCB = []
    TXTETCB = []
    TXRETCB = []
    index = []
    count = 0
    for row in tables[1:]:
        count += 1
        sublist = []
        if (row[0] == 'TETCB'):
            sublist.append(row[2])
            sublist.append(row[3])
            if (row[1] == 'CA'):
                CATETCB.append(sublist)
            elif (row[1] == 'AZ'):
                AZTETCB.append(sublist)
            elif (row[1] == 'NM'):
                NMTETCB.append(sublist)
            else:
                TXTETCB.append(sublist)
        elif (row[0] == 'RETCB'):
            sublist.append(row[2])
            sublist.append(row[3])
            if (row[1] == 'CA'):
                CARETCB.append(sublist)
            elif (row[1] == 'AZ'):
                AZRETCB.append(sublist)
            elif (row[1] == 'NM'):
                NMRETCB.append(sublist)
            else:
                TXRETCB.append(sublist)
        elif ()
    print(count)
    print("CATETCB")
    for i in CATETCB:
        print(str(i[0])+" , "+str(i[1]))
    # print(CATETCB)
    # print(AZTETCB)
    # print(NMTETCB)
    # print(TXTETCB)
    print("CARETCB")
    for i in CARETCB:
        print(str(i[0])+" , "+str(i[1]))
    # print(CARETCB)
    # print(AZRETCB)
    # print(NMRETCB)
    # print(TXRETCB)
    
    REVNE = []
    for i in range(0,len(CATETCB)):
        if (CATETCB[i][0] == CARETCB[i][0]):
            value = CARETCB[i][1]/(CATETCB[i][1]-CARETCB[i][1])
            # print(CATETCB[i][0])
            # print(CARETCB[i][1])
            # print(CATETCB[i][1]-CARETCB[i][1])
            # print(value)
            REVNE.append(value)
        else:
            print('Missing data TE-year='+CATETCB[i][0]+" , RE-year="+CARETCB[i][0])
    print("REVNE")
    for i in REVNE:
        print(str(i)+"")
    # print(REVNE)
if __name__=="__main__":
    CalcTCB()