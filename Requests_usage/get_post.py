'''
post:
    - 账号登录
    - 搜索内容
    - 上传图片
    - 上传文件
    - 往服务器传数据 等
get:
    - 正常打开网页
    - 不往服务器传数据
post是发送，比较主动，用户可以控制服务器返回的内容
get是获取，用户不用发送信息，服务器也不会返回个性化页面
'''

import requests
import webbrowser

# get请求
param = {'q' : '莫烦python'}     # q是要搜索的信息
r = requests.get('https://cn.bing.com/search', params = param)
print(r.url)
webbrowser.open(r.url)

# post请求
# https://pythonscraping.com/pages/files/form.html
# 其中需要发送firstname和lastname，然后请求页面为https://pythonscraping.com/pages/files/processing.php
data = {'firstname' : 'qilong', 'lastname' : 'zhong'}
# 发送数据用data参数
r = requests.post('https://pythonscraping.com/pages/files/processing.php', data = data)
print(r.text)

# post上传文件
# https://pythonscraping.com/files/form2.html
# 上传一张图片，请求页面为https://pythonscraping.com/pages/files/processing2.php
file = {'uploadFile' : open('D:\\tencent\LabProjects\drone_dataset_brighton_beach-master\\brighton_beach.jpg', 'rb')}
# 上传文件用files参数
r = requests.post('https://pythonscraping.com/pages/files/processing2.php', files = file)
print(r.text)

# 使用post登录获取cookies，使用其get用户登录后的网页
# post登录
data = {'username' : 'EasternE', 'password' : 'password'}
r = requests.post('https://pythonscraping.com/pages/cookies/welcome.php', data = data)
print(type(r.cookies))
print(r.cookies.get_dict())
# get获取用户登录后的界面，用cookies参数
r = requests.get('https://pythonscraping.com/pages/cookies/profile.php', cookies = r.cookies)
print(r.text)
webbrowser.open(r.url)