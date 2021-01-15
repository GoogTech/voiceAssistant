'''
Author: GoogTech
Date: 2021-01-02 17:16:44
LastEditTime: 2021-01-03 17:19:48
Description: 获取豆瓣近一周口碑榜、北美票房榜
'''
import requests
from bs4 import BeautifulSoup

import sys
# 打印所有 python 解释器可以搜索到的所有路径
sys.path.append('../../')
# print(sys.path)
# 导入自定义包
from tools.ttsTool import *

# 请求链接及请求头
url = "https://movie.douban.com/chart"
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


class moviceData(object):

    # 获取网页 html 内容
    @staticmethod
    def get_HTMLText():
        request = requests.get(url, headers=headers)
        request.encoding = request.apparent_encoding
        html_text = request.text
        return html_text

    # 获取豆瓣近一周电影口碑榜
    @staticmethod
    def week_MoveRanking():
        datas = []
        html = moviceData.get_HTMLText()
        soup = BeautifulSoup(html, 'lxml')
        updatedTime = soup.find('div',
                                class_='movie_top').h2.span.string  # 更新时间
        moviceNos = soup.find_all('div', class_='no')
        moviceNames = soup.find_all('div', class_='name')
        for moviceNo, moviceName in zip(moviceNos, moviceNames):
            datas.append([
                moviceNo.string,  # 电影排行榜序号
                moviceName.a.string.strip()  # 电影名称
            ])
        return updatedTime, datas

    # 输出豆瓣近一周电影口碑榜数据
    @staticmethod
    def showData(row):
        updatedTime, datas = moviceData.week_MoveRanking()
        print('更新时间: ', updatedTime)
        print('{}\t{:5}\t\n'.format('序号', '电影名称'))
        # 存储数据, 用于语音播报
        forcast_txt = "以下播报的是豆瓣近一周排名前十的电影口碑榜 : \t\n"
        count = 1
        for i, j in datas:
            if count <= row:
                print('{}\t{:5}\t\n'.format(i, j))
                forcast_txt += '第{}名: \t{:5}。\t\n'.format(i, j)
                count += 1
        return forcast_txt

    # 获取北美票房榜数据
    @staticmethod
    def northAmerica_MoveTop():
        pass

    # 运行程序
    @staticmethod
    def run():
        # 获取前 10 条热点话题, 全部共计 10 条数据
        datas = moviceData.showData(10)
        # 语音播报豆瓣近一周排名前十的电影口碑榜, 最后将其文本数据推送到微信
        ttsToool.Voice_broadcast(forcast_txt=datas)


"""
更新时间:  1月1日 更新
序号    电影名称

1       心灵奇旅

2       拆弹专家2

3       送你一朵小红花

4       画家与贼

5       行骗天下JP：公主篇      

6       2020去死

7       印第安纳的蒙罗维亚      

8       脚步

9       黑神驹

10      宇宙中最明亮的屋顶
"""
