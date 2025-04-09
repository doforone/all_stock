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
    
    with open('000_全部中国股票.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
        ddd=json.loads(f.read())

    mmm=["SH000001","SZ399001","SZ399006","SH000300","SH000016","SH000905",
         "SZ399005","SH000688"]

    print("沪深A股主板")
    sss="<p>"
    for dd in ddd.keys():
        if ddd[dd][2]==1 and ddd[dd][1][:2]!="BJ"\
           and ddd[dd][1]!="SH科创板" and ddd[dd][1]!="SZ创业板"\
           and ddd[dd][1]!="SZ深证B股" and ddd[dd][1]!="SH上证B股"\
           and dd not in mmm:
            sss+=f"&ensp;<a href='/data/CN0/{dd}_d.html'>\
{dd}：{ddd[dd][0].replace(' ', '')}</a>&ensp;|"

    sss+="</p>"
    print(sss)


    print("SH科创板\SZ创业板")
    sss="<p>"
    for dd in ddd.keys():
        if ddd[dd][2]==1\
           and (ddd[dd][1]=="SH科创板" or ddd[dd][1]=="SZ创业板")\
           and dd not in mmm:
            sss+=f"&ensp;<a href='/data/CN0/{dd}_d.html'>\
{dd}：{ddd[dd][0].replace(' ', '')}</a>&ensp;|"

    sss+="</p>"
    print(sss)


    print("BJ北证A股")
    sss="<p>"
    for dd in ddd.keys():
        if ddd[dd][2]==1\
           and (ddd[dd][1]=="BJ北证A股")\
           and dd not in mmm:
            sss+=f"&ensp;<a href='/data/CN0/{dd}_d.html'>\
{dd}：{ddd[dd][0].replace(' ', '')}</a>&ensp;|"

    sss+="</p>"
    print(sss)



    print("沪深B股")
    sss="<p>"
    for dd in ddd.keys():
        if ddd[dd][2]==1 and dd not in mmm\
           and (ddd[dd][1]=="SH上证B股" or ddd[dd][1]=="SZ深证B股"):
            sss+=f"&ensp;<a href='/data/CN0/{dd}_d.html'>\
{dd}：{ddd[dd][0].replace(' ', '')}</a>&ensp;|"

    sss+="</p>"
    print(sss)
    


    print("AB股")
    sss="<p>"
    for dd in ddd.keys():
        if ddd[dd][2]==1 and dd not in mmm:
            for d in ddd[dd][4]:
                if d[:9]=="@深证AB股比价:"\
                   or d[:9]=="@上证AB股比价:":
                    sss+=f"&ensp;<a href='/data/CN0/{dd}_d.html'>\
{dd}：{ddd[dd][0].replace(' ', '')}</a>(B:<a href='/data/CN0/{dd[:2]+d[9:]}_d.html'>\
{dd[:2]+d[9:]}</a>)&ensp;|"

    sss+="</p>"
    print(sss)



    print("@A+H:")
    sss="<p>"
    for dd in ddd.keys():
        if ddd[dd][2]==1 and dd not in mmm:
            for d in ddd[dd][4]:
                if d[:5]=="@A+H:":
                    sss+=f"&ensp;<a href='/data/CN0/{dd}_d.html'>\
{dd}：{ddd[dd][0].replace(' ', '')}</a>(H:<a href='/data/HK0/{d[5:]}_d.html'>\
{d[5:]}</a>)&ensp;|"

    sss+="</p>"
    print(sss)
#............................

    print("中国股票非常分类")
    sss="<p>"
    for dd in ddd.keys():
        if ddd[dd][2]==1 and dd not in mmm:
            for d in ddd[dd][4]:
                if d=="@融资融券" or d=="RM:融资融券":
                    strr=f"000_中国股票分类_融资融券.html"
                    md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
                    sss+=f"&ensp;<a href='/data/CN0/{dd}_d.html'>{dd}：{ddd[dd][0].replace(' ', '')}</a>\
&ensp;|"
                    break
    sss+="</p>"

    with open(f'vip\\{strr}', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(sss)
    #print(sss)

    #---------

    sss="<p>"
    for dd in ddd.keys():
        if ddd[dd][2]==1 and dd not in mmm:
            for d in ddd[dd][4]:
                if d=="@核准制深证A股":
                    strr=f"000_中国股票分类_核准制深证A股.html"
                    md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
                    sss+=f"&ensp;<a href='/data/CN0/{dd}_d.html'>{dd}：{ddd[dd][0].replace(' ', '')}</a>\
&ensp;|"
                    break
    sss+="</p>"
    
    with open(f'vip\\{strr}', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(sss)
    #print(sss)

    #---------

    sss="<p>"
    for dd in ddd.keys():
        if ddd[dd][2]==1 and dd not in mmm:
            for d in ddd[dd][4]:
                if d=="@核准制上证A股":
                    strr=f"000_中国股票分类_核准制上证A股.html"
                    md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
                    sss+=f"&ensp;<a href='/data/CN0/{dd}_d.html'>{dd}：{ddd[dd][0].replace(' ', '')}</a>\
&ensp;|"
                    break
    sss+="</p>"
    
    with open(f'vip\\{strr}', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(sss)
    #print(sss)


    #---------

    sss="<p>"
    for dd in ddd.keys():
        if ddd[dd][2]==1 and dd not in mmm:
            for d in ddd[dd][4]:
                if d=="@核准制创业板":
                    strr=f"000_中国股票分类_核准制创业板.html"
                    md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
                    sss+=f"&ensp;<a href='/data/CN0/{dd}_d.html'>{dd}：{ddd[dd][0].replace(' ', '')}</a>\
&ensp;|"
                    break
    sss+="</p>"
    
    with open(f'vip\\{strr}', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(sss)
    #print(sss)

    #---------

    sss="<p>"
    for dd in ddd.keys():
        if ddd[dd][2]==1 and dd not in mmm:
            for d in ddd[dd][4]:
                if d=="@注册制上证A股":
                    strr=f"000_中国股票分类_注册制上证A股.html"
                    md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
                    sss+=f"&ensp;<a href='/data/CN0/{dd}_d.html'>{dd}：{ddd[dd][0].replace(' ', '')}</a>\
&ensp;|"
                    break
    sss+="</p>"
    
    with open(f'vip\\{strr}', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(sss)
    #print(sss)

    #---------

    sss="<p>"
    for dd in ddd.keys():
        if ddd[dd][2]==1 and dd not in mmm:
            for d in ddd[dd][4]:
                if d=="@注册制深证A股":
                    strr=f"000_中国股票分类_注册制深证A股.html"
                    md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
                    sss+=f"&ensp;<a href='/data/CN0/{dd}_d.html'>{dd}：{ddd[dd][0].replace(' ', '')}</a>\
&ensp;|"
                    break
    sss+="</p>"
    
    with open(f'vip\\{strr}', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(sss)
    #print(sss)

    #---------

    sss="<p>"
    for dd in ddd.keys():
        if ddd[dd][2]==1 and dd not in mmm:
            for d in ddd[dd][4]:
                if d=="@注册制创业板":
                    strr=f"000_中国股票分类_注册制创业板.html"
                    md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
                    sss+=f"&ensp;<a href='/data/CN0/{dd}_d.html'>{dd}：{ddd[dd][0].replace(' ', '')}</a>\
&ensp;|"
                    break
    sss+="</p>"
    
    with open(f'vip\\{strr}', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(sss)
    #print(sss)

    #---------

    sss="<p>"
    for dd in ddd.keys():
        if ddd[dd][2]==1 and dd not in mmm:
            for d in ddd[dd][4]:
                if d=="@深股通(港>深)":
                    strr=f"000_中国股票分类_深股通.html"
                    md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
                    sss+=f"&ensp;<a href='/data/CN0/{dd}_d.html'>{dd}：{ddd[dd][0].replace(' ', '')}</a>\
&ensp;|"
                    break
    sss+="</p>"
    
    with open(f'vip\\{strr}', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(sss)
    #print(sss)

    #---------

    sss="<p>"
    for dd in ddd.keys():
        if ddd[dd][2]==1 and dd not in mmm:
            for d in ddd[dd][4]:
                if d=="@沪股通(港>沪)":
                    strr=f"000_中国股票分类_沪股通.html"
                    md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
                    sss+=f"&ensp;<a href='/data/CN0/{dd}_d.html'>{dd}：{ddd[dd][0].replace(' ', '')}</a>\
&ensp;|"
                    break
    sss+="</p>"
    
    with open(f'vip\\{strr}', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(sss)
    #print(sss)

    #-----------------------


    sss="<p>"
    strr=f"000_中国股票分类_融资融券.html"
    md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
    sss+=f"&ensp;<a href='/vip/{md5_16}.html'>融资融券</a>&ensp;|"

    strr=f"000_中国股票分类_核准制深证A股.html"
    md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
    sss+=f"&ensp;<a href='/vip/{md5_16}.html'>核准制深证A股</a>&ensp;|"

    strr=f"000_中国股票分类_核准制上证A股.html"
    md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
    sss+=f"&ensp;<a href='/vip/{md5_16}.html'>核准制上证A股</a>&ensp;|"

    strr=f"000_中国股票分类_核准制创业板.html"
    md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
    sss+=f"&ensp;<a href='/vip/{md5_16}.html'>核准制创业板</a>&ensp;|"

    strr=f"000_中国股票分类_注册制上证A股.html"
    md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
    sss+=f"&ensp;<a href='/vip/{md5_16}.html'>注册制上证A股</a>&ensp;|"

    strr=f"000_中国股票分类_注册制深证A股.html"
    md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
    sss+=f"&ensp;<a href='/vip/{md5_16}.html'>注册制深证A股</a>&ensp;|"

    strr=f"000_中国股票分类_注册制创业板.html"
    md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
    sss+=f"&ensp;<a href='/vip/{md5_16}.html'>注册制创业板</a>&ensp;|"

    strr=f"000_中国股票分类_深股通.html"
    md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
    sss+=f"&ensp;<a href='/vip/{md5_16}.html'>深股通</a>&ensp;|"

    strr=f"000_中国股票分类_沪股通.html"
    md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
    sss+=f"&ensp;<a href='/vip/{md5_16}.html'>沪股通</a>&ensp;|"

    sss+="</p>"

    print(sss)
    #----------------------------
    aaa={'计算机设备', '氮肥', '镍', '铁路公路', '固废治理', '医疗服务', '种子', '煤化工', '锂电池', '医疗设备', '地面兵装', '乳品', '其他多元金融', '旅游综合', '摩托车', '电机Ⅱ', '娱乐用品', '通信线缆及配套', '农牧饲渔', '橡胶制品', '钨', '动力煤', '建筑装饰', '轻工制造', '面板', '航空装备Ⅲ', '防水材料', '专业连锁', '国有大型银行', '军工电子Ⅱ', '医美服务', '纺织服装', '农产品加工', '其他家电', '航空机场', '食品饮料', '分立器件', '房产租赁经纪', '白酒Ⅱ', '会展服务', '种植业', '采掘行业', '有机硅', '摩托车及其他', '诊断服务', '成品家居', '生物制品', '文化传媒', '工程咨询服务Ⅲ', '综合包装', '家电零部件', '租赁', '铅锌', '卫浴电器', '休闲食品', '空调', '玻璃制造', '林业Ⅱ', '水泥建材', '计算机', '其他家电Ⅱ', '环保设备Ⅱ', '白酒Ⅲ', '航天装备Ⅲ', '体外诊断', '其他家电Ⅲ', '旅游酒店', '线缆部件及其他', '仪器仪表', '广告营销', '其他电源设备', '保险', '地面兵装Ⅱ', '非运动服装', '自动化设备', '航天航空', '电视广播Ⅲ', '其他专用设备', '焦煤', '软件开发', '原料药', '国有大型银行Ⅲ', '塑料', '航运', '能源金属', '车身附件及饰件', '其他电源设备Ⅲ', '其他能源发电', '纸包装', '厨房小家电', '涂料', '调味发酵品Ⅲ', '油品石化贸易', '电子元件', '橡胶', '综合电力设备商', '机器人', '被动元件', '培训教育', '家电零部件Ⅱ', '化学制品', '物流行业', '贸易Ⅲ', '基础化工', '中药Ⅲ', '线下药店', '焦炭', '黄金', '电信运营商', '城商行Ⅱ', '服装家纺', '航空装备Ⅱ', '核力发电', '化纤行业', '工程机械', '特钢Ⅲ', '美容护理', '照明设备Ⅲ', '电力设备', '粮油加工', '通用设备', '军工电子', '文化用品', '学历教育', '体育Ⅲ', '农林牧渔', '冶钢辅料', '炼化及贸易', '钛白粉', '炭黑', '旅游零售Ⅱ', '氟化工', '电子', '银行', '公用事业', '旅游零售', '印刷', '其他通用设备', '其他计算机设备', '装修装饰Ⅱ', '硅料硅片', '稀土', '旅游零售Ⅲ', '综合电商', '钢铁管材', '工控设备', '医院', '海洋捕捞', '通信服务', '铁路运输', '其他酒类', '冰洗', '电视广播', '基础建设', '工程机械器件', '农商行Ⅱ', '油气开采Ⅱ', '家纺', '仓储物流', '林业Ⅲ', '电子化学品Ⅲ', '高速公路', '电网设备', '游戏Ⅱ', '医药商业', 'IT服务Ⅱ', '铜', '改性塑料', '期货', '体育', '产业地产', '血液制品', '其他塑料制品', '水泥', '橡胶助剂', '瓷砖地板', '火电设备', '铝', '造纸', '农药', '专用设备', '通信', '家用电器', '商贸零售', '焦炭Ⅲ', '定制家居', '辅料', '楼宇设备', '化肥行业', '其他化学纤维', '家居用品', '商用载客车', '钢铁行业', '家电零部件Ⅲ', '通信应用增值服务', '风力发电', '非金属材料Ⅱ', '油服工程', '果蔬加工', '游戏', '工程咨询服务Ⅱ', '电视广播Ⅱ', '风电设备', '零食', '保健品', '集成电路制造', '通信网络设备及器件', '有色金属', '城商行Ⅲ', '检测服务', '纺织制造', '数字芯片设计', '数字媒体', '钾肥', '原材料供应链服务', '配电设备', '通信终端及配件', '风电整机', '化学纤维', '综合环境治理', '其他建材', '热力服务', '半导体设备', '光学光电子', '教育出版', '环保设备Ⅲ', '电源设备', '油气及炼化工程', '装修建材', '医疗美容', '光伏辅材', '农业综合Ⅱ', '光伏加工设备', '航天装备', '影视动漫制作', '白色家电', '房屋建设Ⅱ', '汽车零部件', '汽车整车', '燃料电池', '电池', '煤炭行业', '航运港口', '金属包装', '纺织鞋类制造', 'IT服务Ⅲ', '房地产服务', '房屋建设', '化妆品', '环保行业', '金融信息服务', '水力发电', '氯碱', '汽车电子电气系统', '炼油化工', '商业物业经营', '模拟芯片设计', '复合肥', '其他家居用品', '城商行', '玻纤制造', '饮料乳品', '粘胶', '长材', '电子化学品Ⅱ', '医疗研发外包', '水务及水治理', '品牌化妆品', '预加工食品', '包装材料', '超市', '生猪养殖', '航海装备Ⅱ', '酿酒行业', '底盘与发动机系统', '金属新材料', '逆变器', '装修装饰', '航海装备', '膜材料', '地面兵装Ⅲ', '机床工具', '工程咨询服务', '航空运输', '自然景区', '黑色家电', '特种纸', '光伏设备', '医疗器械', '房地产开发', '光伏电池组件', '饰品', '影视院线', '珠宝首饰', '餐饮', '棉纺', '其他电子Ⅲ', '物业管理', '焦炭Ⅱ', '激光设备', '酒店', '印制电路板', '互联网服务', '商业百货', '农业综合Ⅲ', '专业服务', '保险Ⅲ', '煤炭开采', '电商服务', '交通运输', '氨纶', '金属制品', '纺织服装设备', '管材', '农业综合', '其他银行', '农药兽药', '输变电设备', '塑料包装', '软饮料', '磁性材料', '其他电子', '电力行业', '航天装备Ⅱ', '其他纺织', '建筑材料', '社交', '文字媒体', '港口', '其他养殖', '其他医疗服务', '半导体材料', '交运设备', '汽车服务', '化学制药', '医疗耗材', '清洁小家电', '人工景区', '贵金属', '普钢', '轮胎轮毂', '图片媒体', '电工仪器仪表', '人力资源服务', '综合行业', '证券', '保险Ⅱ', '综合乘用车', '国有大型银行Ⅱ', '化妆品制造及其他', '电机Ⅲ', '其他饰品', '电子化学品', '商用载货车', '板材', '钴', '合成树脂', '调味发酵品', '物流', '纺织服饰', '特钢', '军工电子Ⅲ', '钼', '厨卫电器', '渔业', '航空装备', '出版', '环境治理', '电网自动化设备', '股份制银行', '燃气Ⅱ', '大众出版', '耐火材料', '汽车', '医美耗材', '中药Ⅱ', '风电零部件', '文娱用品', '一般零售', '调味发酵品Ⅱ', '农商行Ⅲ', '其他小金属', '其他运输设备', '机械设备', '其他专业工程', '互联网电商', '公交', '油气开采', '体育Ⅱ', '油气开采Ⅲ', '个护用品', '贸易', '其他自动化设备', '食品加工', '其他种植业', '环保', '化学工程', '轨交设备Ⅲ', '多业态零售', '环保设备', '中药', '动物保健Ⅲ', '锦纶', '白银', '品牌消费电子', '非金属材料Ⅲ', '航海装备Ⅲ', '印染', '中间产品及消费品供应链服务', '肉制品', '小金属', '综合Ⅱ', '股份制银行Ⅲ', '玻璃玻纤', '水泥制品', '电能综合服务', '轨交设备', '其他橡胶制品', '无机盐', '门户网站', '照明设备Ⅱ', '游戏Ⅲ', '电机', '本地生活服务', '石油行业', '横向通用软件', '燃气Ⅲ', '其他电源设备Ⅱ', '铁矿石', '视频媒体', '锂', '化学制剂', '安防设备', '工程机械整机', '园林工程', '煤炭', '资产管理', '啤酒', '大宗用纸', '电力', '水产饲料', '塑料制品', '证券Ⅱ', '其他专业服务', '信托', '蓄电池及其他电池', '水产养殖', '消费电子零部件及组装', '林业', '跨境物流', '专业连锁Ⅱ', '制冷空调设备', '垂直应用软件', '非金属材料', '涂料油墨', '饲料', '燃气', '其他电子Ⅱ', '其他生物制品', '国际工程', '房地产', '基建市政工程', '院线', '聚氨酯', '工业金属', '机场', '综合', '电动乘用车', '油田服务', '个护小家电', '宠物食品', 'IT服务', '动物保健Ⅱ', '纯碱', '钢结构', '其他农产品加工', '疫苗', '跨境电商', '粮食种植', '农化制品', '广告媒体', '百货', '其他化学制品', '元件', '证券Ⅲ', '医药生物', '消费电子', 'LED', '照明设备', '运动服装', '特钢Ⅱ', '电池化学品', '家电行业', '钢铁', '锂电专用设备', '股份制银行Ⅱ', '商业地产', '生活用纸', '造纸印刷', '贸易Ⅱ', '纺织化学制品', '厨房电器', '其他石化', '金融控股', '食用菌', '化学原料', '磷肥及磷化工', '其他数字媒体', '住宅开发', '装修装饰Ⅲ', '汽车经销商', '教育', '商用车', '乘用车', '火力发电', '家用轻工', '农用机械', '印刷包装机械', '肉鸡养殖', '包装印刷', '传媒', '通信工程及服务', '营销代理', '其他金属新材料', '其他通信设备', '白酒', '涤纶', '动物保健', '民爆制品', '非白酒', '畜禽饲料', '卫浴制品', '食品及饲料添加剂', '烘焙食品', '集成电路封测', '钟表珠宝', '综合Ⅲ', '水泥制造', '专业连锁Ⅲ', '农商行', '半导体', '工程建设', '国防军工', '光伏发电', '贸易行业', '教育运营及其他', '汽车综合服务', '鞋帽及其他', '房屋建设Ⅲ', '熟食', '大气治理', '非银金融', '石油石化', '快递', '其他化学原料', '洗护用品', '酒店餐饮', '光学元件', '磨具磨料', '医药流通', '养殖业', '通信设备', '公路货运', '小家电', '旅游及景区', '社会服务', '其他汽车零部件', '能源及重型设备', '多元金融', '胶黏剂及胶带', '专业工程', '冶钢原料', '轨交设备Ⅱ', '彩电', '其他黑色家电', '船舶制造'}
    bbb={'公路桥梁', '纺织行业', '化工行业', '煤炭行业', '发电设备', '纺织机械', '电器行业', '酿酒行业', '机械行业', '玻璃行业', '房地产', '钢铁行业', '其它行业', '电力行业', '家电行业', '化纤行业', '传媒娱乐', '汽车制造', '造纸行业', '物资外贸', '电子信息', '摩托车', '环保行业', '金融行业', '供水供气', '医疗器械', '石油行业', '农林牧渔', '服装鞋类', '飞机制造', '农药化肥', '电子器件', '陶瓷行业', '综合行业', '家具行业', '建筑建材', '水泥行业', '开发区', '商业百货', '塑料制品', '有色金属', '生物制药', '交通运输', '仪器仪表', '印刷包装', '船舶制造', '酒店旅游', '食品行业'}
    aaa={f"@{v}" for v in aaa}
    bbb={f"&{v}" for v in bbb}
    ccc={'农、林、牧、渔业': ['农业', '林业', '畜牧业', '渔业', '农、林、牧、渔服务业'], '采矿业': ['煤炭开采和洗选业', '石油和天然气开采业', '黑色金属矿采选业', '有色金属矿采选业', '非金属矿采选业', '开采辅助活动', '其他采矿业'], '制造业': ['农副食品加工业', '食品制造业', '酒、饮料和精制茶制造业', '烟草制品业', '纺织业', '纺织服装、服饰业', '皮革、毛皮、羽毛及其制品和制鞋业', '木材加工和木、竹、藤、棕、草制品业', '家具制造业', '造纸和纸制品业', '印刷和记录媒介复制业', '文教、工美、体育和娱乐用品制造业', '石油加工、炼焦和核燃料加工业', '化学原料和化学制品制造业', '医药制造业', '化学纤维制造业', '橡胶和塑料制品业', '非金属矿物制品业', '黑色金属冶炼和压延加工业', '有色金属冶炼和压延加工业', '金属制品业', '通用设备制造业', '专用设备制造业', '汽车制造业', '铁路、船舶、航空航天和其他运输设备制造业', '电气机械和器材制造业', '计算机、通信和其他电子设备制造业', '仪器仪表制造业', '其他制造业', '废弃资源综合利用业', '金属制品、机械和设备修理业'], '电力、热力、燃气及水生产和供应业': ['电力、热力生产和供应业', '燃气生产和供应业', '水的生产和供应业'], '建筑业': ['房屋建筑业', '土木工程建筑业', '建筑安装业', '建筑装饰和其他建筑业'], '批发和零售业': ['批发业', '零售业'], '交通运输、仓储和邮政业': ['铁路运输业', '道路运输业', '水上运输业', '航空运输业', '管道运输业', '装卸搬运和运输代理业', '仓储业', '邮政业'], '住宿和餐饮业': ['住宿业', '餐饮业'], '信息传输、软件和信息技术服务业': ['电信、广播电视和卫星传输服务', '互联网和相关服务', '软件和信息技术服务业'], '金融业': ['货币金融服务', '资本市场服务', '保险业', '其他金融业'], '房地产业': ['房地产业'], '租赁和商务服务业': ['租赁业', '商务服务业'], '科学研究和技术服务业': ['研究和试验发展', '专业技术服务业', '科技推广和应用服务业'], '水利、环境和公共设施管理业': ['水利管理业', '生态保护和环境治理业', '公共设施管理业'], '居民服务、修理和其他服务业': ['居民服务业', '机动车、电子产品和日用产品修理业', '其他服务业'], '教育': ['教育'], '卫生和社会工作': ['卫生', '社会工作'], '文化、体育和娱乐业': ['新闻和出版业', '广播、电视、电影和影视录音制作业', '文化艺术业', '体育', '娱乐业'], '综合': ['综合']}
    ccc2=set()

    for cc in ccc.keys():
        for c in ccc[cc]:
            ccc2.add(f"@{cc}:{c}")


    hhh=["广东","浙江","江苏","北京","上海","山东","安徽","四川","福建","湖北","湖南","河南","江西","辽宁","陕西","河北","重庆",\
         "天津","新疆","吉林","山西","云南","广西","黑龙江","贵州","甘肃","海南","内蒙古","西藏","宁夏","青海"]


    with open('000_全部行业.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
        uuu=json.loads(f.read())


    print("中国股票分类1")
    sss="<p>"
    for uu in uuu.keys():
        if uu in aaa or uu in bbb:
            strr=f"000_中国股票分类_{uu[1:]}.html"
            md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
            sss+=f"&ensp;<a href='/vip/{md5_16}.html'>{uu[1:]}</a>&ensp;|"
    sss+="</p>"
    print(sss)



    for uu in uuu.keys():
        if uu in aaa or uu in bbb:
            strr=f"000_中国股票分类_{uu[1:]}.html"
            #md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
            sss="<p>"
            for dd in ddd.keys():
                if ddd[dd][2]==1 and uu in ddd[dd][4] and dd not in mmm:
                    sss+=f"&ensp;<a href='/data/CN0/{dd}_d.html'>{dd}：{ddd[dd][0].replace(' ', '')}</a>&ensp;|"
                    #break
            sss+="</p>"
                    
            with open(f'vip\\{strr}', 'w', encoding='utf-8', newline='\r\n') as f:
                f.write(sss)


    print("中国股票分类2")
    sss=""
    for cc in ccc.keys():  # 注意厦门的大小冒号之分
        sss+=f"<p>{cc}：<br/>"
        for c in ccc[cc]:
            if f"@{cc}:{c}" in uuu.keys():
                strr=f"000_中国股票分类_{cc}：{c}.html"  # 文件名用大冒号
                md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
                sss+=f"&ensp;<a href='/vip/{md5_16}.html'>{c}</a>&ensp;|"
        sss+="</p>"
    print(sss)



    for uu in uuu.keys():
        if uu in ccc2:
            strr=f"000_中国股票分类_{uu[1:].replace(':','：')}.html"
            #md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
            sss="<p>"
            for dd in ddd.keys():
                if ddd[dd][2]==1 and uu in ddd[dd][4] and dd not in mmm:
                    sss+=f"&ensp;<a href='/data/CN0/{dd}_d.html'>{dd}：{ddd[dd][0].replace(' ', '')}</a>&ensp;|"
                    #break
            sss+="</p>"
                    
            with open(f'vip\\{strr}', 'w', encoding='utf-8', newline='\r\n') as f:
                f.write(sss)



    print("地区板块分类")
    sss="<p>"
    for hh in hhh:
        strr=f"000_中国股票分类_{hh}.html"
        md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
        sss+=f"&ensp;<a href='/vip/{md5_16}.html'>{hh}</a>&ensp;|"
    sss+="</p>"
    print(sss)



    for hh in hhh:
        sss="<p>"
        for dd in ddd.keys():
            if ddd[dd][2]==1 and dd not in mmm:
                for d in ddd[dd][4]:
                    if d[:1]=="#" and hh in d:
                        strr=f"000_中国股票分类_{hh}.html"
                        #md5_16=hashlib.md5(strr.encode(encoding='UTF-8')).hexdigest()[:16]
                        sss+=f"&ensp;<a href='/data/CN0/{dd}_d.html'>{dd}：{ddd[dd][0].replace(' ', '')}</a>&ensp;|"
                        break
        sss+="</p>"
                    
        with open(f'vip\\{strr}', 'w', encoding='utf-8', newline='\r\n') as f:
            f.write(sss)


print("end")












        
