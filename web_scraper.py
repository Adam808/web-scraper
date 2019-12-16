import urllib3
import re

http = urllib3.PoolManager()
r = http.request('GET', 'https://www.duolingo.com/')
page = r.data.decode('utf-8')

links = re.findall(r'a href="https?:\/\/(\S+)"', page)
print(links)

