# 使用requests库获取豆瓣影评

import requests

from fake_useragent import UserAgent      # fake_useragent模块 user-agent的获取 


ua = UserAgent()        # 实例化，实例化时需要联网但是网站不太稳定 


# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent':ua.random}

myurl = 'https://movie.douban.com/top250'

response = requests.get(myurl,headers=header)

print(response.text)
print(f'返回码是: {response.status_code}')
