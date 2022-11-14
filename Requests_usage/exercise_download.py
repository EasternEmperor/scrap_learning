# 从http://www.ngchina.com.cn/下载图片
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import re

web = 'https://www.vcg.com/creative-image/meijing/'
html = urlopen(web).read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')
print(soup.title.string)

# 获取图片网址：soup.find_all
# 这里是嵌套的，先获取外层'a'
outer = soup.find_all('a', {'class' : 'imgWaper', 'target' : '_blank', 'rel' : 'opener'})
imgs = []
for a in outer:
    imgs.append(a.find_all('img'))
cnt = 1     # 用于计数
for img in imgs:
    # 图片网址
    imgurl = 'https:' + img[0]['data-src']
    print(img[0]['title'], ' : ', imgurl)
    # 读取图片
    r = requests.get(imgurl)
    os.makedirs('./img/', exist_ok=True)
    # 返回匹配的子串：re.research()返回pattern，再使用.group()可返回匹配的子串
    # date = re.search(r'\d{4}/\d\d/\d\d', img[0]['data-src']).group()
    # 奇数次图片用f.write()
    if cnt % 2 == 0:
        with open('./img/' + str(cnt) + img[0]['title'] + '.jpg', 'wb') as f:
            f.write(r.content)
    # 偶数次图片用chunk
    else:
        with open('./img/' + str(cnt) + img[0]['title'] + '.jpg', 'wb') as f:
            for chunk in r.iter_content(chunk_size=32):
                f.write(chunk)
    cnt += 1
    if cnt >= 20:
        break