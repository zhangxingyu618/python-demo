import pandas as pd
import requests
import json
import csv
from sklearn.linear_model import LinearRegression   # 线性回归
from sklearn.preprocessing import PolynomialFeatures    # 多项式特征构造
import matplotlib.pyplot as plt
import numpy as np
import datetime
import re
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.commons.utils import JsCode
import webbrowser


# 爬虫和网址
# https://news.qq.com/zt2020/page/feiyan.htm#/country?ct=United%20States
# 爬取数据得到的json格式
def get_json():
    url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country=%E7%BE%8E%E5%9B%BD&'
    usa_json = requests.get(url).json()
    print(usa_json)

    usa_json = usa_json['data']
    print(usa_json)
    with open('usa.json', 'w') as f:
        json.dump(usa_json, f)


# 对json格式进行转换为csv格式文件
def get_csv():
    # 读、创建文件
    json_fp = open("usa.json", "r")
    csv_fp = open("usa.csv", "w")
    # 提出表头和表的内容
    data_list = json.load(json_fp)
    sheet_title = data_list[0].keys()
    sheet_data = []
    for data in data_list:
        sheet_data.append(data.values())
        # print(sheet_data)
    # csv
    writer = csv.writer(csv_fp)
    # 写入表头
    writer.writerow(sheet_title)
    # 写入内容
    writer.writerows(sheet_data)
    json_fp.close()
    csv_fp.close()

# 对数据进行处理
def data_treating():
    np.set_printoptions(suppress=True)
    data = pd.read_csv("USA.csv", )
    # print(data)
    global index, date, confirm_add, confirm, heal, dead, now
    # 索引
    index = data.index + 1
    # print(index)
    # 时间
    date = np.array(data['date'])
    # 新增确诊
    confirm_add = np.array(data['confirm_add'])
    # 累计确诊
    confirm = np.array(data['confirm'])
    # 累计治愈
    heal = np.array(data['heal'])
    # 累计死亡
    dead = np.array(data['dead'])
    # 现存确诊
    now = confirm - heal - dead
    # print(now)

    # 绘制现在美国的现存确诊人数图表
    plt.scatter(index, now)
    plt.title("USA existing confirmed")
    plt.show()

    # 一元一次线性回归
    # liner_reg = LinearRegression()
    # x_data = index[:, np.newaxis]
    # y_data = now[:, np.newaxis]
    # liner_reg.fit(x_data, y_data)
    #
    # plt.scatter(x_data, y_data)
    # plt.plot(x_data, liner_reg.predict(x_data), 'r')
    # plt.show()

# 预测 绘图
def prediction(n):
    # print(index)
    # print(confirm)
    # print(heal)
    # print(dead)
    # print(now)
    # print(date)
    global prediction_now, prediction_data

    # 先绘制目前的现存的感染者图表
    x_data_index = index[:, np.newaxis]
    y_data_now = now[:, np.newaxis]
    # print(y_data_now)

    plt.title("USA existing and projected confirmed")
    plt.plot(x_data_index, y_data_now, "r")

    # 累计确诊的预测
    liner_reg = LinearRegression()
    x_data_index = index[:, np.newaxis]
    y_data_confirm = confirm[:, np.newaxis]
    liner_reg.fit(x_data_index, y_data_confirm)
    # 多项式次数
    poly = PolynomialFeatures(6)
    x_data_poly = poly.fit_transform(x_data_index)
    # print(x_data_poly)
    liner_reg = LinearRegression()
    liner_reg.fit(x_data_poly, y_data_confirm)
    # 预测的累计确诊人数
    prediction_data = np.arange(1, n)[:, np.newaxis]
    prediction_confirm = liner_reg.predict(poly.fit_transform(prediction_data))
    # print(prediction_confirm.tolist())
    # print(confirm)

    # 预测累计治愈人数
    y_data_heal = heal[:, np.newaxis]
    liner_reg.fit(x_data_index, y_data_heal)
    liner_reg = LinearRegression()
    liner_reg.fit(x_data_poly, y_data_heal)
    prediction_data = np.arange(1, n)[:, np.newaxis]
    prediction_heal = liner_reg.predict(poly.fit_transform(prediction_data))
    # prediction_heal = liner_reg.predict([[i ** 0, i ** 1, i ** 2, i ** 3] for i in np.arange(1, 500)])
    # print(prediction_heal)

    # 预测累计死亡人数
    y_data_dead = dead[:, np.newaxis]
    liner_reg.fit(x_data_index, y_data_dead)
    liner_reg = LinearRegression()
    liner_reg.fit(x_data_poly, y_data_dead)
    prediction_data = np.arange(1, n)[:, np.newaxis]
    prediction_dead = liner_reg.predict(poly.fit_transform(prediction_data))
    # prediction_dead = liner_reg.predict([[i ** 0, i ** 1, i ** 2, i ** 3] for i in np.arange(1, 500)])
    # print(prediction_dead)

    # 预测的 现有确诊 = 预测累计确诊 - 预测累计治愈 - 预测累计死亡
    # global prediction_now, prediction_data
    prediction_now = prediction_confirm - prediction_heal - prediction_dead
    prediction_now = np.ceil(prediction_now)
    plt.plot(prediction_data, prediction_now)
    # print(prediction_data)
    plt.show()


def get_time(n):

    the_date = datetime.datetime(2020, 1, 28)
    result_date = the_date + datetime.timedelta(days=n)
    d = result_date.strftime('%Y-%m-%d')
    # print(d)
    starttime = '20200128'
    endtime = re.sub('-', '', d)
    # print(endtime)
    startdate = datetime.datetime(int(starttime[0:4]), int(starttime[4:6]), int(starttime[6:8]))

    delta = datetime.timedelta(days=1)
    n = 0
    global date_list
    date_list = []
    while 1:
        if starttime <= endtime:
            days = (startdate + delta * n).strftime('%Y%m%d')
            n = n + 1
            date_list.append(days)
            if days == endtime:
                break
    # print(date_list)

def pyecharts():

    # print(date_list)
    js_formatter = """function (params) {
            console.log(params);
            return '美国疫情  ' + params.value + (params.seriesData.length ? '日：' + params.seriesData[0].data[1]+'人' : '');
        }"""

    (
        Line(init_opts=opts.InitOpts(width="1400px", height="700px"))
            .add_xaxis(
            xaxis_data=date_list
        )
            .extend_axis(
            xaxis_data=date_list,
            xaxis=opts.AxisOpts(
                type_="category",
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                axisline_opts=opts.AxisLineOpts(
                    is_on_zero=False, linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                ),
                axispointer_opts=opts.AxisPointerOpts(
                    is_show=True, label=opts.LabelOpts(formatter=JsCode(js_formatter))
                ),
            ),
        )
            .add_yaxis(
            series_name="美国真实确诊人数",
            is_smooth=True,
            symbol="emptyCircle",
            is_symbol_show=False,
            xaxis_index=1,
            color="#6e9ef1",
            y_axis=now.tolist(),

            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=2),
        )
            .add_yaxis(
            series_name="机器学习预测确诊人数",
            is_smooth=True,
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#d14a61",
            y_axis=prediction_now.tolist(),
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=2),
        )
            .set_global_opts(
            legend_opts=opts.LegendOpts(),
            tooltip_opts=opts.TooltipOpts(trigger="none", axis_pointer_type="cross"),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                axisline_opts=opts.AxisLineOpts(
                    is_on_zero=False, linestyle_opts=opts.LineStyleOpts(color="#6e9ef1")
                ),
                axispointer_opts=opts.AxisPointerOpts(
                    is_show=True, label=opts.LabelOpts(formatter=JsCode(js_formatter))
                ),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                ),
            ),
        )
            .render("美国疫情预测.html")
    )
    webbrowser.open("美国疫情预测.html")


if __name__ == "__main__":
    num = 350
    # get_json()
    # get_csv()
    data_treating()
    prediction(num)
    get_time(num)
    pyecharts()
