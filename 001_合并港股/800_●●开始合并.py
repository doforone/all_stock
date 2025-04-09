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


rrr={}


with open('000_新浪香港股票symbol信息.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd=json.loads(f.read())

with open('000_东方财富香港全部股票.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd2=json.loads(f.read())

with open('100_香港股票symbol信息.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd3=json.loads(f.read())


for kk in ddd.keys():
    if kk not in rrr.keys() and kk.isdigit():  # 屏蔽了指数,因为指数不能获取数据
        rrr[kk]=[""]

for kk in ddd2.keys():
    if kk not in rrr.keys() and kk.isdigit():
        rrr[kk]=[""]

for kk in ddd3.keys():
    if kk not in rrr.keys() and kk.isdigit():
        rrr[kk]=[""]


for kk in rrr.keys():  # 先雪球
    if kk in ddd3.keys():
        rrr[kk][0]=ddd3[kk][0]
        

for kk in rrr.keys():  # 再新浪中文名
    if rrr[kk][0]=="" and kk in ddd.keys():
        rrr[kk][0]=ddd[kk][0]


for kk in rrr.keys():  # 再东方财富
    if rrr[kk][0]=="" and kk in ddd2.keys():
        rrr[kk][0]=ddd2[kk][0]
        

for kk in rrr.keys():  # 再新浪英文名
    if rrr[kk][0]=="" and kk in ddd.keys():
        rrr[kk][0]=ddd[kk][1]
        print(kk,ddd[kk][1])
        

print(len(rrr))

with open(f'000_全部港股.txt', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(json.dumps(rrr, indent=4, ensure_ascii=False)+"\r\n")

print("--end--")
