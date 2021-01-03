'''
Author: GoogTech
Date: 2021-01-02 15:40:49
LastEditTime: 2021-01-03 12:15:17
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

# 请求链接及请求头
url = 'https://s.weibo.com/top/summary'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


# 获取网页 html 内容
def get_HTMLText():
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    html_text = r.text
    return html_text


# 获取微博热门话题数据
def getHotTop():
    results = []
    htmls = get_HTMLText()
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
            hot.i.string if hot.i else ''  # 热点类型, 即 '新'、'热'、'推'、'沸'...
        ])
    return results


# 输出微博热门话题数据
def showData(row):
    datas = getHotTop()
    # 格式化遍历输出
    print('{}\t{:30}\t{:30}\t{:30}\t\n'.format('序号', '热门话题关键字', '热点浏览次数',
                                               '热点类型'))
    count = 1
    for i, j, k, m in datas:
        if count <= row:
            print('{}\t{:30}\t{:30}\t{:30}\t\n'.format(i, j, k, m))
            count += 1


# 获取微博要闻榜数据
def getNewsTop(row):
    pass


# 主函数
if __name__ == "__main__":
    # 获取前 10 条热点话题, 全部共计 50 条数据
    showData(10)
    
""" 2021 01 02
序号    热门话题关键字                              热点浏览次数                      热点类型

1       元旦春节疫情防控提示                           9999999                          热

2       东方卫视跨年被指侵权                           3687708                          新

3       北京乘地铁不戴口罩不听劝阻可报警                2561085

4       2021 重新上场                                 2309032                          荐

5       杨蓉 我是一个女生我希望她如愿                   2220472                          热

6       张文宏接种新冠疫苗                             1212397                          新

7       肖战 不是说大家是我妈的意思                     1148267                          沸

8       昆凌肚子                                      1104991                          热

9       小红花里的吃外卖大叔                           1014182                          新

10      公民在庄重的场合可以佩戴国徽徽章                975268
"""
