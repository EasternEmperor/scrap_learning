from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

base_url = 'https://baike.baidu.com'
links = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

# 爬20个网页
for i in range(20):
    url = base_url + links[-1]      # 基本域名+刚爬到的网址
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')

    # 输出当前网址标题和网址
    print(soup.h1, '\turl: ' + url)

    # 爬取其中网址
    get_links = soup.find_all('a', {'target' : '_blank', 'href' : re.compile(r'/item/%(.{2})+')})

    # 如果该页面中爬到网址，则挑选其中一个加入links中待遍历栈中
    # random.sample(list, n)，可以从给定的list中随机挑选n个元素作为新的list
    if len(get_links) != 0:
        links.append(random.sample(get_links, 1)[0]['href'])
    # 如果该页面未爬到网址，则弹出当前网址，继续爬下一个
    else:
        links.pop()