import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

# 读取网页
html = urlopen('https://mofanpy.com/static/scraping/table.html').read().decode('utf-8')

# 提取图片链接
soup = BeautifulSoup(html, features='lxml')
imgs = soup.find_all('img', {'src' : re.compile(r'.*\.jpg')})
for img in imgs:
    print(img['src'])

print()
# 提取课程链接
courses = soup.find_all('a', {'href' : re.compile('/tutorials/*')})
for course in courses:
    print(course['href'])