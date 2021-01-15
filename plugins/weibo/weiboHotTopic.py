'''
Author: GoogTech
Date: 2021-01-02 15:40:49
LastEditTime: 2021-01-03 17:40:48
Description: 获取微博热门话题数据
Reference: 
https://www.cnblogs.com/wxhou/p/13771382.html
https://www.cnblogs.com/rainights/p/13278702.html
'''

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
# from prettytable import PrettyTable

import sys
# 打印所有 python 解释器可以搜索到的所有路径
sys.path.append('../../')
# print(sys.path)
# 导入自定义包
from tools.ttsTool import *

# 请求链接及请求头
url = 'https://s.weibo.com/top/summary'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


class weiboHotTopic(object):

    # 获取网页 html 内容
    @staticmethod
    def get_HTMLText():
        r = requests.get(url, headers=headers)
        r.encoding = r.apparent_encoding
        html_text = r.text
        return html_text

    # 获取微博热门话题数据
    @staticmethod
    def getHotTop():
        results = []
        htmls = weiboHotTopic.get_HTMLText()
        soup = BeautifulSoup(htmls, 'lxml')
        # 分别通过三个 find_all 方法获取到所有所需的数据文本
        ranks = soup.find_all('td', class_='td-01 ranktop')
        tags = soup.find_all('td', class_='td-02')
        hots = soup.find_all('td', class_='td-03')
        # 通过zip方法把每一组放在各自的列表中
        for rank, tag, hot in zip(ranks, tags, hots):
            results.append([
                rank.string if rank else '',  # 序号
                tag.a.string,  # 热门话题标题
                tag.span.string
                if tag.span else 9999999,  # 最热门的话题没有热点浏览次数, 及设置为9999999
                hot.i.string if hot.i else '空'  # 热点类型, 即 '新'、'热'、'推'、'沸'...
            ])
        return results

    # 输出微博热门话题数据
    @staticmethod
    def showData(row):
        datas = weiboHotTopic.getHotTop()
        # 格式化遍历输出
        print('{}\t{:30}\t{:30}\t{:30}\t\n'.format('序号', '热门话题关键字', '热点浏览次数',
                                                   '热点类型'))
        # 存储数据, 用于语音播报
        forcast_txt = "以下播报的是今日微博排行榜前十的热门话题 : \t\nn"
        count = 1
        for i, j, k, m in datas:
            if count <= row:
                print('{}\t{:30}\t{:30}\t{:30}\t\n'.format(i, j, k, m))
                forcast_txt += '排行榜第{}名: \t{:30}, \t浏览次数为: {:30}, \t热点类型为: {:30}。\t\n'.format(
                    i, j, k, m)
                count += 1
        return forcast_txt

    # 获取微博要闻榜数据
    @staticmethod
    def getNewsTop(row):
        pass

    # 运行程序
    @staticmethod
    def run():
        # 获取前 10 条热点话题, 全部共计 50 条数据
        datas = weiboHotTopic.showData(10)
        # 语音播报今日微博排行榜前十的热门话题, 最后将其文本数据推送到微信
        ttsToool.Voice_broadcast(forcast_txt=datas)


""" 2021 01 02
序号    热门话题关键字                              热点浏览次数                      热点类型

1       元旦春节疫情防控提示                           9999999                          热

2       东方卫视跨年被指侵权                           3687708                          新

3       北京乘地铁不戴口罩不听劝阻可报警                2561085                          空

4       2021 重新上场                                 2309032                          荐

5       杨蓉 我是一个女生我希望她如愿                   2220472                          热

6       张文宏接种新冠疫苗                             1212397                          新

7       肖战 不是说大家是我妈的意思                     1148267                          沸

8       昆凌肚子                                      1104991                          热

9       小红花里的吃外卖大叔                           1014182                          新

10      公民在庄重的场合可以佩戴国徽徽章                975268                           空
"""
