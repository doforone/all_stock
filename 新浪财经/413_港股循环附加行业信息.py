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


with open('000_新浪香港股票symbol信息.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd=json.loads(f.read())

##with open('data/雪球_中国股票_申万行业分类.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
##    ddd3=json.loads(f.read())
##    ddd3={v["encode"]:v["name"] for v in ddd3["data"]["industries"]}


for i in range(1,999999):
    time.sleep(1)
    print(i)
    
    # 请求的URL
    #url = f'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHKStockData?page={i}&num=40&sort=symbol&asc=1&node=cyb_hk&_s_r_a=init'  # 创业板
    #url = f'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHKStockData?page={i}&num=40&sort=symbol&asc=1&node=gqg_hk&_s_r_a=init'  # 国企股
    #url = f'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHKStockData?page={i}&num=40&sort=symbol&asc=1&node=hcg_hk&_s_r_a=init'  # 红筹股
    url = f'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHKStockData?page={i}&num=40&sort=symbol&asc=1&node=lcg_hk&_s_r_a=init'  # 蓝筹股
    

    # 创建一个Request对象，设置URL和Headers
    req = urllib.request.Request(url)

##    # 添加请求头部
##    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7')
##    req.add_header('Accept-Encoding', 'gzip, deflate, br')
##    req.add_header('Accept-Language', 'zh-CN,zh;q=0.9')
##    req.add_header('Cache-Control', 'max-age=0')
##    # 注意：直接在代码中使用Cookie可能涉及隐私和安全问题，请谨慎处理
##    req.add_header('Cookie', 'cookiesu=791705843542526; device_id=ad8a6eaffaf1256a73fec55de2a7a307; xq_a_token=edbee4e5d1e92f98548629214a6e17fe06486a8f; xqat=edbee4e5d1e92f98548629214a6e17fe06486a8f; xq_r_token=1bd9fe2188768570022d1a3f9e12934cdaa1dc53; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcwODQ3NjMzNiwiY3RtIjoxNzA2OTcwODg3NjU1LCJjaWQiOiJkOWQwbjRBWnVwIn0.QxNyUSVR696RjzfcCZXFDgI5JHwIj4OXREF2a-32U4SFHNxMu2biuU8ZeiEYQZxU9VUHbIGXYUG2vuRhccmpjeU2GIvKI3weFaN4t3dtJKMXKh7Lf4SiFXzT_NtYR0eks6iH4gYAkMstIBvXiqbEHEuYRjPeJP7oVmIh66JO5AmsgR0wzWyYHwrPT_BS7_BlAIQ6cs35pmthZEecVXwHLldabXIMJDAxn5s2dHJKA80LLziTs7Ucrx2clvPibNP8SzgMLi9YEyzjCmISzjmw66sodlPm6tzpqmpggCWZLDOBj9uH4gu6RRQYeAFpkvQ2WF2AeBIQXxj3IbBlenxkvA; u=791705843542526; Hm_lvt_1db88642e346389874251b5a1eded6e3=1705843544,1705890599,1706591178,1706970894; s=ai18qot7kf; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1707045719')
##    req.add_header('Sec-Ch-Ua', '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"')
##    req.add_header('Sec-Ch-Ua-Mobile', '?0')
##    req.add_header('Sec-Ch-Ua-Platform', '"Windows"')
##    req.add_header('Sec-Fetch-Dest', 'document')
##    req.add_header('Sec-Fetch-Mode', 'navigate')
##    req.add_header('Sec-Fetch-Site', 'none')
##    req.add_header('Sec-Fetch-User', '?1')
##    req.add_header('Upgrade-Insecure-Requests', '1')
##    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36')
##
##    # 使用urlopen打开并读取URL
##    with urllib.request.urlopen(req) as response:
##        data = response.read()
##
##    data2 = gzip.decompress(data)
##    ddd2 = data2.decode('utf-8')
##    ddd2 = json.loads(ddd2)

    # 使用urlopen打开并读取URL
    with urllib.request.urlopen(req) as response:
        data = response.read()

    ddd2 = data.decode('gb2312')
    ddd2 = json.loads(ddd2)
    if ddd2==[]:
        break
    
    for dd2 in ddd2:
        if dd2["symbol"] not in ddd.keys():
            ddd[dd2["symbol"]]=[dd2["name"], dd2["engname"], dd2["tradetype"], "@蓝筹股"]
        else:
            ddd[dd2["symbol"]].append("@蓝筹股")


with open(f'000_新浪香港股票symbol信息.txt', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(json.dumps(ddd, indent=4, ensure_ascii=False)+"\r\n")

print("--end--")
