'''
Author: GoogTech
Date: 2021-01-02 21:14:16
LastEditTime: 2021-01-03 12:11:46
Description: 获取今日日历及近期节日数据
'''
import requests
from bs4 import BeautifulSoup

# 请求链接及请求头
url = 'https://www.rili.com.cn/'
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


# 获取今日日历数据
def getTodayCal():
    html = get_HTMLText()
    soup = BeautifulSoup(html, 'lxml')
    date1 = soup.find('p')
    date2 = soup.find('span', id='today_24jie')
    today_yi = soup.find('ul', id='today_yi')
    today_ji = soup.find('ul', id='today_ji')
    daojishi = soup.find('div', class_='daojishi')
    print(date1.get_text())
    print(date2.get_text())
    print(today_yi.get_text())
    print(today_ji.get_text())
    print(daojishi.get_text())


# 主函数
if __name__ == "__main__":
    getTodayCal()
    
"""2020 01 02
今天是2021年01月02日
二十四节气：冬至 第十三天       

祈福嫁娶移徙纳采求嗣斋醮纳财竖柱


开市出行求财修造冠笄盖屋动土求医


小寒2021-01-05还有3天
腊八节2021-01-20还有18天        
大寒2021-01-20还有18天
立春2021-02-03还有32天
除夕2021-02-11还有40天
春节2021-02-12还有41天
"""
