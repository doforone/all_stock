# 白点数据，运行环境Python3.8
# -*- coding: UTF-8 -*-

from urllib import request, parse
from urllib.parse import quote
import urllib.parse

import json
import datetime
import os
import time
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
        with request.urlopen(req, timeout=3) as resp:  # ================
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
    data={"jjrSel":"","p":p}
    data=urllib.parse.urlencode(data)
    data=bytes(data,'utf-8')
    
    try:
        #req = request.Request(urll, headers=headers)
        req = request.Request(urll, headers=headers, data=data, method="POST")
        with request.urlopen(req, timeout=3) as resp:  # ===================
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


##参数名称	参数描述
##code	证券代码
##code_name	证券名称
##ipoDate	上市日期
##outDate	退市日期
##type	证券类型，其中1：股票，2：指数，3：其它，4：可转债，5：ETF
##status	上市状态，其中1：上市，0：退市


#### 日K线参数名称及定义 ####
##"2023-07-27,1836.00,1838.03,1854.79,1828.70,20340,3749635290.00,1.43,0.52,9.48,0.16"
##茅台日期         开盘        收盘         最高        最低        成交量（手）成交额（元）振幅% 涨跌幅% 涨跌值 流通换手率
##   0              1           2            3          4            5           6           7    8      9     10
## 振幅%=（最高-最低）/昨收；涨跌幅%=（收盘-昨收）/昨收；涨跌值=收盘-昨收
## 不复权的涨跌幅也是计算的不复权的

##  日期【0】  昨收【1】  开盘【2】  最低【3】  最高【4】  收盘【5】  振幅%【6】  涨跌%【7】
##  成交量【8】  成交额【9】  换手率【10】  （收开%【11】  昨均【12】  今均【13】  均幅%【14】  市值【15】）
##  说明：振幅=最高*100/最低-100，收开=（收盘*100/开盘）-100
##  昨均=昨成交额/昨成交量，均幅=（（成交额/成交量）*100）/昨均-100
##  市值=收盘*（成交量*100）/换手率


##print("等待运行。。。")
##while 1:
##    current_time = datetime.datetime.now().strftime("%H:%M")
##    if current_time > "15:06":
##        break
##    else:
##        time.sleep(60)
        

##http://27.push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery35108213504870312407_1690465719584&secid=1.600665&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=1&end=20500101&lmt=120&_=1690465719607
##http://39.push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery35105429362863952196_1690468900155&secid=0.002703&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=1&end=20500101&lmt=120&_=1690468900179

## 27 阿里云 39  阿里云
## 8 阿里云  79  电信

# 电信 https://push2.eastmoney.com/api/qt/pkyd/get?&cb=jQuery35108550771531612558_1699353432635&fields=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6%2Cf7&secids=1.688577&lmt=20&ut=fa5fd1943c7b386f172d6893dbfba10b&wbp2u=%7C0%7C0%7C0%7Cweb&_=1699353432636
# 联通 https://np-anotice-stock.eastmoney.com/api/security/ann?cb=jQuery35108550771531612558_1699353432643&page_size=5&page_index=1&market_code=1&stock_list=688577&client_source=web&_=1699353432644
#72 阿里云  37  电信

with open('000_全部港股.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd=json.loads(f.read())
    #ddd=[[k,v[0],v[1]] for k,v in ddd.items()]
    
    ddd=list(ddd.keys())
    ddd=ddd[::-1]
    #random.shuffle(ddd)

##with open('data/不再更新的股票.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
##    ddd4=json.loads(f.read())
ddd4=[]


FF=999999
ff=50
nnn={}
while ddd!=[]:
    dd=ddd[-1]
    if 1:
        print(f"---{len(ddd)}---")
        #=================
        if os.path.exists(f'data/HK_前复权/{dd}_d.txt'):
            with open(f'data/HK_前复权/{dd}_d.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
                uuu=json.loads(f.read())
            if uuu==[]:
                lmt=FF
                time.sleep(0.1)
            else:
                if len(uuu)==1:
                    lmt=FF
                    time.sleep(0.1)
                else:  # 只有大于1的才用ff
                    lmt=ff
                    time.sleep(0.01)  # 正常用这个================
        else:
            uuu=[]
            lmt=FF
            time.sleep(0.1)
        #==================
        print(dd)

        typee="116"  # 无论主板还是创业板都是

        if typee!="":
            url=f"https://push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery35103384079352782643_1707719386148\
&secid={typee}.{dd}&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61\
&klt=101&fqt=1&end=20500101&lmt={lmt}&_={int(time.time()*1000)}"
            try:
                htmll=get_htmll(urll=url)
                p_l=htmll.find("({\"")+1
                p_r=htmll.find("});")+1
                htmll=htmll[p_l:p_r]
                ooo=json.loads(htmll)

                if ooo["data"]!=None:
                    ddd2=[]
                    for oo in ooo["data"]["klines"]:
                        o=oo.split(",")
                        ddd2.append([o[0],f0(o[1]),f0(o[2]),f0(o[3]),f0(o[4]),f0(o[5]),f0(o[6]),f0(o[7]),f0(o[8]),f0(o[9]),f0(o[10])])
                else:
                    ddd2=[]

                if lmt==FF:
                    with open(f'data/HK_前复权/{dd}_d.txt', 'w', encoding='utf-8', newline='\r\n') as f:
                        f.write(json.dumps(ddd2, indent=0, ensure_ascii=False)+"\r\n")

                    nnn[dd]=[]  # 写入到新数据文件里
                    #nnn[dd].extend([[xx[0],round(xx[2]-xx[9],2),xx[1],xx[4],xx[3],xx[2],xx[5],xx[6],xx[10]] for xx in ddd2])
                    nnn[dd].extend([[xx[0],xx[1],xx[4],xx[3],xx[2],xx[9],xx[8],xx[5],xx[6],xx[10]] for xx in ddd2])
                    
                    ddd.pop()  # 删除最后一个。
                else:
                    if ddd2!=[]:
                        if ddd2[-1]==uuu[-1]:  # 已有,就不再更新了
                            ddd.pop()  # 删除最后一个。
                        else:
                            if ddd2[0] in uuu and uuu[-2] in ddd2:  # -2是因为最后一个可能是实时的数据,不是最终的K线数据
                                i=ddd2.index(uuu[-2])
                                uuu=uuu[:-1]
                                uuu.extend(ddd2[i+1:])
                                with open(f'data/HK_前复权/{dd}_d.txt', 'w', encoding='utf-8', newline='\r\n') as f:
                                    f.write(json.dumps(uuu, indent=0, ensure_ascii=False)+"\r\n")  # 写入空值重新循环

                                nnn[dd]=[]  # 写入到新数据文件里
                                #nnn[dd].extend([[xx[0],round(xx[2]-xx[9],2),xx[1],xx[4],xx[3],xx[2],xx[5],xx[6],xx[10]] for xx in ddd2[i+1:]])
                                nnn[dd].extend([[xx[0],xx[1],xx[4],xx[3],xx[2],xx[9],xx[8],xx[5],xx[6],xx[10]] for xx in ddd2[i+1:]])

                                ddd.pop()  # 删除最后一个。
                            else:
                                with open(f'data/HK_前复权/{dd}_d.txt', 'w', encoding='utf-8', newline='\r\n') as f:
                                    f.write(json.dumps([], indent=0, ensure_ascii=False)+"\r\n")  # 写入空值重新循环
                    else:
                        ddd.pop()  # 删除最后一个。
                                           
            except Exception as e:
                print(e)
                print("--Err--")
                #ddd.pop()  # 删除最后一个。===========临时用
        else:
            ddd.pop()  # 删除最后一个。

    else:
        ddd.pop()  # 删除最后一个。


with open(f'_new_data_HK1.txt', 'w', encoding='utf-8', newline='\r\n') as f:
    #f.write(json.dumps(ddd2, indent=4, ensure_ascii=False)+"\r\n")
    f.write(json.dumps(nnn, ensure_ascii=False))
    #f.write(json.dumps(ddd2, indent=0, ensure_ascii=False)+"\r\n")


print("--end--")






time.sleep(6)
import os

# 启动第一个程序
# 这里假设第一个程序是 test1.py
os.system("python 110_●前复权数据HK1上传同步.py")
