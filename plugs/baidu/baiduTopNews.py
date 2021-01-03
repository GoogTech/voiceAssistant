'''
Author: GoogTech
Date: 2021-01-02 11:49:16
LastEditTime: 2021-01-03 12:11:11
Description: 获取百度实时、今日、七日热点事件排行榜数据
Reference: https://www.cnblogs.com/-stewart/p/12521202.html
'''
import requests
from bs4 import BeautifulSoup

# 请求链接及请求头
url = 'http://top.baidu.com/buzz/shijian.html'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


# 获取网页 html 内容
def get_HTMLText():
    urls = requests.get(url, headers=headers)
    urls.encoding = urls.apparent_encoding
    html_text = urls.text
    return html_text


# 获取今日热点事件
def today_News():
    # 使用 lxml HTML 解析器: 速度快、文档容错能力强
    soup = BeautifulSoup(get_HTMLText(), 'lxml')
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
    # 格式化遍历输出
    index = 1
    print('{}\t{:25}\t\n'.format('排名', '热点事件关键词', '搜索指数'))
    for i, j in zip(all_news_title_text, all_exponent_text):
        print('{}\t{:25}\t\n'.format(index, i, j))
        index += 1


# 获取实时热点事件
def realTime_News():
    pass


# 获取七日热点事件
def week_News():
    pass


# 主函数
if __name__ == "__main__":
    today_News()
""" 2021 01 02
排名    热点事件关键词

1       习近平发表2021新年贺词

2       华为全面下架腾讯游戏

3       天安门广场新年首次升旗仪式

4       上海现首例英国变异病毒感染病例

5       婚姻法继承法合同法等废止

6       谢娜宣布怀二胎

7       2021年第一缕曙光

8       北京一确诊病例曾到派出所报警

9       男子跨年晚会中奖半头猪

10      上海通报发现英国变异病毒病例
"""
