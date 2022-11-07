from bs4 import BeautifulSoup
from urllib.request import urlopen

# 网页有中文需要使用decode()
html = urlopen("https://mofanpy.com/static/scraping/basic-structure.html").read().decode('utf-8')
print(html)

# 获取标题和段落
soup = BeautifulSoup(html, features = 'lxml')
print(soup.h1)      # 输出html中的h1标题
print('\n', soup.p) # 输出html中的段落

# 获取<a>中的内容：find_all()
# 1. 查找标签：soup.find_all('标签'), 如'a'
# 2. 查找文本：soup.find_all(text = 'text')
# 3. 根据id查找：soup.find_all(id = 'tag_id')
# 4. 指定属性查找对应标签：soup.find_all('标签', { 'id' : 'tag_id', 'class' : 'tag_class'})
links = soup.find_all('a')
# 获取<a>中的所有链接href
hrefs = [l['href'] for l in links]
print('\n', hrefs)