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


with open('000_全部美股.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd=json.loads(f.read())

##folder_path = "data\\US_前复权\\"
##file_names = os.listdir(folder_path)
##file_names.sort(reverse=True)
###random.shuffle(file_names)
####file_names=[v for v in file_names if ((ex:=v.split(".")[-1])=="html" or ex=="py")]
####file_names.sort()
####ddd_vip={fun.md5(v)[:16]:v for v in file_names}
##
##for ff in file_names:
##    #print(ff)
##    with open(f'data\\US_前复权\\{ff}', 'r', encoding='utf-8-sig', newline='\r\n') as f:
##        ddd0=json.loads(f.read())
##    if ddd0!=[]:
##        if ddd0[-1][0]<"2024-02-06":
##            print(ff,ddd0[-1][0])


##for dd in ddd.keys():
##    if os.path.exists(f'data/US_前复权/{dd}_d.txt'):
##        with open(f'data\\US_前复权\\{dd}_d.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
##            ddd0=json.loads(f.read())
##        if ddd0==[] or ddd0[-1][0]<"2024-01-01":
##            ddd[dd].extend([0,0])
##        else:
##            if f0(ddd0[-1][10])==0:
##                ddd[dd].extend([0,0])
##            else:
##                ddd[dd].extend([1,(f0(ddd0[-1][2])*f0(ddd0[-1][5])*100)/f0(ddd0[-1][10])])  # 1为股票是否更新,第二项为市值
##    else:
##        ddd[dd].extend([0,0])


for dd in ddd.keys():
    if os.path.exists(f'data/US_前复权/{dd}_d.txt'):
        with open(f'data\\US_前复权\\{dd}_d.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
            ddd0=json.loads(f.read())
        if ddd0==[] or ddd0[-1][0]<"2024-01-01":
            ddd[dd][1]=0
            ddd[dd][2]=0
        else:
            if f0(ddd0[-1][10])==0:
                ddd[dd][1]=1
                ddd[dd][2]=0
            else:
                ddd[dd][1]=1
                ddd[dd][2]=(f0(ddd0[-1][2])*f0(ddd0[-1][5])*100)/f0(ddd0[-1][10])
    else:
        ddd[dd][1]=0
        ddd[dd][2]=0
        
ddd=dict(sorted(ddd.items(), key=lambda x: x[1][2], reverse=True))



with open(f'000_全部美股.txt', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(json.dumps(ddd, indent=4, ensure_ascii=False)+"\r\n")
        
print("--end--")
