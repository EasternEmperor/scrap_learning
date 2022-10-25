from urllib.request import urlopen
import re

# 如果网页有中文则需应用decode()
html = urlopen(
    "https://mofanpy.com/static/scraping/basic-structure.html"
).read().decode('utf-8')
print(html)

# 使用正则匹配获取内容
# 获取网页title
res = re.findall(r'<title>(.+?)</title>', html)
print('\nweb title: ', res[0])
# 获取中间段落<p>，如果有分行、制表符等空白字符，使用flags=re.DOTALL来获取全部内容
res = re.findall(r'<p>(.*?)</p>', html, flags=re.DOTALL)
print('\npage paragraph:', res[0])
# 获取网页中的所有链接
res = re.findall(r'href="(.*?)"', html)
print('\nlinks:', res)