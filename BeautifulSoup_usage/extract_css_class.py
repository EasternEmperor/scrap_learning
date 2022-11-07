from bs4 import BeautifulSoup
from urllib.request import urlopen

# 读取html
html = urlopen('https://mofanpy.com/static/scraping/list.html').read().decode('utf-8')
print(html)

# css中有class，在<ul>标签中可以使用相应class，在<ul>下也可使用<li>标签来继续增加class元素
soup = BeautifulSoup(html, features='lxml')
months = soup.find_all('li', {'class' : 'month'})
print('\n', months)
# 获取标签内的text：get_text()
for m in months:
    print(m.get_text())

# 在标签下提取其中嵌套的class，如下提取其中的日期
# <ul class="jan"> <li>一月一号</li> <li>一月二号</li> <li>一月三号</li> </ul>
# soup.find()：返回第一个匹配的对象
Jan = soup.find('ul', {'class' : 'jan'})
days = Jan.find_all('li')
print('\n', days)
for d in days:
    print(d.get_text())