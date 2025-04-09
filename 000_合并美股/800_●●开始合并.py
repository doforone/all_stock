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


with open('000_新浪美国股票symbol信息.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd=json.loads(f.read())

with open('000_东方财富美国全部股票.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd2=json.loads(f.read())

with open('200_美国股票symbol信息.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd3=json.loads(f.read())


for kk in ddd.keys():
    if kk not in rrr.keys():
        if ddd[kk][3]=="NASDAQ" or ddd[kk][3]=="NYSE" or ddd[kk][3]=="AMEX":
            rrr[kk]=[ddd[kk][3]]
        else:
            rrr[kk]=[""]

for kk in ddd2.keys():
    if kk not in rrr.keys():
        rrr[kk]=[""]

for kk in ddd3.keys():
    if kk not in rrr.keys():
        rrr[kk]=[""]

print(len(rrr))

with open(f'000_全部美股.txt', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(json.dumps(rrr, indent=4, ensure_ascii=False)+"\r\n")

print("--end--")
