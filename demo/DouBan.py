import requests
from lxml import etree
import re
import pprint

url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
res = requests.get(url, headers=headers)

a = etree.HTML(res.text)
ol = a.xpath('//*[@id="content"]/div/div[1]/ol/li')
move = {}
for li in ol:
    name = str(li.xpath(".//div/div[2]/div[1]/a/span[1]/text()"))
    actor = li.xpath(".//div/div[2]/div[2]/p[1]/text()")
    actor = str(actor[0]).strip()

    grade = str(li.xpath(".//div/div[2]/div[2]/div/span[2]/text()"))
    mun = str(li.xpath(".//div/div[2]/div[2]/div/span[4]/text()"))
    comment = str(li.xpath(".//div/div[2]/div[2]/p[2]/span/text()"))
    image = li.xpath(".//div/div[1]/a/img/@src")
    print(name)
    print(actor)
    print(grade+"分，"+mun)
    print(mun)
    print(comment)
    print(image)
