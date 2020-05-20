#%%
import numpy as np
data = np.random.randn(2, 3)
print(data)
#%%[markdown]
# # ndarray有一个swapaxes方法，该方法接收一对轴编号作为参数，并对轴进行调整用于重组数据：
# # swapaxes返回的是数据的视图，而没有对数据进行复制
# %%
import numpy as np
arr = np.arange(12).reshape((3, 4))
# print(np.dot(arr.T,arr))
print(arr.swapaxes(0,1))
# %%
import numpy as np
a_list = [x for x in range(12)]
b = a_list
c = a_list[:4]
d = a_list[1]
b[1] = 7
print('b1',a_list)
c[1] = 8
print('c1', a_list)
d = 6
print('d1', a_list)
# 列表只有在复制即 b =a 时，改变b的值才会影响a，只用切片或者单个元素赋值，不同步

a_array = np.arange(12)
b_array = a_array
c_array = a_array[:4]
d_array = a_array[1]
e_array=a_array[[0,1,2,3]]
b_array[1] = 7
c_array[1] = 8
d_array = 6
e_array[1]=5
# 数组 整体幅值和切片幅值，修改会影响到原先的数组
# 数组的神奇索引不会影响到原先的数组，等于产生新的数组
# %%[markdown]
# # numpy.where函数是三元表达式x if condition else y的向量化版本。
# # np.meshgrid函数接收两个一维数组，并根据两个数组的所有(x, y)对生成一个二维矩阵 与笛卡尔积类似
# # 语法：X,Y = numpy.meshgrid(x, y)
# # 输入的x，y，就是网格点的横纵坐标列向量（非矩阵）
# # 输出的X，Y，就是坐标矩阵。
#%%
import numpy as np
conda_point = np.arange(12)
conda_point2 = np.random.rand(13)
x_conda, y_conda = np.meshgrid(conda_point, conda_point2)
a_where = np.random.randn(4, 4)
b_where=np.where(a_where>0,2,-2)
# %%[markdown]
# # 对于布尔值数组，有两个非常有用的方法any和all。any检查数组中是否至少有一个True，而all检查是否每个值都是True
# # 这些方法也可适用于非布尔值数组，所有的非0元素都会按True处理。
#%%
np.array([True]*3+[False]*2).any()
np.array([True]*3+[False]*2).all()
# %%
import pandas as pd
a_series = pd.Series(['a', 'b', 'c', 'd'])
a_Date=pd.DataFrame(a_series,columns=['shabi'])

# %%
