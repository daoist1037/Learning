#-*- encoding: UTF-8 -*-
"""
>	FileName:	class_1111.py
>	Author:	daoist
>	Email:	1748624858@qq.com
>	Creat:	2020:05:03:07:05
"""
#%%[markdown]
# 判断类型
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# 能用type()判断的基本类型也可以用isinstance()判断
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法

#%%
import os
from multiprocessing import Process
from enum import Enum
import types
def fn():
    pass
type(fn) == types.FunctionType
type(abs) == types.BuiltinFunctionType
type(lambda x: x) == types.LambdaType
type((x for x in range(10))) == types.GeneratorType
#%%[markdown]
# 创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性


#%%
class student(object):
    pass
s = student()
s.name = 'Michael'

def set_age(self,age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

def set_score(self, score):
    self.score = score
student.set_score = MethodType(set_score, student)
b = student()
b.set_score(100)
print(b.score)
# %%[markdown]
# 当我们需要定义常量时，一个办法是用大写变量通过整数来定义
# Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”
# Python内置的logging模块可以非常容易地记录错误信息;同样是出错，但程序打印完错误信息后会继续执行，并正常退出：
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例;只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型
#%%
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
             'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


# %%

# 子进程要执行的代码


# %%
