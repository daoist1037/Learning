import copy
spam = ['a', 'b', 'c', 'd']
chees = copy.copy(spam)   ## 不能命名与模块同名的文件
## 如果复制的列表中包含了列表，那么就用 deepcopy()函数代替
chees[1] = 42
print(spam)
print(chees)