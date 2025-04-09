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


rrr=set()
rrr2=set()  # 新浪行业------另外一个&
rrr_a=set()  # 东方财富地区
rrr_a2=set()  # 新浪地区
rrr3={}  # 新浪证监会行业

with open('../data/雪球_中国股票_申万行业分类.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd=json.loads(f.read())

for dd in ddd["data"]["industries"]:
    rrr.add(dd["name"])


with open('../东方财富/000_左栏菜单数据.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd=json.loads(f.read())
    
for dd in ddd[5]["next"][2]["next"]:  # 行业
    rrr.add(dd["title"])
    
for dd in ddd[5]["next"][1]["next"]:  # 地区
    rrr_a.add(dd["title"])


with open('../新浪财经/000_新浪导航分类等基本信息.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd=json.loads(f.read())
for dd in ddd[1][0][1][0][1]:
    rrr2.add(dd[0])

for dd in ddd[1][0][1][1][1]:  # 申万行业
    rrr.add(dd[0])

for dd in ddd[1][0][1][2][1]:  # 申万一级行业
    rrr.add(dd[0])

for dd in ddd[1][0][1][3][1]:  # 申万二级行业
    rrr.add(dd[0])

for dd in ddd[1][0][1][4][1]:  # 申万三级行业
    rrr.add(dd[0])

for dd in ddd[1][0][1][7][1]:  # 地域
    rrr_a2.add(dd[0])

for dd in ddd[1][0][1][8][1]:  # 证监会行业
    rrr3[dd[0]]=[]
    for d in dd[1]:
        rrr3[dd[0]].append(d[0])
    
print(rrr)
print("=========")
print(rrr2)
print(rrr_a)
print(rrr_a2)
print(rrr3)
print("--end--")
