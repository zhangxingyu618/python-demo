from lxml import etree
import requests

url = "https://www.inspur.com"
resp = requests.get(url)
# print(resp)
# decode,把宁蕉数据解码成宁符数据，encode()方法和它相反
html = resp.content.decode()
# print(html)
element = etree.HTML(html)
lst = element.xpath("//div[@class= 'in_zdcp']/table")
with open("inspur.txt", "w", encoding="utf-8") as f:
    for table in lst:
        title = table.xpath("./tbody/tr[2]/td/a/text()")[0]
        content = table.xpath("./tbody/tr[3]/td/text()")[0]
        f1 = title + "----" + content
        f.write(f1)
        f.write("\n")
    f.close()
