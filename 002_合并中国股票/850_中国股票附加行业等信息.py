# 白点数据，运行环境Python3.8
# -*- coding: UTF-8 -*-

from urllib import request, parse
from urllib.parse import quote
import urllib.parse

import json
import datetime
import os
import time
import base64
import hashlib
import random


#============================时间到强制结束线程
import threading
import inspect
import ctypes

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
 
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

#=============================

def get_htmll(urll, p=0, dataa=None):     #请求页面，这个函数要用线程，长时间不响应就杀死线程，参数5秒有时不起作用
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
    try:
        req = request.Request(urll, headers=headers)
        with request.urlopen(req, timeout=6) as resp:  # ================
            #htmll=resp.read().decode("GBK","ignore")
            htmll=resp.read().decode("utf-8","replace")
            #with open('aaa.txt', 'a', encoding='utf-8', newline='\r\n') as f:
                #f.write(htmll)
            return htmll
    except Exception as e:
        print(e)
        htmll=""
        with open(f'err.txt', 'a', encoding='utf-8', newline='\r\n') as f:
            f.write(str(p)+"\r\n")
        return htmll


def get_htmll2(urll, p, dataa=None):     #请求页面，这个函数要用线程，长时间不响应就杀死线程，参数5秒有时不起作用
    #headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Mobile Safari/537.36'}
    
    #data={"areaSn":"","entType":"02","entName":"","pageIndex":p}
    #data={"jjrSel":"","p":p}
    data=dataa
    data=urllib.parse.urlencode(data,encoding='utf-8')
    data=bytes(data,'utf-8')
    
    try:
        #req = request.Request(urll, headers=headers)
        req = request.Request(urll, headers=headers, data=data, method="POST")
        with request.urlopen(req, timeout=6) as resp:  # ===================
            #htmll=resp.read().decode("GBK","ignore")
            htmll=resp.read().decode("utf-8","replace")
            #with open('aaa.txt', 'a', encoding='utf-8', newline='\r\n') as f:
                #f.write(htmll)
            return htmll
    except Exception as e:
        print(e)
        htmll=""
        with open(f'err.txt', 'a', encoding='utf-8', newline='\r\n') as f:
            f.write(str(p)+"\r\n")
        return htmll


f0=lambda x: 0.0 if x=="" else float(x)


www={}


with open('000_全部中国股票.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd=json.loads(f.read())


for dd in ddd.keys():
    ddd[dd].append([])

mmm=["SH000001","SZ399001","SZ399006","SH000300","SH000016","SH000905",
        "SZ399005","SH000688"]

# =======================

with open('000_新浪中国股票symbol信息.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd0=json.loads(f.read())

for dd in ddd.keys():
    if ddd[dd][2]==1 and (dd.lower()) in ddd0.keys() and dd not in mmm:
        for d0 in ddd0[dd.lower()][1:]:
            if d0 not in ddd[dd][4]:
                ddd[dd][4].append(d0)

            if d0 not in www.keys():
                www[d0]=1
            else:
                www[d0]+=1

# =======================

with open('300_中国股票symbol信息.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd0=json.loads(f.read())

for dd in ddd.keys():
    if ddd[dd][2]==1 and (dd.upper()) in ddd0.keys() and dd not in mmm:
        for d0 in ddd0[dd.upper()][1:]:
            if d0 not in ddd[dd][4]:
                ddd[dd][4].append(d0)

            if d0 not in www.keys():
                www[d0]=1
            else:
                www[d0]+=1


# ========================

with open('000_东方财富中国全部股票.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd0=json.loads(f.read())

for dd in ddd.keys():
    if ddd[dd][2]==1 and dd[2:] in ddd0.keys() and dd not in mmm:
        for d0 in ddd0[dd[2:]][1:]:
            if d0 not in ddd[dd][4]:
                ddd[dd][4].append(d0)

            if d0 not in www.keys():
                www[d0]=1
            else:
                www[d0]+=1


# ========================

with open(f'000_全部中国股票.txt', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(json.dumps(ddd, indent=4, ensure_ascii=False)+"\r\n")

www=dict(sorted(www.items(), key=lambda x: x[1], reverse=True))
with open(f'000_全部行业.txt', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(json.dumps(www, indent=4, ensure_ascii=False)+"\r\n")
    
print("--end--")
