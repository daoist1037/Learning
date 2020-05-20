# from numpy.random import randn
# data = {i:randn() for i in range(7)}
# print(data)
""" import numpy as np 
b=3
a = np.array([0 for x in range(21)])
a[0]=b
print(a)
print(len(a))
b = np.linspace(21,21,21)
th=[]
a = (b)
print(a)
print(type(a)) """
import tensorflow as tf 
import matplotlib.pyplot as plt 
import numpy as np 

mnst = tf.keras.datasets.mnist
(train_x,train_y),(test_x,test_y)=mnst.load_data()

for i in range(4):
    num = np.random.randint(1,60000)

    plt.subplot(1,4,i+1)
    plt.axis('off')
    plt.imshow(train_x[num],cmap='gray')
plt.show()