# 函数式编程
# lamdba
x =[1,2,3,4,5]
f = lambda y: y+2
print(x)
print(f(2))
# map函数 用于逐一运算
a =x
b = map(lambda x:x+2, a)
print(list(b))
c = list(b)
# map类型的变量经过一次for循环遍历之后，里面的元素都没有了
# c=[]
bb= map(lambda x,y:x*y,a,a)
print(list(bb))

# reduce函数 用于递归运算
from functools import reduce
e = reduce(lambda x,y:x*y,range(1,10))
# reduce函数首先将列表的前两个元素作为函数的参数进行运算，然后将运算结果与第三个数字作为函数的参数，依次循环
print(e)

# filter函数 筛选符号条件的元素
b = filter(lambda x : x>5 and x< 8,range(10))
print(list(b))