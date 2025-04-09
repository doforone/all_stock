# 白点数据，运行环境Python3.8
# -*- coding: UTF-8 -*-

from urllib import request, parse
from urllib.parse import quote
import urllib.parse

import time
import datetime
import json
import base64
import hashlib
import random
import os
import io
import zipfile
import zlib

import urllib.request
import gzip


def tt_d(x):  # 时间戳转日期
    timestamp = x  # 假设这是一个时间戳
    # 使用 fromtimestamp() 方法将时间戳转换为日期时间对象
    #date_time = datetime.datetime.fromtimestamp(timestamp)
    timestamp+=3600*8  # 北京时间偏移 UTC 时间 8 小时
    date_time = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)
    #date_time = datetime.datetime.fromtimestamp(timestamp, tz=pytz.timezone('Asia/Shanghai'))
    # 然后可以使用 strftime() 方法将日期时间格式化为特定的日期字符串
    #formatted_date = date_time.strftime('%Y-%m-%d %H:%M:%S')
    formatted_date = date_time.strftime('%Y-%m-%d')
    return formatted_date  # 输出格式化后的日期字符串


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


with open('010_不再更新的全部股票.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd0=json.loads(f.read())


#-----------------------

##with open('200_美国股票symbol信息.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
##    ddd=json.loads(f.read())


##with open('100_香港股票symbol信息.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
##    ddd=json.loads(f.read())


with open('300_中国股票symbol信息.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd=json.loads(f.read())

#========================


ddd=list(ddd.keys())
random.shuffle(ddd)
FF=28400
ff=284
nnn={}
#ddd=["03309"]
while ddd!=[]:
    dd=ddd[-1]
    if dd not in ddd0.keys():  # 排除已不再更新的
    #if 1:
        #=================
        if os.path.exists(f'雪球_后复权/{dd}_d.txt'):
            with open(f'雪球_后复权/{dd}_d.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
                uuu=json.loads(f.read())
            if uuu==[]:
                lmt=FF
                time.sleep(0.1)
            else:
                if len(uuu)==1:
                    lmt=FF
                    time.sleep(0.1)
                else:  # 只有大于1的才用ff
                    #if tt_d(int(uuu[-1][0]/1000))=="2024-03-12":
                        #ddd.pop()  # 删除最后一个。
                        #continue
                    lmt=ff
                    time.sleep(0.01)  # 正常用这个================
        else:
            uuu=[]
            lmt=FF
            time.sleep(0.1)
        #==================
        print(dd,len(ddd),lmt)
        try:
            # 请求的URL
            url = f'https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol={dd}&begin={int(time.time()*1000)}&period=day&type=after&count=-{lmt}&indicator=kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance'

            # 创建一个Request对象，设置URL和Headers
            req = urllib.request.Request(url)

            # 添加请求头部
            req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7')
            req.add_header('Accept-Encoding', 'gzip, deflate, br')
            req.add_header('Accept-Language', 'zh-CN,zh;q=0.9')
            req.add_header('Cache-Control', 'max-age=0')
            # 注意：直接在代码中使用Cookie可能涉及隐私和安全问题，请谨慎处理
            req.add_header('Cookie', 'cookiesu=511711698870106; s=cd1b26l0ys; device_id=aecf8ce52df8081afd3e6c40fa85a9cc; xq_a_token=01b99d82fffd2faf8b614e98a00cbb35d6c7ddcf; xqat=01b99d82fffd2faf8b614e98a00cbb35d6c7ddcf; xq_r_token=7fe9b3213c399b15eee3c5bca4841433a03128a6; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcxMzY2MDQyOCwiY3RtIjoxNzExODA2MjU4OTk4LCJjaWQiOiJkOWQwbjRBWnVwIn0.gVpoSp8h0k5WFa0dzEvkW7hMwExLQIZ5u245yHOxPNw3K156IUIhCDu8B4nLSuSTJ8ANn_fr3fb5xQYNr0_gPsDTMDGd6WgJ2Or-Kuf-YsW50igsz_-t1cSj2kEPf9Tcn1wf_F7HJhRAX5HZPSF_i7ONyH7zPtTDWYR-TXN2ebxZUtEb9vYLCWw9IZpdqTEqf-T7m_KcvU3PbkAMHCicEd9hrBd7SFt8nhAy10Nf3BUnqveY_IUgWJBQRzSlgQlpZGh8A6pxkKdhOU6YQwwEICipBqMM8549OOsFTYvvArrqGX8c5jmRF7P8CMndtv2gFwIQAg5MrEow11gEPNXY4g; u=511711698870106; Hm_lvt_1db88642e346389874251b5a1eded6e3=1711698873,1711806270; is_overseas=0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1711806462')
            req.add_header('Sec-Ch-Ua', '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"')
            req.add_header('Sec-Ch-Ua-Mobile', '?0')
            req.add_header('Sec-Ch-Ua-Platform', '"Windows"')
            req.add_header('Sec-Fetch-Dest', 'document')
            req.add_header('Sec-Fetch-Mode', 'navigate')
            req.add_header('Sec-Fetch-Site', 'none')
            req.add_header('Sec-Fetch-User', '?1')
            req.add_header('Upgrade-Insecure-Requests', '1')
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36')

            # 使用urlopen打开并读取URL
            with urllib.request.urlopen(req) as response:
                vvv = response.read()

            vvv = gzip.decompress(vvv)
            vvv = vvv.decode('utf-8')
            vvv = json.loads(vvv)

            if "data" in vvv.keys() and "item" in vvv["data"].keys():
                ddd2=vvv["data"]["item"]
                ddd2=[dd[:10] for dd in ddd2]
                if lmt==FF:
                    with open(f'雪球_后复权/{dd}_d.txt', 'w', encoding='utf-8', newline='\r\n') as f:
                        f.write(json.dumps(ddd2, indent=0, ensure_ascii=False)+"\r\n")
   
                    nnn[dd]=[]  # 写入到新数据文件里
                    # 整理后: 0日期 1开盘 2最低 3最高 4收盘 5涨跌额 6涨跌幅 7成交量 8成交额 9换手率
                    nnn[dd].extend([[tt_d(int(xx[0]/1000)),xx[2],xx[4],xx[3],xx[5],xx[6],xx[7],xx[1],xx[9],xx[8]] for xx in ddd2])
                    
                    ddd.pop()  # 删除最后一个。
                else:
                    if ddd2!=[]:
                        if ddd2[-1]==uuu[-1]:  # 已有,就不再更新了
                            ddd.pop()  # 删除最后一个。
                        else:
                            if ddd2[0] in uuu and uuu[-2] in ddd2:  # -2是因为最后一个可能是实时的数据,不是最终的K线数据
                                #print("ok")
                                i=ddd2.index(uuu[-2])
                                uuu=uuu[:-1]
                                uuu.extend(ddd2[i+1:])
                                with open(f'雪球_后复权/{dd}_d.txt', 'w', encoding='utf-8', newline='\r\n') as f:
                                    f.write(json.dumps(uuu, indent=0, ensure_ascii=False)+"\r\n")  # 写入空值重新循环

                                nnn[dd]=[]  # 写入到新数据文件里
                                nnn[dd].extend([[tt_d(int(xx[0]/1000)),xx[2],xx[4],xx[3],xx[5],xx[6],xx[7],xx[1],xx[9],xx[8]] for xx in ddd2[i+1:]])

                                ddd.pop()  # 删除最后一个。
                            else:
                                #print("no ok")
                                with open(f'雪球_后复权/{dd}_d.txt', 'w', encoding='utf-8', newline='\r\n') as f:
                                    f.write(json.dumps([], indent=0, ensure_ascii=False)+"\r\n")  # 写入空值重新循环
                    else:
                        ddd.pop()  # 删除最后一个。
            else:
                print("--- Cookies Err ---")

        except Exception as e:
            print(e)
            print("--Err--")
            #ddd.pop()  # 删除最后一个。===========临时用
    else:
        ddd.pop()  # 删除最后一个。==========配合上面的 if 1 使用


with open(f'_new_data_2.txt', 'w', encoding='utf-8', newline='\r\n') as f:
    #f.write(json.dumps(ddd2, indent=4, ensure_ascii=False)+"\r\n")
    f.write(json.dumps(nnn, ensure_ascii=False))
    #f.write(json.dumps(ddd2, indent=0, ensure_ascii=False)+"\r\n")


print("--end--")
