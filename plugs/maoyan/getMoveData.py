'''
Author: GoogTech
Date: 2021-01-02 17:22:43
LastEditTime: 2021-01-03 12:14:25
LastEditors: Please set LastEditors
Description: 获取猫眼今日票房排行榜、电影榜单
'''
import requests
from bs4 import BeautifulSoup

# 请求头
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


# 获取网页 html 内容
def get_HTMLText(url):
    request = requests.get(url, headers=headers)
    request.encoding = request.apparent_encoding
    html_text = request.text
    return html_text


# 获取猫眼今日票房排行榜
def today_MoviceRanking():
    html = get_HTMLText("https://maoyan.com/")
    soup = BeautifulSoup(html, 'lxml')
    topOne_movice_name = soup.find(
        'span', class_='ranking-top-moive-name')  # 获取排名第 1 的电影名称
    all_ranking_no = soup.find_all('i', class_='ranking-index')
    all_movice_name = soup.find_all('span', class_='ranking-movie-name')
    all_ranking_no_text, all_movice_name_text = ['1'], [
        topOne_movice_name.get_text()
    ]
    # 获取排行榜中的剩余的 4 部电影的排名编号及名称
    count = 0
    for no in all_ranking_no:
        if count < 4:
            count += 1
            all_ranking_no_text.append(no.get_text())
    count = 0
    for name in all_movice_name:
        if count < 4:
            count += 1
            all_movice_name_text.append(name.get_text())
    return all_ranking_no_text, all_movice_name_text


#  格式化遍历输出今日票房排行榜
def showData_Today_MoviceRanking():
    all_movice_no_text, all_movice_name_text = today_MoviceRanking()
    print('{}\t{:5}\t\n'.format('序号', '电影名称'))
    for i, j in zip(all_movice_no_text, all_movice_name_text):
        print('{}\t{:5}\t\n'.format(i, j))


# 获取天猫正在热映的电影
# 注: 有时候返回空数据即用不了, 因为猫眼会验证身份
def movice_Ranking():
    datas = []
    html = get_HTMLText("https://maoyan.com/board")
    print(html)
    soup = BeautifulSoup(html, 'lxml')
    all_movice_no = soup.find_all('i', class_='board-index')  # 获取所有电影编号
    all_movice_name = soup.find_all('p', class_='name')  # 获取所有电影名称
    for movice_no, movice_name in zip(all_movice_no, all_movice_name):
        datas.append([movice_no.string, movice_name.a.string])
    return datas


# 格式化遍历输出正在热映的电影
def showData_Movice_Ranking():
    datas = movice_Ranking()
    print('{}\t{:5}\t\n'.format('序号', '电影名称'))
    for i, j in datas:
        print('{}\t\{:5}\t\n'.format(i, j))


# 主函数
if __name__ == "__main__":
    # showData_Today_MoviceRanking()
    showData_Movice_Ranking()
    
"""2020 01 02 : 获取猫眼今日票房排行榜
序号    电影名称        

1       送你一朵小红花  

2       温暖的抱抱      

3       拆弹专家2       

4       心灵奇旅        

5       晴雅集
"""
