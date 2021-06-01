import requests
from lxml import etree

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
}
url = "https://hotels.ctrip.com/hotels/list?countryId=1&city=144"
response = requests.get(url, headers = headers)

data = etree.HTML(response.text)
# print(data)
a = data.xpath('//*[@id="ibu_hotel_container"]/div/section/div[2]/ul/li[3]/div/div/div/div[1]/div[2]/div[2]/p/span[1]/span/text()')
print(a)
# ul = data.xpath('//*[@id="ibu_hotel_container"]/div/section/div[2]/ul/li')
# for li in ul :
#     a = li.xpath('.//div/div/div/div[1]/div[2]/div[1]/div/span[1]/text()')
#     print(a)
