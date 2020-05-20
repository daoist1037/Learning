import json,requests
json_data = requests.get('https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json').content.decode()

# 转换为字典
data  = json.loads(json_data)
date =[]
month=[]
week=[]
weekday=[]
close=[]
""" with open('out.txt','w') as f:
    for btc_dict in data:
        
        date = btc_dict['date']
        month = btc_dict['month']
        week = btc_dict['week']
        weekday = btc_dict['weekday']
        close = btc_dict['close']
        f.writelines("{} is month {} week {},{},the close price is {} RMB\n".format(date,month,week,weekday,close)) """

for btc_dict in data:
    date.append(btc_dict['date'])
    month.append(int(btc_dict['month']))
    week.append(int(btc_dict['week']))
    weekday.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
import pygal
import math

# 两个参数，前者让x轴数据标签顺时针旋转20°，后者告诉图形不用显示所有的x轴标签
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)  # ①
line_chart.title = '收盘价（¥）'
line_chart.x_labels = date
N = 20  
# x轴坐标每隔20天显示一次
line_chart.x_labels_major = date[::N]  # ②
line_chart.add('收盘价', close)
line_chart.render_to_file('收盘价折线图（¥）.svg')


line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价对数变换（¥）'
line_chart.x_labels = date
N = 20  
# x轴坐标每隔20天显示一次
line_chart.x_labels_major = date[::N]
close_log = [math.log10(_) for _ in close]  # ①
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('收盘价对数变换折线图（¥）.svg')
line_chart


# groupy  ！！！！！
from itertools import groupby
def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):  # 2
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])  # 3
    x_unique, y_mean = [*zip(*xy_map)]  # 4
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart


idx_month = date.index('2017-12-01')
line_chart_month = draw_line(
    month[:idx_month], close[:idx_month], '收盘价月日均值（¥）', '月日均值')
line_chart_month


idx_week = date.index('2017-12-11')
line_chart_week = draw_line(
    week[1:idx_week], close[1:idx_week], '收盘价周日均值（¥）', '周日均值')
line_chart_week


idx_week = date.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday',
      'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekday[1:idx_week]]
line_chart_weekday = draw_line(
    weekdays_int, close[1:idx_week], '收盘价星期均值（¥）', '星期均值')
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line_chart_weekday.render_to_file('收盘价星期均值（¥）.svg')
line_chart_weekday


with open('收盘价Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write(
        '<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in [
            '收盘价折线图（¥）.svg', '收盘价对数变换折线图（¥）.svg', '收盘价月日均值（¥）.svg',
            '收盘价周日均值（¥）.svg', '收盘价星期均值（¥）.svg'
    ]:
        html_file.write(
            '    <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))  # 1
    html_file.write('</body></html>')

