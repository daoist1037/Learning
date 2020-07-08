# import matplotlib.pyplot as plt
# import numpy as np
# import requests
# y = np.arange(10)
# print(y)
# urls = 'https://www.baidu.com'
# text = requests.get(url=urls).text
# print(text[:250])
# plt.plot(y)
# plt.show()
import tensorflow as tf
import timeit
# with tf.device('/cpu:0'):
#     cpu_a = tf.random.normal([10000, 1000])
#     cpu_b = tf.random.normal([1000, 2000])
#     print(cpu_a.device, cpu_b.device)
# with tf.device('/gpu:0'):
#     gpu_a = tf.random.normal([10000, 1000])
#     gpu_b = tf.random.normal([1000, 2000])
#     print(cpu_a.device, cpu_b.device)


def cpu_run():
    with tf.device('/cpu:0'):
        cpu_a = tf.random.normal([1000, 1000])
        cpu_b = tf.random.normal([1000, 2000])
        c = tf.matmul(cpu_a, cpu_b)
    return c


def gpu_run():
    with tf.device('/gpu:0'):
        gpu_a = tf.random.normal([10000, 10000])
        gpu_b = tf.random.normal([10000, 20000])
        c = tf.matmul(gpu_a, gpu_b)
    return c


# cpu_time = timeit.timeit(cpu_run, number=10)
gpu_time = timeit.timeit(gpu_run, number=10)
# print('warmup:', cpu_time, gpu_time)
print('warmup:', gpu_time)

# cpu_time = timeit.timeit(cpu_run, number=10)
# gpu_time = timeit.timeit(gpu_run, number=10)
# print('run time:', cpu_time, gpu_time)
# %%
c = [-1, 4]
A = [[-3, 1], [1, 2]]
b = [6, 4]
x0_bounds = (None, None)
x1_bounds = (-3, None)
from scipy.optimize import linprog
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds])


# %%
c = [-2, -3, 5]
a = [[-2, 5, -1], [1, 3, 1]]
b = [-10, 12]
aeq = [[1, 1, 1]]
deq = 7
import numpy as np
# x = linprog(c, a, b, aeq, deq, np.zeros(3, 1))
x = linprog(c ,A_ub=a, b_ub=b, A_eq=aeq, b_eq=deq, x0=np.zeros((3, 1)))

# %%

# %%
