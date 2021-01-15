'''
Author: GoogTech
Date: 2021-01-02 11:49:16
LastEditTime: 2021-01-03 16:55:44
Description: 获取百度实时、今日、七日热点事件排行榜数据
Reference: https://www.cnblogs.com/-stewart/p/12521202.html
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
url = 'http://top.baidu.com/buzz/shijian.html'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

class baiduTopNews(object):
    # 获取网页 html 内容
    @staticmethod
    def get_HTMLText():
        urls = requests.get(url, headers=headers)
        urls.encoding = urls.apparent_encoding
        html_text = urls.text
        return html_text


    # 获取今日热点事件
    @staticmethod
    def today_News():
        # 使用 lxml HTML 解析器: 速度快、文档容错能力强
        soup = BeautifulSoup(baiduTopNews.get_HTMLText(), 'lxml')
        # 获取所有 class 属性为 list-title 的标签元素, 即热点事件标题
        all_list_title = soup.find_all(class_="list-title")
        # 获取今日全部热点事件标题, 即 50 个
        # all_news_title_text = [i.get_text() for i in all_list_title]
        # 获取 10 个今日热点事件标题
        all_news_title_text, count = [], 0
        for title in all_list_title:
            if count < 10:
                count += 1
                all_news_title_text.append(title.get_text())
        # 获取所有 class 属性为 last 的标签元素, 即搜索指数
        all_exponent = soup.find_all('td', class_="last")
        all_exponent_text = [i.get_text().strip() for i in all_exponent]
        # 存储数据,用于语音播报
        forcast_txt = "以下播报的是排名前十的百度今日热点事件 : \t\n"
        # 格式化遍历输出
        index = 1
        print('{}\t{:25}\t{:25}\t\n'.format('排名', '热点事件关键词', '搜索指数'))
        for i, j in zip(all_news_title_text, all_exponent_text):
            print('{}\t{:25}\t{:25}\t\n'.format(index, i, j))
            forcast_txt += '第{}条: \t{:25}。\t\n'.format(index, i)
            index += 1
        return forcast_txt

    # 获取实时热点事件
    @staticmethod
    def realTime_News():
        pass


    # 获取七日热点事件
    @staticmethod
    def week_News():
        pass
        
    # 运行程序
    @staticmethod
    def run():
        # 语音播报排名前十的百度今日热点事件, 最后将其文本数据推送到微信
        ttsToool.Voice_broadcast(forcast_txt= baiduTopNews.today_News())
    
""" 2021 01 03
排名    热点事件关键词                         搜索指数

1       区委书记被查:疫情期间看黄色视频         323613

2       巴啦啦小魔仙凌美琪扮演者去世            289574

3       中纪委曝光最懒政市委书记                205711

4       女教师补课期间出轨学生家长              173387

5       男子打车多付十万元:送你不要了           146626

6       商务部回应纽交所摘牌中国运营商          143266

7       王毅:中美关系来到新的十字路口           139921

8       31省新增确诊22例 其中本土8例            137671

9       沈阳1号通知:非必要岗位不上班            127789

10      男生用160个车厘子给女友做捧花           116167
"""
