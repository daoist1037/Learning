import csv
from datetime import datetime

with open('./sitka_weather_2014.csv') as f:
    reader = csv.reader(f)
    # next 函数 会读取csv的下一行，首次运用会返回第一行
    """ reader_row = next(reader)
    # print(reader_row)
    for index,column_header in enumerate(reader_row):
        print(index,column_header)
    reader_row = next(reader) 
    for index,column_header in enumerate(reader_row):
        print(index,column_header)
    print('\n') """

    # row是一个列表
    date,h,l=[],[],[]
    for row in reader:
        try:
            current_datetime = datetime.strptime(row[0],r"%Y-%m-%d")
        except:
            continue
        h.append(int(row[1]))
        date.append(current_datetime)
        l.append(int(row[3]))
import matplotlib.pyplot as plt 
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(date,h,color='red')
plt.plot(date,l,color='blue')

# aplha指定颜色透明度，0是完全透明，1是完全不透明;facecolor指定填充区域颜色
plt.fill_between(date,h,l,facecolor='blue',alpha=0.1)

# 绘制斜的日期标签，避免重叠
fig.autofmt_xdate()
plt.title('Daily high and low temperature')
plt.tick_params(axis='both',which='major')
plt.show()

