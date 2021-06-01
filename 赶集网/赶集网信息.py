import csv
import re
import time

import requests
from lxml import etree

num = 0


class GanJiWang():
    def __init__(self):
        self.url = f'http://jn.ganji.com/chuzu/pn{0}/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }

    # 爬去访问网页
    def html_get(self, url):
        res = requests.get(url, headers=self.headers)
        return res

    # 下载租房信息
    def download(self, house_process_items):
        global num
        path = r'C:/Users/dell/Desktop/ganjiwang.csv'
        with open(path, 'a+', encoding='utf-8', newline='') as f:
            f_csv = csv.writer(f)
            for house_item in house_process_items:
                if num == 0:
                    f_csv.writerow(
                        ['标题', '户型', '租房方式', '房屋大小', '房屋朝向', '楼层', '区县', '小区名称', '地址', '房租', '地铁', '房屋配置', '房屋描述'])
                    f_csv.writerow(
                        [house_item['title'], house_item['type'], house_item['mode'], house_item['size'],
                         house_item['direction'], house_item['floor'], house_item['quxian'], house_item['community'],
                         house_item['address'], house_item['money'], house_item['subway'], house_item['peizhi'],
                         house_item['describe']])
                else:
                    f_csv.writerow(
                        [house_item['title'], house_item['type'], house_item['mode'], house_item['size'],
                         house_item['direction'], house_item['floor'], house_item['quxian'], house_item['community'],
                         house_item['address'], house_item['money'], house_item['subway'], house_item['peizhi'],
                         house_item['describe']])
                num += 1

    # 处理租房信息
    def get_process(self, house_items, i):
        l = 1
        house_process_items = []
        process_num = 0
        for house_item in house_items:
            house_process_item = {}
            for j in house_item.values():
                if len(j) < 1:
                    l = len(j)
            if l >= 1:
                house_process_item['title'] = str(house_item['title'][0])
                house_process_item['money'] = str(house_item['money'][0])
                house_process_item['type'] = str(house_item['type'][0])
                rent_mode_size = str(house_item['rent_mode_size'][0])
                house_process_item['mode'] = rent_mode_size.replace('\xa0\xa0', ',').split(',')[0]
                size = rent_mode_size.replace('\xa0\xa0', ',').split(',')[1]
                house_process_item['size'] = str(re.compile('(\d+)').findall(size)[0])
                house_process_item['direction'] = str(house_item['direction'][0])
                house_process_item['floor'] = str(house_item['floor'][0])
                house_process_item['community'] = str(house_item['community'][0])
                subway = str(house_item['subway'][0])
                if subway == '暂无信息':
                    house_process_item['subway'] = '无'
                else:
                    house_process_item['subway'] = '有'
                address = str(house_item['address'][0])
                house_process_item['address'] = address.replace(r'\n', '').strip()
                house_process_item['quxian'] = house_process_item['address'][0:2]
                house_describe = str(house_item['describe'][0])
                house_process_item['describe'] = house_describe.replace(r'\n', '').strip()
                house_process_item['peizhi'] = str(house_item['peizhi'][0:])
                print(house_process_item)
                print()
                house_process_items.append(house_process_item)
                process_num += 1
        # 对数据信息进行汇报
        # print('去除带有控制')
        print('                                    ')
        print(f'第{i}页采集的数据处理后：{len(house_items)}条，去除{len(house_items) - process_num}条带有空值的信息')
        print('                                    ')
        return house_process_items

    # 爬取租房信息
    def get_house(self, i):
        url = self.url.format(i)  # 拼接租房信息的网址
        #         print(url)
        res = self.html_get(url)
        # print(res.text)
        html = etree.HTML(res.text)
        house_items = []
        res_num, house_items_num = 0, 0
        href_list = html.xpath('//div[@class="f-list js-tips-list"]/div[@class="f-list-item ershoufang-list"]')
        for j in href_list:
            href_url = j.xpath('./dl/dt//a/@href')
            print(href_url)
            # 每5次进行短暂休眠
            if res_num == 5:
                time.sleep(3)
                res_num = 0
            res_num += 1
            house_res = ''
            if len(href_url) != 0:  # 判断爬取的的代码是否为空值
                pass
            else:
                continue
            if href_url[0][0] == 'h':  # 拼接网址代码
                house_res = self.html_get(href_url[0])
            else:
                house_res = self.html_get('http:' + href_url[0])
            # print(house_res.text)
            html_house = etree.HTML(house_res.text)
            house_item = {}

            # 获取租房标题
            house_item['title'] = html_house.xpath('//div[@class="card-top"]/p/i/text()')
            # 获取房租价钱
            house_item['money'] = html_house.xpath('//div[@class="card-top"]/div[@class="er-card-pay"]/div/span/text()')
            # 获取租房类型
            house_item['type'] = html_house.xpath(
                '//div[@class="card-top"]/ul[@class="er-list f-clear"]/li[1]/span[2]/text()')
            # http://jn.ganji.com/hezu/44500056595992x.shtml
            # 获取房屋方式和大小
            house_item['rent_mode_size'] = html_house.xpath(
                '//div[@class="card-top"]/ul[@class="er-list f-clear"]/li[2]/span[2]/text()')
            # 获取房屋朝向
            house_item['direction'] = html_house.xpath(
                '//div[@class="card-top"]/ul[@class="er-list f-clear"]/li[3]/span[2]/text()')
            # 获取房屋楼层
            house_item['floor'] = html_house.xpath(
                '//div[@class="card-top"]/ul[@class="er-list f-clear"]/li[4]/span[2]/text()')
            # 获取房屋所在小区
            house_item['community'] = html_house.xpath(
                '//div[@class="card-top"]/ul[@class="er-list-two f-clear"]/li[1]/span[@class="content"]/a/span/text()')
            # 获取房屋附近地铁
            house_item['subway'] = html_house.xpath(
                '//div[@class="card-top"]/ul[@class="er-list-two f-clear"]/li[2]/div[@class="subway-wrap"]/span[@class="content"]/text()')
            # 获取房屋地址
            house_item['address'] = html_house.xpath(
                '//div[@class="card-top"]/ul[@class="er-list-two f-clear"]/li[3]/span[@class="content"]/text() ')
            # 获取房屋配置
            peizhi = html_house.xpath(
                '//div[@id="js-house-peizhi"]/ul/li[@class="item"]/p[@class="text"]/text()')
            if peizhi != []:
                house_item['peizhi'] = peizhi
            else:
                house_item['peizhi'] = ['无']
            # 获取房屋描述
            describe = html_house.xpath('//div[@id="js-house-describe"]/div/div/text()')
            if describe != []:
                house_item['describe'] = describe
            else:
                house_item['describe'] = ['无']
            house_items_num += 1
            print('\r爬取进度：{:.2f}%'.format(house_items_num * 100 / len(href_list)), end='')

            house_items.append(house_item)
            time.sleep(1)
        print('                                    ')
        print(f'爬取第{i}页信息共爬取：{house_items_num}条，去除{len(href_list) - house_items_num}条信息')
        print('                                    ')
        return house_items


def main():
    ganji = GanJiWang()
    for i in range(1, 71):
        print('                                    ')
        print(f'-------开始第{i}页租房信息爬取--------')
        print('                                    ')
        house_items = ganji.get_house(i)
        house_process_items = ganji.get_process(house_items, i)
        ganji.download(house_process_items)


if __name__ == '__main__':
    main()
