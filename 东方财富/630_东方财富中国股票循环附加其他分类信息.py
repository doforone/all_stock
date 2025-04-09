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


with open('000_东方财富中国全部股票.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
    ddd=json.loads(f.read())

##with open('data/雪球_中国股票_申万行业分类.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
##    ddd3=json.loads(f.read())
##    ddd3={v["encode"]:v["name"] for v in ddd3["data"]["industries"]}


ddd3=[{
		"key": "boards2-90.BK0474",
		"title": "保险",
		"href": "/center/boardlist.html#boards2-90.BK0474",
		"target": "_self",
		"groupKey": "B",
		"order": 472
	}, {
		"key": "boards2-90.BK0733",
		"title": "包装材料",
		"href": "/center/boardlist.html#boards2-90.BK0733",
		"target": "_self",
		"groupKey": "",
		"order": 473
	}, {
		"key": "boards2-90.BK1036",
		"title": "半导体",
		"href": "/center/boardlist.html#boards2-90.BK1036",
		"target": "_self",
		"groupKey": "",
		"order": 474
	}, {
		"key": "boards2-90.BK0546",
		"title": "玻璃玻纤",
		"href": "/center/boardlist.html#boards2-90.BK0546",
		"target": "_self",
		"groupKey": "",
		"order": 475
	}, {
		"key": "boards2-90.BK0729",
		"title": "船舶制造",
		"href": "/center/boardlist.html#boards2-90.BK0729",
		"target": "_self",
		"groupKey": "C",
		"order": 476
	}, {
		"key": "boards2-90.BK1017",
		"title": "采掘行业",
		"href": "/center/boardlist.html#boards2-90.BK1017",
		"target": "_self",
		"groupKey": "",
		"order": 477
	}, {
		"key": "boards2-90.BK0738",
		"title": "多元金融",
		"href": "/center/boardlist.html#boards2-90.BK0738",
		"target": "_self",
		"groupKey": "D",
		"order": 478
	}, {
		"key": "boards2-90.BK1033",
		"title": "电池",
		"href": "/center/boardlist.html#boards2-90.BK1033",
		"target": "_self",
		"groupKey": "",
		"order": 479
	}, {
		"key": "boards2-90.BK1030",
		"title": "电机",
		"href": "/center/boardlist.html#boards2-90.BK1030",
		"target": "_self",
		"groupKey": "",
		"order": 480
	}, {
		"key": "boards2-90.BK0428",
		"title": "电力行业",
		"href": "/center/boardlist.html#boards2-90.BK0428",
		"target": "_self",
		"groupKey": "",
		"order": 481
	}, {
		"key": "boards2-90.BK0457",
		"title": "电网设备",
		"href": "/center/boardlist.html#boards2-90.BK0457",
		"target": "_self",
		"groupKey": "",
		"order": 482
	}, {
		"key": "boards2-90.BK1034",
		"title": "电源设备",
		"href": "/center/boardlist.html#boards2-90.BK1034",
		"target": "_self",
		"groupKey": "",
		"order": 483
	}, {
		"key": "boards2-90.BK1039",
		"title": "电子化学品",
		"href": "/center/boardlist.html#boards2-90.BK1039",
		"target": "_self",
		"groupKey": "",
		"order": 484
	}, {
		"key": "boards2-90.BK0459",
		"title": "电子元件",
		"href": "/center/boardlist.html#boards2-90.BK0459",
		"target": "_self",
		"groupKey": "",
		"order": 485
	}, {
		"key": "boards2-90.BK1045",
		"title": "房地产服务",
		"href": "/center/boardlist.html#boards2-90.BK1045",
		"target": "_self",
		"groupKey": "F",
		"order": 486
	}, {
		"key": "boards2-90.BK0451",
		"title": "房地产开发",
		"href": "/center/boardlist.html#boards2-90.BK0451",
		"target": "_self",
		"groupKey": "",
		"order": 487
	}, {
		"key": "boards2-90.BK0436",
		"title": "纺织服装",
		"href": "/center/boardlist.html#boards2-90.BK0436",
		"target": "_self",
		"groupKey": "",
		"order": 488
	}, {
		"key": "boards2-90.BK1020",
		"title": "非金属材料",
		"href": "/center/boardlist.html#boards2-90.BK1020",
		"target": "_self",
		"groupKey": "",
		"order": 489
	}, {
		"key": "boards2-90.BK1032",
		"title": "风电设备",
		"href": "/center/boardlist.html#boards2-90.BK1032",
		"target": "_self",
		"groupKey": "",
		"order": 490
	}, {
		"key": "boards2-90.BK1031",
		"title": "光伏设备",
		"href": "/center/boardlist.html#boards2-90.BK1031",
		"target": "_self",
		"groupKey": "G",
		"order": 491
	}, {
		"key": "boards2-90.BK1038",
		"title": "光学光电子",
		"href": "/center/boardlist.html#boards2-90.BK1038",
		"target": "_self",
		"groupKey": "",
		"order": 492
	}, {
		"key": "boards2-90.BK0427",
		"title": "公用事业",
		"href": "/center/boardlist.html#boards2-90.BK0427",
		"target": "_self",
		"groupKey": "",
		"order": 493
	}, {
		"key": "boards2-90.BK0425",
		"title": "工程建设",
		"href": "/center/boardlist.html#boards2-90.BK0425",
		"target": "_self",
		"groupKey": "",
		"order": 494
	}, {
		"key": "boards2-90.BK0739",
		"title": "工程机械",
		"href": "/center/boardlist.html#boards2-90.BK0739",
		"target": "_self",
		"groupKey": "",
		"order": 495
	}, {
		"key": "boards2-90.BK0726",
		"title": "工程咨询服务",
		"href": "/center/boardlist.html#boards2-90.BK0726",
		"target": "_self",
		"groupKey": "",
		"order": 496
	}, {
		"key": "boards2-90.BK0732",
		"title": "贵金属",
		"href": "/center/boardlist.html#boards2-90.BK0732",
		"target": "_self",
		"groupKey": "",
		"order": 497
	}, {
		"key": "boards2-90.BK0479",
		"title": "钢铁行业",
		"href": "/center/boardlist.html#boards2-90.BK0479",
		"target": "_self",
		"groupKey": "",
		"order": 498
	}, {
		"key": "boards2-90.BK0447",
		"title": "互联网服务",
		"href": "/center/boardlist.html#boards2-90.BK0447",
		"target": "_self",
		"groupKey": "H",
		"order": 499
	}, {
		"key": "boards2-90.BK0731",
		"title": "化肥行业",
		"href": "/center/boardlist.html#boards2-90.BK0731",
		"target": "_self",
		"groupKey": "",
		"order": 500
	}, {
		"key": "boards2-90.BK0471",
		"title": "化纤行业",
		"href": "/center/boardlist.html#boards2-90.BK0471",
		"target": "_self",
		"groupKey": "",
		"order": 501
	}, {
		"key": "boards2-90.BK1019",
		"title": "化学原料",
		"href": "/center/boardlist.html#boards2-90.BK1019",
		"target": "_self",
		"groupKey": "",
		"order": 502
	}, {
		"key": "boards2-90.BK0538",
		"title": "化学制品",
		"href": "/center/boardlist.html#boards2-90.BK0538",
		"target": "_self",
		"groupKey": "",
		"order": 503
	}, {
		"key": "boards2-90.BK0465",
		"title": "化学制药",
		"href": "/center/boardlist.html#boards2-90.BK0465",
		"target": "_self",
		"groupKey": "",
		"order": 504
	}, {
		"key": "boards2-90.BK0728",
		"title": "环保行业",
		"href": "/center/boardlist.html#boards2-90.BK0728",
		"target": "_self",
		"groupKey": "",
		"order": 505
	}, {
		"key": "boards2-90.BK0420",
		"title": "航空机场",
		"href": "/center/boardlist.html#boards2-90.BK0420",
		"target": "_self",
		"groupKey": "",
		"order": 506
	}, {
		"key": "boards2-90.BK0480",
		"title": "航天航空",
		"href": "/center/boardlist.html#boards2-90.BK0480",
		"target": "_self",
		"groupKey": "",
		"order": 507
	}, {
		"key": "boards2-90.BK0450",
		"title": "航运港口",
		"href": "/center/boardlist.html#boards2-90.BK0450",
		"target": "_self",
		"groupKey": "",
		"order": 508
	}, {
		"key": "boards2-90.BK0429",
		"title": "交运设备",
		"href": "/center/boardlist.html#boards2-90.BK0429",
		"target": "_self",
		"groupKey": "J",
		"order": 509
	}, {
		"key": "boards2-90.BK0456",
		"title": "家电行业",
		"href": "/center/boardlist.html#boards2-90.BK0456",
		"target": "_self",
		"groupKey": "",
		"order": 510
	}, {
		"key": "boards2-90.BK0440",
		"title": "家用轻工",
		"href": "/center/boardlist.html#boards2-90.BK0440",
		"target": "_self",
		"groupKey": "",
		"order": 511
	}, {
		"key": "boards2-90.BK0740",
		"title": "教育",
		"href": "/center/boardlist.html#boards2-90.BK0740",
		"target": "_self",
		"groupKey": "",
		"order": 512
	}, {
		"key": "boards2-90.BK0735",
		"title": "计算机设备",
		"href": "/center/boardlist.html#boards2-90.BK0735",
		"target": "_self",
		"groupKey": "",
		"order": 513
	}, {
		"key": "boards2-90.BK0485",
		"title": "旅游酒店",
		"href": "/center/boardlist.html#boards2-90.BK0485",
		"target": "_self",
		"groupKey": "L",
		"order": 514
	}, {
		"key": "boards2-90.BK0437",
		"title": "煤炭行业",
		"href": "/center/boardlist.html#boards2-90.BK0437",
		"target": "_self",
		"groupKey": "M",
		"order": 515
	}, {
		"key": "boards2-90.BK1035",
		"title": "美容护理",
		"href": "/center/boardlist.html#boards2-90.BK1035",
		"target": "_self",
		"groupKey": "",
		"order": 516
	}, {
		"key": "boards2-90.BK0484",
		"title": "贸易行业",
		"href": "/center/boardlist.html#boards2-90.BK0484",
		"target": "_self",
		"groupKey": "",
		"order": 517
	}, {
		"key": "boards2-90.BK0433",
		"title": "农牧饲渔",
		"href": "/center/boardlist.html#boards2-90.BK0433",
		"target": "_self",
		"groupKey": "N",
		"order": 518
	}, {
		"key": "boards2-90.BK0730",
		"title": "农药兽药",
		"href": "/center/boardlist.html#boards2-90.BK0730",
		"target": "_self",
		"groupKey": "",
		"order": 519
	}, {
		"key": "boards2-90.BK1015",
		"title": "能源金属",
		"href": "/center/boardlist.html#boards2-90.BK1015",
		"target": "_self",
		"groupKey": "",
		"order": 520
	}, {
		"key": "boards2-90.BK0477",
		"title": "酿酒行业",
		"href": "/center/boardlist.html#boards2-90.BK0477",
		"target": "_self",
		"groupKey": "",
		"order": 521
	}, {
		"key": "boards2-90.BK1016",
		"title": "汽车服务",
		"href": "/center/boardlist.html#boards2-90.BK1016",
		"target": "_self",
		"groupKey": "Q",
		"order": 522
	}, {
		"key": "boards2-90.BK0481",
		"title": "汽车零部件",
		"href": "/center/boardlist.html#boards2-90.BK0481",
		"target": "_self",
		"groupKey": "",
		"order": 523
	}, {
		"key": "boards2-90.BK1029",
		"title": "汽车整车",
		"href": "/center/boardlist.html#boards2-90.BK1029",
		"target": "_self",
		"groupKey": "",
		"order": 524
	}, {
		"key": "boards2-90.BK1028",
		"title": "燃气",
		"href": "/center/boardlist.html#boards2-90.BK1028",
		"target": "_self",
		"groupKey": "R",
		"order": 525
	}, {
		"key": "boards2-90.BK0737",
		"title": "软件开发",
		"href": "/center/boardlist.html#boards2-90.BK0737",
		"target": "_self",
		"groupKey": "",
		"order": 526
	}, {
		"key": "boards2-90.BK0482",
		"title": "商业百货",
		"href": "/center/boardlist.html#boards2-90.BK0482",
		"target": "_self",
		"groupKey": "S",
		"order": 527
	}, {
		"key": "boards2-90.BK0454",
		"title": "塑料制品",
		"href": "/center/boardlist.html#boards2-90.BK0454",
		"target": "_self",
		"groupKey": "",
		"order": 528
	}, {
		"key": "boards2-90.BK0424",
		"title": "水泥建材",
		"href": "/center/boardlist.html#boards2-90.BK0424",
		"target": "_self",
		"groupKey": "",
		"order": 529
	}, {
		"key": "boards2-90.BK1044",
		"title": "生物制品",
		"href": "/center/boardlist.html#boards2-90.BK1044",
		"target": "_self",
		"groupKey": "",
		"order": 530
	}, {
		"key": "boards2-90.BK0464",
		"title": "石油行业",
		"href": "/center/boardlist.html#boards2-90.BK0464",
		"target": "_self",
		"groupKey": "",
		"order": 531
	}, {
		"key": "boards2-90.BK0438",
		"title": "食品饮料",
		"href": "/center/boardlist.html#boards2-90.BK0438",
		"target": "_self",
		"groupKey": "",
		"order": 532
	}, {
		"key": "boards2-90.BK0736",
		"title": "通信服务",
		"href": "/center/boardlist.html#boards2-90.BK0736",
		"target": "_self",
		"groupKey": "T",
		"order": 533
	}, {
		"key": "boards2-90.BK0448",
		"title": "通信设备",
		"href": "/center/boardlist.html#boards2-90.BK0448",
		"target": "_self",
		"groupKey": "",
		"order": 534
	}, {
		"key": "boards2-90.BK0545",
		"title": "通用设备",
		"href": "/center/boardlist.html#boards2-90.BK0545",
		"target": "_self",
		"groupKey": "",
		"order": 535
	}, {
		"key": "boards2-90.BK0421",
		"title": "铁路公路",
		"href": "/center/boardlist.html#boards2-90.BK0421",
		"target": "_self",
		"groupKey": "",
		"order": 536
	}, {
		"key": "boards2-90.BK0486",
		"title": "文化传媒",
		"href": "/center/boardlist.html#boards2-90.BK0486",
		"target": "_self",
		"groupKey": "W",
		"order": 537
	}, {
		"key": "boards2-90.BK0422",
		"title": "物流行业",
		"href": "/center/boardlist.html#boards2-90.BK0422",
		"target": "_self",
		"groupKey": "",
		"order": 538
	}, {
		"key": "boards2-90.BK1027",
		"title": "小金属",
		"href": "/center/boardlist.html#boards2-90.BK1027",
		"target": "_self",
		"groupKey": "X",
		"order": 539
	}, {
		"key": "boards2-90.BK1018",
		"title": "橡胶制品",
		"href": "/center/boardlist.html#boards2-90.BK1018",
		"target": "_self",
		"groupKey": "",
		"order": 540
	}, {
		"key": "boards2-90.BK1037",
		"title": "消费电子",
		"href": "/center/boardlist.html#boards2-90.BK1037",
		"target": "_self",
		"groupKey": "",
		"order": 541
	}, {
		"key": "boards2-90.BK0458",
		"title": "仪器仪表",
		"href": "/center/boardlist.html#boards2-90.BK0458",
		"target": "_self",
		"groupKey": "Y",
		"order": 542
	}, {
		"key": "boards2-90.BK0727",
		"title": "医疗服务",
		"href": "/center/boardlist.html#boards2-90.BK0727",
		"target": "_self",
		"groupKey": "",
		"order": 543
	}, {
		"key": "boards2-90.BK1041",
		"title": "医疗器械",
		"href": "/center/boardlist.html#boards2-90.BK1041",
		"target": "_self",
		"groupKey": "",
		"order": 544
	}, {
		"key": "boards2-90.BK1042",
		"title": "医药商业",
		"href": "/center/boardlist.html#boards2-90.BK1042",
		"target": "_self",
		"groupKey": "",
		"order": 545
	}, {
		"key": "boards2-90.BK0478",
		"title": "有色金属",
		"href": "/center/boardlist.html#boards2-90.BK0478",
		"target": "_self",
		"groupKey": "",
		"order": 546
	}, {
		"key": "boards2-90.BK1046",
		"title": "游戏",
		"href": "/center/boardlist.html#boards2-90.BK1046",
		"target": "_self",
		"groupKey": "",
		"order": 547
	}, {
		"key": "boards2-90.BK0475",
		"title": "银行",
		"href": "/center/boardlist.html#boards2-90.BK0475",
		"target": "_self",
		"groupKey": "",
		"order": 548
	}, {
		"key": "boards2-90.BK1043",
		"title": "专业服务",
		"href": "/center/boardlist.html#boards2-90.BK1043",
		"target": "_self",
		"groupKey": "Z",
		"order": 549
	}, {
		"key": "boards2-90.BK0910",
		"title": "专用设备",
		"href": "/center/boardlist.html#boards2-90.BK0910",
		"target": "_self",
		"groupKey": "",
		"order": 550
	}, {
		"key": "boards2-90.BK1040",
		"title": "中药",
		"href": "/center/boardlist.html#boards2-90.BK1040",
		"target": "_self",
		"groupKey": "",
		"order": 551
	}, {
		"key": "boards2-90.BK0734",
		"title": "珠宝首饰",
		"href": "/center/boardlist.html#boards2-90.BK0734",
		"target": "_self",
		"groupKey": "",
		"order": 552
	}, {
		"key": "boards2-90.BK0539",
		"title": "综合行业",
		"href": "/center/boardlist.html#boards2-90.BK0539",
		"target": "_self",
		"groupKey": "",
		"order": 553
	}, {
		"key": "boards2-90.BK0476",
		"title": "装修建材",
		"href": "/center/boardlist.html#boards2-90.BK0476",
		"target": "_self",
		"groupKey": "",
		"order": 554
	}, {
		"key": "boards2-90.BK0725",
		"title": "装修装饰",
		"href": "/center/boardlist.html#boards2-90.BK0725",
		"target": "_self",
		"groupKey": "",
		"order": 555
	}, {
		"key": "boards2-90.BK0473",
		"title": "证券",
		"href": "/center/boardlist.html#boards2-90.BK0473",
		"target": "_self",
		"groupKey": "",
		"order": 556
	}, {
		"key": "boards2-90.BK0470",
		"title": "造纸印刷",
		"href": "/center/boardlist.html#boards2-90.BK0470",
		"target": "_self",
		"groupKey": "",
		"order": 557
	}]


for dd3 in ddd3:
    print(dd3)
    for i in range(1,999999):
        #time.sleep(random.randint(1, 1))
        time.sleep(random.random())
        print(i)
        
        # 请求的URL
        url = f'https://80.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124021655675155099519_1707224394394&pn={i}\
&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=b:{dd3["key"][-6:]}+f:!50\
&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152,f45&_=1707224394404'

        #print(url)

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

        ddd2 = data.decode('utf-8')
        p_l=ddd2.find("\"diff\":[")
        if p_l==-1:
            break

        p_l+=7
        p_r=ddd2.find("}});")
        ddd2=ddd2[p_l:p_r]
        ddd2 = json.loads(ddd2)
        if ddd2==[]:
            break
        
    ##    for dd2 in ddd2:
    ##        if dd2["f12"] not in ddd.keys():
    ##            ddd[dd2["f12"]]=[dd2["f14"]]

        for dd2 in ddd2:
            if dd2["f12"] not in ddd.keys():
                ddd[dd2["f12"]]=[dd2["f14"],f"&{dd3['title']}"]
            else:
                ddd[dd2["f12"]].append(f"&{dd3['title']}")  # RM:热门概念,GN:概念板块,#:地域板块,*:分类,&美股指数

    with open(f'000_东方财富中国全部股票.txt', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(json.dumps(ddd, indent=4, ensure_ascii=False)+"\r\n")

print("--end--")
