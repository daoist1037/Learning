""" def a(pra=[],value=0):
    pra.append(value)
    return pra

print('张三:{}'.format(a(value = 100)))
print(a(value = 50))


import re
a = re.compile(r'\d\d\d-(\d\d\d)-(\d\d\d\d)')
num = a.search('My number is 415-555-4242.')
print(num.groups()) """
import csv
with open('./result.csv','r') as f:
    # 列表形式读入
    reader = csv.reader(f)
    for row in reader:
        print(row)
with open('./result.csv','r') as f:
    # 字典形式读入
    reader = csv.DictReader(f)
    for row in reader:
        print(row)