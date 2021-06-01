from lxml import etree
import requests
# 百度热榜
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
}
url = "https://www.baidu.com/"
response = requests.get(url=url, headers=headers)
# 使用etree进行解析
data = etree.HTML(response.text)
# print(data)
# 可参考上表格进行对比，//div可理解为任意路径下的一个div标签，@class表示选取class属性，text()表示获取text文本
# name = data.xpath('//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]/text()')
ul = data.xpath('//*[@id="hotsearch-content-wrapper"]/li')

for li in ul:
    name = li.xpath(".//span[@class='title-content-title']/text()")
    print(name)
