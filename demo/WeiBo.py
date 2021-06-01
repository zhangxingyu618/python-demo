import requests
from lxml import etree
import re
import pprint

url = 'https://s.weibo.com/top/summary'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
res = requests.get(url, headers=headers)

a = etree.HTML(res.text)
tbody = a.xpath("//*[@id='pl_top_realtimehot']/table/tbody/tr")
for tr in tbody:
    title = tr.xpath(".//td[2]/a/text()")
    num = tr.xpath(".//td[1]/text()")
    print(num)
    print(title)