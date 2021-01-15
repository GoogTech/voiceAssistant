'''
Author: GoogTech
Date: 2021-01-03 16:26:24
LastEditTime: 2021-01-15 15:06:41
Description: 测试功能插件
'''

import sys
# 打印所有 python 解释器可以搜索到的所有路径
sys.path.append('../')
print(sys.path)
# 导入自定义包
from plugins.baidu.baiduTopNews import *
from plugins.countdown.countdown import *
from plugins.douban.getMoveData import *
from plugins.weibo.weiboHotTopic import *
from plugins.maoyan.getMoveDataMY import *
from plugins.system.sysinfo import *
from plugins.weather.weatherInfo import *

# 测试运行播报百度今日热点事件程序(ok)
# baiduTopNews.run()

# 测试运行播报距离 2021 年考研初试的倒计时的程序(ok)
# countdown.run()

# 测试运行播报豆瓣近一周电影口碑榜的程序(ok)
# moviceData.run()

# 测试运行播报猫眼今日票房排行榜的程序(ok)
# moviceDataMY.run_today_movice_ranking()

# 测试运行播报天猫正在热映的电影的程序(ok)
# moviceDataMY.run_movice_ranking()

# 测试运行播报微博热门话题数据的程序(ok)
# weiboHotTopic.run()

# 测试运行播报系统信息数据的程序(仅能在 linux 环境中测试: ok)
# sysinfo.run()

# 测试运行播报今日天气预报的程序(ok)
# weatherInfo.run_today_weather()

# 测试运行播报明日天气预报的程序(ok)
# weatherInfo.run_tomorrow_weather()

# 测试运行播报今日日历情况的程序
# ...程序待完善...
