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

def rep(s):
    return s.replace(" ","").replace(" ","").replace("Ｂ","B")


with open('000_新浪中国股票symbol信息.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd=json.loads(f.read())

with open('000_东方财富中国全部股票.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd2=json.loads(f.read())  # 东方财富为纯数字

with open('300_中国股票symbol信息.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd3=json.loads(f.read())

#----------------BJ北证A股
for kk in ddd2.keys():  # 东方财富
    if "BJ"+kk not in rrr.keys():
        for dd in ddd2[kk]:
            if dd=="@北证A股":
                rrr["BJ"+kk]=[rep(ddd2[kk][0]),"BJ北证A股"]

        
for kk in ddd.keys():  # 新浪
    if kk[:2].upper()=="BJ" and kk.upper() not in rrr.keys():  # 屏蔽了指数,因为指数不能获取数据
        rrr[kk.upper()]=[rep(ddd[kk][0]),"BJ北证A股"]
#=================

#----------------SZ创业板
for kk in ddd2.keys():  # 东方财富
    if "SZ"+kk not in rrr.keys():
        for dd in ddd2[kk]:
            if dd=="@注册制创业板" or dd=="@核准制创业板":
                rrr["SZ"+kk]=[rep(ddd2[kk][0]),"SZ创业板"]
                break


for kk in ddd.keys():  # 新浪
    if kk.upper() not in rrr.keys():  # 屏蔽了指数,因为指数不能获取数据
        for dd in ddd[kk]:
            if dd=="*:创业板":
                rrr[kk.upper()]=[rep(ddd[kk][0]),f"{kk[:2].upper()}创业板"]
                break
#=================

#----------------SH科创板
for kk in ddd2.keys():  # 东方财富
    if "SH"+kk not in rrr.keys():
        for dd in ddd2[kk]:
            if dd=="@科创板":
                rrr["SH"+kk]=[rep(ddd2[kk][0]),"SH科创板"]
                break


for kk in ddd.keys():  # 新浪
    if kk.upper() not in rrr.keys():  # 屏蔽了指数,因为指数不能获取数据
        for dd in ddd[kk]:
            if dd=="*:科创板":
                rrr[kk.upper()]=[rep(ddd[kk][0]),f"{kk[:2].upper()}科创板"]
                break
#=================

#----------------SH沪市B股
for kk in ddd.keys():  # 新浪
    if kk.upper() not in rrr.keys():  # 屏蔽了指数,因为指数不能获取数据
        for dd in ddd[kk]:
            if dd=="*:沪市B股":
                rrr[kk.upper()]=[rep(ddd[kk][0]),f"{kk[:2].upper()}上证B股"]
                break

for kk in ddd2.keys():  # 东方财富
    if "SH"+kk not in rrr.keys():
        for dd in ddd2[kk]:
            if dd=="@B股" and dd[0]=="9":
                rrr["SH"+kk]=[rep(ddd2[kk][0]),"SH上证B股"]
                break
#=================


#----------------SZ深市B股
for kk in ddd.keys():  # 新浪
    if kk.upper() not in rrr.keys():  # 屏蔽了指数,因为指数不能获取数据
        for dd in ddd[kk]:
            if dd=="*:深市B股":
                rrr[kk.upper()]=[rep(ddd[kk][0]),f"{kk[:2].upper()}深证B股"]
                break

for kk in ddd2.keys():  # 东方财富
    if "SZ"+kk not in rrr.keys():
        for dd in ddd2[kk]:
            if dd=="@B股" and dd[0]=="2":
                rrr["SZ"+kk]=[rep(ddd2[kk][0]),"SZ深证B股"]
                break
#=================


for kk in ddd3.keys():  # 雪球
    if kk.upper() not in rrr.keys():
        if kk[:2].upper()=="SH":
            A="SH上证A股"
        elif kk[:2].upper()=="SZ":
            A="SZ深证A股"
            
        rrr[kk.upper()]=[rep(ddd3[kk][0]),A]


for kk in ddd2.keys():  # 东方财富
    if "SZ"+kk not in rrr.keys():
        for dd in ddd2[kk]:
            if dd=="@核准制深证A股" or dd=="@注册制深证A股":
                rrr["SZ"+kk]=[rep(ddd2[kk][0]),"SZ深证A股"]
                break


for kk in ddd2.keys():  # 东方财富
    if "SH"+kk not in rrr.keys():
        for dd in ddd2[kk]:
            if dd=="@核准制上证A股" or dd=="@注册制上证A股":
                rrr["SH"+kk]=[rep(ddd2[kk][0]),"SH上证A股"]
                break
            

for kk in ddd.keys():  # 新浪
    if kk.upper() not in rrr.keys():  # 屏蔽了指数,因为指数不能获取数据
        for dd in ddd[kk]:
            if dd=="*:沪市A股":
                rrr[kk.upper()]=[rep(ddd[kk][0]),"SH上证A股"]
                break

for kk in ddd.keys():  # 新浪
    if kk.upper() not in rrr.keys():  # 屏蔽了指数,因为指数不能获取数据
        for dd in ddd[kk]:
            if dd=="*:深市A股":
                rrr[kk.upper()]=[rep(ddd[kk][0]),"SZ深证A股"]
                break

rrr["SH000001"]=["上证指数","SH上证指数"]
rrr["SZ399001"]=["深证成指","SZ深证成指"]
rrr["SZ399006"]=["创业板指","SZ创业板指"]
rrr["SH000300"]=["沪深300","SH沪深300"]
rrr["SH000016"]=["上证50","SH上证50"]
rrr["SH000905"]=["中证500","SH中证500"]
rrr["SZ399005"]=["中小100","SZ中小100"]
rrr["SH000688"]=["科创50","SH科创50"]

print(len(rrr))

with open(f'000_全部中国股票.txt', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(json.dumps(rrr, indent=4, ensure_ascii=False)+"\r\n")

print("--end--")
