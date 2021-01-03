'''
Author: GoogTech
Date: 2021-01-02 17:16:44
LastEditTime: 2021-01-03 12:13:21
Description: 获取豆瓣近一周口碑榜、北美票房榜
'''
import requests
from bs4 import BeautifulSoup

# 请求链接及请求头
url = "https://movie.douban.com/chart"
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


# 获取网页 html 内容
def get_HTMLText():
    request = requests.get(url, headers=headers)
    request.encoding = request.apparent_encoding
    html_text = request.text
    return html_text


# 获取豆瓣近一周口碑榜
def week_MoveRanking():
    datas = []
    html = get_HTMLText()
    soup = BeautifulSoup(html, 'lxml')
    updatedTime = soup.find('div', class_='movie_top').h2.span.string  # 更新时间
    moviceNos = soup.find_all('div', class_='no')
    moviceNames = soup.find_all('div', class_='name')
    for moviceNo, moviceName in zip(moviceNos, moviceNames):
        datas.append([
            moviceNo.string,  # 电影排行榜序号
            moviceName.a.string.strip()  # 电影名称
        ])
    return updatedTime, datas


# 输出微博热门话题数据
def showData(row):
    updatedTime, datas = week_MoveRanking()
    print('更新时间: ', updatedTime)
    print('{}\t{:5}\t\n'.format('序号', '电影名称'))
    count = 1
    for i, j in datas:
        if count <= row:
            print('{}\t{:5}\t\n'.format(i, j))
            count += 1


# 获取北美票房榜数据
def northAmerica_MoveTop():
    pass


# 主函数
if __name__ == "__main__":
    # 获取前 10 条热点话题, 全部共计 10 条数据
    showData(10)
    
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
