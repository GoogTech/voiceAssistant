'''
Author: GoogTech
Date: 2021-01-03 14:30:22
LastEditTime: 2021-01-03 20:21:24
Description: TTS即将文本转换为语音并播放, 最后将文本数据推送到到微信
'''

import os
import requests
import playsound
import subprocess
from aip import AipSpeech

import sys
# 打印所有 python 解释器可以搜索到的所有路径
sys.path.append('../')
# print(sys.path)
# 导入自定义包
from config.apiConfig import *


class ttsToool(object):
    # Voice prompt by Baidu API
    @staticmethod
    def Voice_broadcast(forcast_txt):
        sys_info = forcast_txt
        # 将树莓派系统信息推送到微信
        if ttsToool.SendToWeChat(forcast_txt):
            sys_info = sys_info + \
            '最后, 以上播报信息已通过「Server 酱」推送到你的微信~'
        else:
            sys_info = sys_info + \
            '注意: 以上播报信息无法通过「Server 酱」推送到你的微信!'
        # 百度语音合成, 参数配置详见: https://ai.baidu.com/ai-doc/SPEECH/Qk38y8lrl
        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        result = client.synthesis(sys_info, 'zh', 1, {'vol': 5, 'per': 0})
        if not isinstance(result, dict):
            with open(BAIDU_TTS_MP3, 'wb') as f:
                f.write(result)
            f.close()
        # Linux OS 播放语音
        subprocess.getoutput('mplayer .tts.mp3')
        # Windows OS 播放语音
        # playsound.playsound(BAIDU_TTS_MP3)
        # os.remove(BAIDU_TTS_MP3)

    # Return system information to WeChat By ServerChan
    @staticmethod
    def SendToWeChat(weather_forecast_txt):
        # text 为推送的 title, desp 为推送的 description
        title = "树莓派发来新信息啦~"
        content = weather_forecast_txt
        data = {"text": title, "desp": content}
        # 发送( 同样内容的消息一分钟只能发送一次, 服务器只保留一周的消息记录 )
        return True if requests.post(SERVER_API,
                                     data=data).status_code == 200 else False


# 测试
# ttsTool.Voice_broadcast(forcast_txt="这是测试数据")
