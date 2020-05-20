#%%[markdown]
# # tuple 元组
# ## 元组一旦创建，各个位置上的对象是无法被修改的，如果一个元组的元素是可变的，就可以在其内部修改
# ## 元组连接 +
# ## 元组拆包
# ## 轻松交换变量名
# ## *rest *_是不想要的数据
# ## count方法统计某个元素出现的次数
#%%
a = 1, 2, 3
print(a)
a = 'string'
a = tuple(a)
print(a)
b = 'too', (2, 3, 4), [1, 2], True
print(b)
b[2].append(3)
print(b)

c = 'bar',
print(c + b)

s1, s2, s3, s4 = b
print(s1)
s1, s2, *_ = b
print(s1)

a1, a2 = 1, 2
a1, a2 = a2, a1
print(a1)

a = (1, 2, 3, 2, 4, 2, 3,)
print(a.count(2))
# %%[markdown]
# # list 列表
# ## append
# ## insert 插入的位置超出列表范围，会插入在末尾
# ## pop 原列表删除某个元素，并返回删除的元素 根据index
# ## remove 不返回值
# ## index
# ## extend向列表添加多个元素 不返回值 extend较添加的方法，消费小，因为连接过程中创建了新表，并且还要复制表
# ## 排序sort key指定排序方法
#%%
b_list = []
b_list.append('a')
b_list.insert(3, 'b')
print(b_list)
print(b_list.index('a'))
print(b_list.pop(1), b_list)
print(b_list.remove('a'),b_list)
b_list.extend([7, 8])
print(b_list)

e = [1, 3, 2, 6, 3, 7, 4, 2, 7, 3]
print(e.sort(), e)
e = ['foo', 'sdad', 'hsgdjf', 'a']
print(e.sort(key=len),e)
# %%[markdown]
# # 内建序列函数
# ## enumerate返回(i,values)的元组，i是索引，values是值
# ## sorted返回一个根据任意序列中的元素新建的已排序列表;接受的参数与列表的sort方法一致
# ## zip将列表、元组或其他序列的元素配对，新建一个元组构成的列表;可以处理任意长度的序列，它生成列表长度由最短的序列决定；转换成列表输出
# ## zip对象，遍历一遍只后为空
# ## reversed函数将序列的元素倒序排列 是一个生成器;因此如果没有实例化（例如使用list函数或进行for循环）的时候，它并不会产生一个倒序的列表
# %%
for i, values in enumerate(b_list):
    pass
print(i, values)

print(sorted([2, 3, 1, 6, 7, 12, 4]))
print(sorted('horse race'))

seq1 = ['s', 1, 'c']
seq2 = [2, '2', 'd', 'e']
zipped = zip(seq1, seq2)
print(list(zipped))
d=[(1,2),('s',1),('sda','sd')]
first, second = zip(*d)
print(first, second)

aa = list(reversed(range(10)))
print(list(reversed(range(10))))
print(aa)
# %%[markdown]
# # 字典
# ## 使用del关键字或pop方法删除值，pop方法会在删除的同时返回被删的值，并删除键
# ## keys方法和values方法会分别为你提供字典键、值的迭代器
# ## 使用update方法将两个字典合并;如果传给update方法的数据也含有相同的键，则它的值将会被覆盖。
# ## 字典的get方法和pop方法可以返回一个默认值；带有默认值的get方法会在key参数不是字典的键时返回None，而pop会抛出异常
# + 传递给该方法的第一个参数，是要检查的键。第二个参数，是如果该键不存在时要设置的值。如果该键确实存在，方法就会返回键的值
# + 与`get()`区别是：`get`只是返回值，并不更改/添加键-值，`setdefault`则是设置默认值（如果不存在）并返回`value`，若存在则返回`value`
# %%
dict_a = {'a': [1, 2, 3], 1: 'c'}
dict_a.update({'e': (1, 2, 3)})
print(dict_a)

# %%[markdown]
# # 通过hash函数可以检查一个对象是否可以哈希化（即是否可以用作字典的键
# %%[markdown]
# # 集合是一种无序且元素唯一的容器
# ## 两种创建方式：通过set函数或者是用字面值集与大括号的语法
# ## 集合支持数学上的集合操作，例如联合、交集、差集、对称差集
# %%
a = {1, 2, 3}
b = set([2, 3, 4, 5])
c = a.union(b)
print(a)
print(c)
print(a|b)

c = a.intersection(b)
print(c)
print(a&b)
# %%[markdown]
# # 列表推导式
# # 字典推导式
#%%
col = range(10)
cool = [x for x in col if x > 5]
print(cool)
cooll = {str(x): x for x in col if x < 7}
print(cooll)
coolll = {x for x in col if x > 5}
print(coolll)
# %%[markdown]
# # 生成器和生成器表达式
#%%
gen = (x ** 2 for x in range(100))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# %%[markdown]
# # 标准库中的itertools模块是适用于大多数数据算法的生成器集合。例如，groupby可以根据任意的序列和一个函数，通过函数的返回值对序列中连续的元素进行分组
#%%
import itertools
first_letter = lambda x: x[0]
names =[' Alan', ' Adam', ' wes', ' Will', ' Albert', ' steven']
for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names)) # names is a generator A [' Alan', ' Adam']

