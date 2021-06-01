import requests
from lxml import etree
import scrapy

url = "https://ssr1.scrape.center/page/1"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3765.400 QQBrowser/10.6.4143.400'
}
res = requests.get(url, headers = header)

data = etree.HTML(res.text)
# print(data)
item = {}
# move = set([item])
movies = data.xpath('//div[@class="el-col el-col-18 el-col-offset-3"]/div')
for div in movies:
    item['title'] = div.xpath('.//h2[@class="m-b-sm"]/text()')
    item['fraction'] = div.xpath('.//p[@class="score m-t-md m-b-n-sm"]/text()').strip()
    item['country'] = div.xpath('.//div[@class="m-v-sm info"]/span[1]/text()')
    item['time'] = div.xpath('.//div[@class="m-v-sm info"]/span[3]/text()')
    item['date'] = div.xpath('.//div[@class="m-v-sm info"][2]/span/text()')
    print(item)
    # title = div.xpath('.//h2[@class="m-b-sm"]/text()')
    # print(title)
# title = data.xpath('.//h2[@class="m-b-sm"]/text()')
# print(title)

