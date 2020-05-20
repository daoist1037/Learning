#%%[markdown]
# # 位置参数
#%%
def fun(x, n):
    return x ** n
a=fun(2,3)
#%%
# # 必选参数
def fun_2(x, n):
    return x ** n
a = fun_2(2, 3)
#%%
# # 可变参数
def fun_4(*args):
    if len(args) == 0:
        return 0
    elif len(args) == 1:
        x = args[0]
        return x ** 2
    else:
        x, n = args
        return x**n
a = fun_4(2)
#%%
# # 关键字参数
def fun_5(**kw):

    return kw.get('x', 1)**kw.get('n', 2)
    
a = fun_5(x=2)
# %%
# # 默认参数


def fun_6(x, l=[]):
    l.append('end')
    return l
l = ['a']
b =[]
a = fun_6(l)
a = fun_6(b)
a = fun_6(b)
a = fun_6(b)
## 这里b最后会是多个end，注意考察原因
# # 参数组合


# %%[markdown]
# # 装饰器
# # 偏函数



#%%
class stu(object):
    def __init__(self):
        pass
    def add(self):
        print('a')
a = stu()
dir(a)
# 显示该类对象的所有属性和方法
# # 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
# # 上述分别是获取一个对象的某个属性或者方法，设置属性或者方法，判断是否有相应属性或者方法
# %%
