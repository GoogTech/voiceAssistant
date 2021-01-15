# Voice Assistant Of RasPi
🔊 It's a simple voice assistant which base on `RasPi4B`、`Snowboy` and `Baidu ASR`, Please refer to [`This airticle`](https://www.passerma.com/article/54) if you want to know more detail info about it.

> This Project Forked From : https://github.com/passerma/voiceAssistant Thanks A Lot bro ~


## OS
* `Raspberry Pi 4B 4GB`


## Env
* `Python 3.7`
* `apscheduler`
* `python3-pyaudio`
* `swig`
* `libatlas-base-dev`
* `baidu-aip`
* `Baidu AIP SDK( aip-python-sdk-2.2.15 )`


## How To Run
1. the first step : install the dependencies of Wake-on-voice
```shell
sudo apt-get install python3-pyaudio
```

```shell
sudo apt-get install swig
```

```shell
sudo apt-get install libatlas-base-dev
```

> You need to change the fifth line of code : `from * import snowboydetect` to `import snowboydetect` in the `snowboy/examples/Python3/snowboydecoder.py` after you installed the dependencies of Wake-on-voice successfully.


2. the second step : install the snowboy project
```shell
git clone https://github.com/Kitt-AI/snowboy.git
```

```shell
cd snowboy/swig/Python3 && make
```

let's execute the following command to test it whether installed successfully.
```shell
cd snowboy/examples/Python3
python3.7 demo.py resources/models/snowboy.umdl
```

Then speak the world of Wake-on-voice : `snowboy`，Verify installed successfully if you hear this sound is similar to : `D~`


3. the third step : git clone this project
```shell
git clone https://github.com/raspberry-pi-org/voiceAssistant.git
```

4. the fourth step : install some dependencies of this project needed
```shell
$ pip3 install apscheduler
```

```shell
$ cd aip-python-sdk-2.2.15
```

```shell
$ pip3 install baidu-aip
```

```shell
$ python3.7 setup.py install
```

5. The fifth step : open the `config/apiConfig.py` file and add your `Baidu API` and `ServerChan` configuration information into it.

6. The last step : run it and enjoy it bro
```shell
# the word of Wake-on-voice is : snowboy
$ python3.7 voiceAssistant.py
```

### Problems
If the program throw a error info such as `[Errno -9985] Device unavailable ...`，Please fix it by the following command !
```shell
# install the pulseaudio
sudo apt-get install pulseaudio
# start it
pulseaudio --start
```


## Speech Sound Plugins
* [x] Play Music  
* [x] System Data  
* [x] Weather Data
* [x] Hot Top Of Weibo.com
* [x] Hot Event Of Baidu.com
* [x] Movice Data Of Douban.com
* [x] Movice Data Of Maoyan.com
* [x] Universal Counting Leader

> Thanks for your contribution if you want to add some funny or useful plugins into it.


## Thanks
* [Snowboy](https://github.com/Kitt-AI)
* [Baidu ASR](https://cloud.baidu.com/product/speech/)
