import json
from PIL import Image, ImageDraw,ImageFont
import datetime
import os
import time
import random


##        "column": [
##            "timestamp",  # 0 时间戳
##            "volume",  # 1 成交量
##            "open",  # 2 开盘
##            "high",  # 3 最高
##            "low",  # 4 最低
##            "close",  # 5 收盘
##            "chg",  # 6 涨跌额
##            "percent",  # 7 涨跌幅%=(今收/昨收-1)*100
##            "turnoverrate",  # 8 换手率
##            "amount",  # 9 成交额
##            "volume_post",
##            "amount_post",
##            "pe",
##            "pb",
##            "ps",
##            "pcf",
##            "market_capital",
##            "balance",
##            "hold_volume_cn",
##            "hold_ratio_cn",
##            "net_volume_cn",
##            "hold_volume_hk",
##            "hold_ratio_hk",
##            "net_volume_hk"
##        ],


##with open('200_美国股票symbol信息.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
##    ddd=json.loads(f.read())


##with open('100_香港股票symbol信息.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
##    ddd=json.loads(f.read())


with open('300_中国股票symbol信息.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd=json.loads(f.read())

ddd=list(ddd.keys())
random.shuffle(ddd)

for kk in ddd[:100]:
    print(kk)
    with open(f'雪球_不复权/{kk}_d.txt', 'r', encoding='utf-8-sig',\
              newline='\r\n') as f:
        uuu0=json.loads(f.read())

    with open(f'雪球_前复权/{kk}_d.txt', 'r', encoding='utf-8-sig',\
              newline='\r\n') as f:
        uuu1=json.loads(f.read())




##    if len(uuu0)==len(uuu1) and uuu0[0][0]==uuu1[0][0] and uuu0[-1][0]==uuu1[-1][0]:
##        for i in range(0,len(uuu0)):
##            #if uuu0[i][7]!=uuu1[i][7]:
##            if abs(uuu0[i][7]-uuu1[i][7])>0.02:
##                print(i,uuu0[i][7],uuu1[i][7])
##    else:
##        print("pass")





    for i in range(len(uuu1)-1,1,-1):
        #print(i)
        if round(uuu1[i][5]-uuu1[i][6],4)!=uuu1[i-1][5]:
            print(round(uuu1[i][5]-uuu1[i][6],4),uuu1[i-1][5])
            print(uuu1[i])
            print(uuu1[i-1])
            print(i,"-----------")

##        if round(ddd2[i][6]*100/(ddd2[i][5]-ddd2[i][6]),2)!=ddd2[i][7]:
##            print(i,ddd2[i][6]*100/(round(ddd2[i][5]-ddd2[i][6],2)),ddd2[i][7])
##            print(ddd2[i])




print("-- End --")







