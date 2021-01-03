'''
Author: GoogTech
Date: 2021-01-02 23:10:07
LastEditTime: 2021-01-03 12:12:15
Description: 倒计时
Reference: https://blog.csdn.net/qq128619/article/details/103800142
'''
import time

# 获取现在的本地时间
localtime = time.localtime(time.time())
# 分段抽取现在的本地时间
tm_year = localtime[0]
tm_mon = localtime[1]
tm_day = localtime[2]
tm_hour = localtime[3]
tm_min = localtime[4]
tm_sec = localtime[5]
tm_y_day = localtime[7]


# 接收用户所输入的倒计时结束日期
def inputDate(input_years, input_month, input_day):
    # 检查用户输入的年份是否合理
    if input_years < localtime[0]:
        print("请输入大于或等于当前年份")
    # 检查用户输入的月份及日是否合理
    if (isRight(input_years, input_month, input_day)):
        # 查询的年份距离当前年份是同一年
        if input_years == tm_year:
            sameYear(input_years, input_month, input_day)
        # 查询的年份距离当前年份大于一整年
        elif input_years - tm_year == 1:
            nextYear(input_years, input_month, input_day)
        # 查询的年份距离当前年份大于一整年以上
        else:
            diffYear(input_years, input_month, input_day)
    else:
        print("你输入的日期数据不合理 !")


# 验证用户输入的月份及日数据是否复合要求
def isRight(input_years, input_month, input_day):
    # 判断月份天数
    if input_month in [1, 3, 5, 7, 8, 10, 12]:
        if input_day > 31 or input_day < 1:
            print("大月31天")
            return False
    elif input_month in [4, 6, 9, 11]:
        if input_day > 30 or input_day < 1:
            print("小月30天")
            return False
    # 判断是否为闰年
    elif input_month == 2:
        if input_years % 100 == 0 and input_years % 400 == 0:
            if input_day > 29 or input_day < 1:
                print("闰年2月29天")
                return False
        elif input_years % 4 == 0 and input_years % 100 != 0:
            if input_day > 29 or input_day < 1:
                print("闰年2月29天")
                return False
        elif input_years % 3200 == 0 and input_years % 172800 == 0:
            if input_day > 29 or input_day < 1:
                print("闰年2月29天")
                return False
        else:
            if input_day > 28 or input_day < 1:
                print("平年2月28天")
                return False
    else:
        print("请输入1至12月, 谢谢 !")
        return False
    return True


# 判断倒计时年份是否为闰年
def isLeap(input_years):
    leap_years = False
    if input_years % 100 == 0 and input_years % 400 == 0:
        leap_years = True
    elif input_years % 4 == 0 and input_years % 100 != 0:
        leap_years = True
    elif input_years % 3200 == 0 and input_years % 172800 == 0:
        leap_years = True
    return leap_years


# 计算输入的年里这一日是这一年的第多少天
def getDays(input_years, input_month, input_day):
    a = 0
    for i in range(1, input_month + 1):
        for j in range(1, 32):
            if input_month == i and input_day == j:
                a += 1
                print(
                    f"{input_years}年{input_month}月{input_day}日是{input_years}年第{a}天, "
                )
                break
            a += 1
            if i in [1, 3, 5, 7, 8, 10, 12]:
                if j >= 31:
                    break
            elif i in [4, 6, 9, 11]:
                if j >= 30:
                    break
            elif i == 2:
                if isLeap(input_years):
                    if j >= 29:
                        break
                else:
                    if j >= 28:
                        break
    return a


# 查询的年份距离当前年份是同一年
def sameYear(input_years, input_month, input_day):
    days = getDays(input_years, input_month, input_day)
    Var_Hour = 23 - time.localtime(time.time())[3]
    Var_Min = 59 - time.localtime(time.time())[4]
    Var_Sec = 60 - time.localtime(time.time())[5]
    print("\r距离%d年%d月%d日考研初试还剩%d天%02d小时%02d分钟%02d秒 !" %
          (input_years, input_month, input_day, days - tm_y_day - 1, Var_Hour,
           Var_Min, Var_Sec),
          end="")


# 查询的年份距离当前年份大于一整年
def nextYear(input_years, input_month, input_day):
    days = getDays(input_years, input_month, input_day)
    d = 365 - tm_y_day + days - 1 if isLeap(
        input_years) else 366 - tm_y_day + days - 1
    Var_Hour = 23 - time.localtime(time.time())[3]
    Var_Min = 59 - time.localtime(time.time())[4]
    Var_Sec = 60 - time.localtime(time.time())[5]
    print("\r距离%d年%d月%d日还剩%d天%02d小时%02d分钟%02d秒 !" %
          (input_years, input_month, input_day, d, Var_Hour, Var_Min, Var_Sec),
          end="")


# 查询的年份距离当前年份大于一整年以上
def diffYear(input_years, input_month, input_day):
    var_y = tm_year + 1
    y = -1
    days = getDays(input_years, input_month, input_day)
    # 判断输入的年份至今年中间有多少个闰年, 每个闰年加 1 天
    while var_y <= input_years:
        if var_y % 100 == 0 and var_y % 400 == 0:
            y += 1
            var_y += 1
        elif var_y % 4 == 0 and var_y % 100 != 0:
            y += 1
            var_y += 1
        elif var_y % 3200 == 0 and var_y % 172800 == 0:
            y += 1
            var_y += 1
        var_y += 1
    print(f"{input_years}至{tm_year + 1}年有{y + 1}个闰年, ")
    y = (input_years - tm_year - 1) * 365 + y
    d = 365 - tm_y_day + days + y - 1 if isLeap(
        input_years) else 366 - tm_y_day + days + y - 1
    Var_Hour = 23 - time.localtime(time.time())[3]
    Var_Min = 59 - time.localtime(time.time())[4]
    Var_Sec = 60 - time.localtime(time.time())[5]
    print("\r距离%d年%d月%d日还剩%d天%02d小时%02d分钟%02d秒 !" %
          (input_years, input_month, input_day, d, Var_Hour, Var_Min, Var_Sec),
          end="")


# 主函数
if __name__ == "__main__":
    inputDate(2021, 12, 26)  # 2022 考研初试时间
    
"""
2021/3~4: 开始准备考研, 搜集喜欢的学校, 并且开始准备专业课和英语.

2021/7~8: 暑期时间不要放过, 积极备考, 开始看政治.

2021/9~10: 考研冲刺阶段, 填报学校.

2021/12: 考研初试.

2022/3~4: 考研复试.

2022/5: 收到通知书.

> 大四上开始准备考研的初试, 也就是我们常常说的需要考英语、政治和专业课. 大四下也就是2022年初, 准备考研的复试 !
"""

"""
$ python countdown.py 
2021年12月26日是2021年第360天, 
距离2021年12月26日考研初试还剩356天11小时57分钟55秒 !
"""
