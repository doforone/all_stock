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


with open('000_新浪中国股票symbol信息.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd=json.loads(f.read())

##with open('000_新浪导航分类等基本信息.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
##    ddd3=json.loads(f.read())
##    ddd3={v[2][3:]:v[0] for v in ddd3["行情中心"]["香港股市"]["恒生行业"]}  # 错误
##    print(ddd3)

ddd3=[
                        [
                            "北交所",
                            "",
                            "hs_bjs",
                            "cn"
                        ],
                        [
                            "沪市A股",
                            "",
                            "sh_a"
                        ],
                        [
                            "沪市B股",
                            "",
                            "sh_b",
                            "cn.cn_sh_b"
                        ],
                        [
                            "深市A股",
                            "",
                            "sz_a"
                        ],
                        [
                            "深市B股",
                            "",
                            "sz_b"
                        ],
                        [
                            "沪市债券",
                            "",
                            "sh_z_fenlei",
                            "bond.bond",
                            "{node: 'sh_z'}"
                        ],
                        [
                            "深市债券",
                            "",
                            "sz_z_fenlei",
                            "bond.bond",
                            "{node: 'sz_z'}"
                        ],
                        [
                            "沪深A股",
                            "",
                            "hs_a"
                        ],
                        [
                            "沪深B股",
                            "",
                            "hs_b"
                        ],
                        [
                            "沪深债券",
                            "",
                            "hs_z_fenlei",
                            "bond.bond",
                            "{node: 'hs_z'}"
                        ],
                        [
                            "沪深基金",
                            "",
                            "close_fund_fenlei",
                            "bond.fundex",
                            "{node: 'close_fund'}"
                        ],
                        [
                            "所有指数",
                            "",
                            "hs_s",
                            "bond.cnindex"
                        ],
                        [
                            "沪深权证",
                            "",
                            "hs_qz_fenlei",
                            "bond.cnzxg",
                            "{node: 'hs_qz'}"
                        ],
                        [
                            "创业板",
                            "",
                            "cyb",
                            "cn"
                        ],
                        [
                            "科创板",
                            "",
                            "kcb",
                            "cn"
                        ],
                        [
                            "上证所风险警示板",
                            "",
                            "shfxjs",
                            "cn"
                        ]
                    ]


for dd3 in ddd3:
    print(dd3)
    for i in range(1,999999):
        time.sleep(random.randint(1, 6))
        print(i)
        
        # 请求的URL
        url = f'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page={i}&num=40&sort=symbol&asc=1&node={dd3[2]}&symbol=&_s_r_a=init'
        

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
                ddd[dd2["symbol"]]=[dd2["name"], f"*:{dd3[0]}"]  # RM:热门概念,GN:概念板块,#:地域板块,*:分类
            else:
                ddd[dd2["symbol"]].append(f"*:{dd3[0]}")  # RM:热门概念,GN:概念板块,#:地域板块,*:分类


    with open(f'000_新浪中国股票symbol信息.txt', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(json.dumps(ddd, indent=4, ensure_ascii=False)+"\r\n")

print("--end--")
