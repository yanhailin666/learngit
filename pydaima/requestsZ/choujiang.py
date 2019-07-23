import requests
import xlrd
import time
# list=["safdsfasdfas","319hacsregp"]
# for i in list:
#     r=requests.get("http://192.168.1.201:15001/activity/activityDrawRoster/queryWinningInfo?acCode="+i)
#     print(r.json())

workbook = xlrd.open_workbook('C:/Users/qaunhou006/Desktop/test.xlsx')  #表格路径
table = workbook.sheets()[0]   #第一个表[0]

# print(table.nrows)
# print(table.ncols)
# print(table.row_values(0))
# print(table.col_values(0))
# print(table.cell(1,0).value)   #第一行、0列
# list=["safdsfasdfas","319hacsregp"]  http://192.168.1.201:15001

for j in range(0,100):
    i = table.cell(j, 0).value
    r=requests.get("http://172.16.1.118:1114/activity/activityDrawRoster/queryWinningInfo?acCode="+i)
    print(j)
    print(r.json()["data"])
    # print(r.json()["data"]["acCode"])
    # if r.json()["data"]["data"] != None:
    #
    #   print(r.json()["data"]["acCode"])
    time.sleep(0.2)