#%%
import numpy as np
a = np.array([1,2,3,4])
print(a)
print(a.ndim,a.shape,a.size,a.dtype,a.itemsize,sep=' ')
b = np.array([1,2,3,4],dtype=np.int64)
print(b.itemsize)

print('create a nArray')
print(np.arange(1,100,2,dtype=np.int64))
# 前闭后开
print(np.ones((3,3),dtype=np.int64))
print(np.zeros((3,3),dtype=np.int64))
# ones((3,3))  (3,3)表示是shape的元组
print(np.eye(3,3,dtype=np.int64))
# eye()不输入shape的元组
print(np.linspace(1,10,10))
# 等差数列 前闭后闭
print(np.logspace(1,5,5,base=2,dtype=np.int64))
# 等比数列 start  和  stop均为指数

print('array and asarray')
# 当数据源本身是一个ndarray对象时，array()会复制出一个副本，占用新的内存，而asarray()则不复制副本, 它直接引用原数组
list1=[[1,2,3],[2,3,4],[3,4,5]]
array1=np.array(list1)
array2=np.asarray(list1)
list1[0][0]=3
print(array1)
print(array2)
print('two')
list1[0][0]=1
a = np.array(list1)
array1=np.array(a)
array2=np.asarray(a)
a[0][0]=3
print(array1)
print(array2)




b = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
b.reshape((3,4))
# 不改变当前数组
print(b)
b.resize((3,4))
# 改变当前数组
print(b)

print(b.reshape((-1,1)))
# 变为列向量，但不知道元素个数，用-1可以自动计算出这个维度的取值


a = np.array([[1,1],[0,1]])
b = np.array([[2,0],[3,4]])
c =a*b
print(c)
# 各个元素相乘
print(np.matmul(a,b))
print(np.dot(a,b))
# 以上为真正矩阵相乘的运算
print(np.transpose(c))
# 转置
print(np.linalg.inv(c))
# 求逆



# %%

# %%


# %%
