import csv
data = [    {'name':'梨花','age':20,'wage':1800},
            {'name':'张三','age':21,'wage':1800},
            {'name':'李四','age':22,'wage':1800}
        ]
with open('.\\pyscrapy\\result.csv', 'w', encoding="GBK",newline='') as f:
    context = csv.DictWriter(f, fieldnames=['name','age','wage'])
    context.writeheader()
    context.writerows(data)
    context.writerow({'name':'王五', 'age':23, 'wage':1800})
with open('.\\pyscrapy\\result.csv',encoding="GBK") as f:
    read = csv.DictReader(f)
    for rows in read:
        print(rows)