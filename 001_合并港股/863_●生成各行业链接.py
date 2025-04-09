# -*- coding: UTF-8 -*-

from urllib import request, parse
from urllib.parse import quote

import time
import json
import hashlib

from PIL import Image, ImageDraw,ImageFont
import random
import os

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

def get_htmll(urll,dataa=None):     #请求页面，这个函数要用线程，长时间不响应就杀死线程，参数5秒有时不起作用
    print(urll)
    if 1:
        global htmll
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        try:
            req = request.Request(urll, headers=headers)
            with request.urlopen(req, timeout=125) as resp:
                htmll=resp.read().decode("utf-8")
        except Exception as e:
            htmll=""


f0=lambda x: 0.0 if x=="" else float(x)


if __name__ == "__main__":
    
    with open('000_全部港股.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
        ddd=json.loads(f.read())


    print("知名港股")
    sss="<p>"
    for dd in ddd.keys():
        if ddd[dd][1]==1:
            for d in ddd[dd][3]:
                if d=="知名港股":
                    sss+=f"&ensp;<a href='/data/HK0/{dd}_d.html'>\
{dd}：{ddd[dd][0]}</a>&ensp;|"
                    #sss+=f"<a href='/data/HK0/{dd}_d.html'>{dd}：{ddd[dd][4]}</a>&ensp;&ensp;"
                    break

    sss+="</p>"
    print(sss)


    print("港股主板")
    sss="<p>"
    for dd in ddd.keys():
        if ddd[dd][1]==1:
            for d in ddd[dd][3]:
                if d=="港股主板":
                    sss+=f"&ensp;<a href='/data/HK0/{dd}_d.html'>\
{dd}：{ddd[dd][0]}</a>&ensp;|"
                    #sss+=f"<a href='/data/HK0/{dd}_d.html'>{dd}：{ddd[dd][4]}</a>&ensp;&ensp;"
                    break

    sss+="</p>"
    print(sss)



    print("港股创业板")
    sss="<p>"
    for dd in ddd.keys():
        if ddd[dd][1]==1:
            for d in ddd[dd][3]:
                if d=="港股创业板" or d=="创业板":
                    sss+=f"&ensp;<a href='/data/HK0/{dd}_d.html'>\
{dd}：{ddd[dd][0]}</a>&ensp;|"
                    #sss+=f"<a href='/data/HK0/{dd}_d.html'>{dd}：{ddd[dd][4]}</a>&ensp;&ensp;"
                    break

    sss+="</p>"
    print(sss)



    print("蓝筹股\红筹股\国企股")
    sss="<p>蓝筹股：<br/>"
    for dd in ddd.keys():
        if ddd[dd][1]==1:
            for d in ddd[dd][3]:
                if d=="蓝筹股":
                    sss+=f"&ensp;<a href='/data/HK0/{dd}_d.html'>\
{dd}：{ddd[dd][0]}</a>&ensp;|"
                    #sss+=f"<a href='/data/HK0/{dd}_d.html'>{dd}：{ddd[dd][4]}</a>&ensp;&ensp;"
                    break

    sss+="</p>"


    sss+="<p>红筹股：<br/>"
    for dd in ddd.keys():
        if ddd[dd][1]==1:
            for d in ddd[dd][3]:
                if d=="红筹股":
                    sss+=f"&ensp;<a href='/data/HK0/{dd}_d.html'>\
{dd}：{ddd[dd][0]}</a>&ensp;|"
                    #sss+=f"<a href='/data/HK0/{dd}_d.html'>{dd}：{ddd[dd][4]}</a>&ensp;&ensp;"
                    break

    sss+="</p>"



    sss+="<p>国企股：<br/>"
    for dd in ddd.keys():
        if ddd[dd][1]==1:
            for d in ddd[dd][3]:
                if d=="国企股":
                    sss+=f"&ensp;<a href='/data/HK0/{dd}_d.html'>\
{dd}：{ddd[dd][0]}</a>&ensp;|"
                    #sss+=f"<a href='/data/HK0/{dd}_d.html'>{dd}：{ddd[dd][4]}</a>&ensp;&ensp;"
                    break

    sss+="</p>"

    print(sss)



    print("A+H")
    sss="<p>"
    for dd in ddd.keys():
        if ddd[dd][1]==1:
            for d in ddd[dd][3]:
                if d[:3]=="A+H":
                    Toa=d[4:] if d[4:].isdigit() else d[6:]
                    sss+=f"&ensp;<a href='/data/HK0/{dd}_d.html'>{dd}：{ddd[dd][0]}</a>(A:<a href='/data/CN0/{Toa}_d.html'>{Toa}</a>)&ensp;|"
                    break

    sss+="</p>"
    print(sss)






    with open('000_全部行业.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
        uuu=json.loads(f.read())



    print("港股分类")
    sss="<p>"
    for uu in uuu.keys():
        if uu!="港股主板" and uu[:3]!="A+H" and uu!="知名港股"\
           and uu!="国企股"and uu!="港股创业板"and uu!="红筹股"\
           and uu!="创业板"and uu!="蓝筹股":
            #strr=f"_US0_{hashlib.md5(uu.encode(encoding='UTF-8')).hexdigest()}.html"
            strr=f"000_港股分类_{uu.replace('/','-')}.html"
            md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
            sss+=f"&ensp;<a href='/vip/{md5_16}.html'>{uu}</a>&ensp;|"
    sss+="</p>"
    print(sss)



    for uu in uuu.keys():
        if uu!="港股主板" and uu[:3]!="A+H" and uu!="知名港股"\
           and uu!="国企股"and uu!="港股创业板"and uu!="红筹股"\
           and uu!="创业板"and uu!="蓝筹股":
            #strr=f"_US0_{hashlib.md5(uu.encode(encoding='UTF-8')).hexdigest()}.html"
            strr=f"000_港股分类_{uu.replace('/','-')}.html"
            #md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
            sss="<p>"
            for dd in ddd.keys():
                if ddd[dd][1]==1 and uu in ddd[dd][3]:
                    sss+=f"&ensp;<a href='/data/HK0/{dd}_d.html'>{dd}：{ddd[dd][0]}</a>&ensp;|"
            sss+="</p>"
                    
            with open(f'vip\\{strr}', 'w', encoding='utf-8', newline='\r\n') as f:
                f.write(sss)


print("end")












        
