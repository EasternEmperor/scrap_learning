import requests

# 使用session来登录网页：requests.session()
session = requests.session()
data = {'username' : 'EasternE', 'password' : 'password'}
r = session.post('https://pythonscraping.com/pages/cookies/welcome.php', data = data)
print(r.cookies.get_dict())

r = session.get('https://pythonscraping.com/pages/cookies/profile.php')
print(r.text)