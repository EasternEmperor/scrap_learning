import os
from urllib.request import urlretrieve
import webbrowser
import requests

# 创建新文件夹：os.makedirs(), exist_ok：False时若已存在同名文件夹则报错；True则不触发报错
os.makedirs('./img/', exist_ok=True)

imgurl = 'https://mofanpy.com/static/img/description/learning_step_flowchart.png'
webbrowser.open(imgurl)

# 使用urlretrieve下载图片
urlretrieve(imgurl, './img/img1.jpg')

# 使用request下载
# 写入文件的方式：f.write(r.content)
r = requests.get(imgurl)
with open('./img/img2.png', 'wb') as f:
    f.write(r.content)

# 较大文件也可以采取一段一段下载的方式
# 使用遍历方式：r.iter_content(chunk_size = 32)
with open('./img/img3.jpg', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)