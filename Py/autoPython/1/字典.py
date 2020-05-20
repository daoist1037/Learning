myCat = {'size':'fat', 'color':'gray', 'disposition':'loud'}
print(myCat['size'])
# 字典没有顺序

# 键  值   键-值对
for i in myCat.values():
    print(i)
for j in myCat.keys():
    print(j)
for k in myCat.items():
    print(k)

print(myCat.values())
print(list(myCat.values()))


for k,v in myCat.items():
    print('keys ' + k + 'Value ' + v)



# get()函数有两个参数：要取得其值的键，以及如果不存在返回的备用值
pin = {'apples':5, 'cups':2}
print('I am bringing ' + str( pin.get('cups',0) ) + ' cups')
print('I am bringing ' + str( pin.get('eggs',0) ) + ' eggs')

# setfault()
pin.setdefault('color', 'black')