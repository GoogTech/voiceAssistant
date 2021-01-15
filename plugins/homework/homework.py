'''
Author: GoogTech
Date: 2021-01-02 20:47:18
LastEditTime: 2021-01-02 21:04:37
Description: 作业提示
'''
import requests, time

# 链接
url = ""


# 登录
def login():
    s = requests.session()
    data = [
        ('number', ''),
        ('password', ''),
    ]
    res = s.post(url, data)
    print(res.status_code)  # 200 ok !


# 爬取作业数据
def getData():
    pass


# 格式化输出
def showData():
    pass


# 主函数
if __name__ == "__main__":
    login()
