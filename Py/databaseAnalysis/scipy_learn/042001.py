# %%[markdown]
# # scipy.io 文件读取
# %%
from scipy.integrate import quad
from scipy.interpolate import interp1d
from scipy import io as spio
import numpy as np
a = np.ones((3, 3))
spio.savemat('file.mat', {'a': a})
data = spio.loadmat('file.mat', struct_as_record=True)
data['a']


# %%[markdown]
# # misc图片读取，这里使用imageio模块，misc没有imread模块
# %%
from PIL import Image
from scipy import misc
import imageio
import numpy as np
a_image = imageio.imread('../../1569054836920.jpg')
print(a_image)
import matplotlib.pyplot as plt
b_image = plt.imread('../../1569054836920.jpg')
print(b_image)
# %%[markdown]
# # 矩阵运算函数，与numpy类似 linalg
# %%
from scipy import linalg
arr = np.array([[1, 2], [3, 4]])
brr = linalg.det(arr)
crr =np.linalg.det(arr)

brr_inv = linalg.inv(arr)
crr_inv=np.linalg.inv(arr)
# %%[markdown]
# # 傅里叶变换 scipy.fftpack
# %%
from scipy import fftpack
time_step = 0.02
period = 5.
time_vec = np.arange(0, 20, time_step)
sig = np.sin(2 * np.pi / period * time_vec) + 0.5 * np.random.randn(time_vec.size)
# scipy.fftpack.fftfreq() 函数会生成采样频率，scipy.fftpack.fft() 则用于进行快速傅里叶变化
sample_freq = fftpack.fftfreq(sig.size, d=time_step)
sig_fft = fftpack.fft(sig)
# 由于产生的功率是对称的，因此只需要使用频谱的正部分来查找频率：
pidxs = np.where(sample_freq > 0)
freqs = sample_freq[pidxs]
power = np.abs(sig_fft)[pidxs]

import pylab as pl
pl.figure()
pl.plot(freqs, power)
pl.xlabel('Frequency [Hz]')
pl.ylabel('plower')
axes = pl.axes([0.3, 0.3, 0.5, 0.5])
pl.title('Peak frequency')
pl.plot(freqs[:8], power[:8])
pl.setp(axes, yticks=[])
# 信号频率可通过如下方式获得:
freq = freqs[power.argmax()]
np.allclose(freq, 1./period)  # check that correct freq is found
# 滤去傅里叶变化后的信号中的高频噪声:
sig_fft[np.abs(sample_freq) > freq] = 0
# ifft逆变换
main_sig=fftpack.ifft(sig_fft)

# import pylab as plt
import matplotlib.pyplot as plt
plt.figure()
plt.plot(time_vec, sig)
plt.plot(time_vec, main_sig, linewidth=3)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
# %%[markdown]
# np.trapz()
# 复化梯形法求积分
# %%[markdown]
# # 优化和拟合: scipy.optimize
# ## 寻找标量函数的零点optimize.fsolve
# ## 找出局部最低点，用scipy.optimize.fminbound，并指定变量区间
# ## 找到这个函数的最小值的常用有效方式是从给定的初始点开始进行一个梯度下降。BFGS算法  fmin_bfgs 这个方法的一个可能问题是，如果这个函数有一些局部最低点，算法可能找到这些局部最低点而不是全局最低点，这取决于初始点：
# ## 使用暴力算法来找到全局最小值 optimize.brute
# ## scipy.optimize.leatsq():最小二乘法拟合
# ## scipy.optimize.curve_fit() 非线性最小二乘拟合  已经知道了函数的形式是 (f) 但不知道每一项系数的大小。 我们可以使用最小二乘算法来进行曲线拟合得到系数的值，首先要定义要进行拟合的函数
# %%
from scipy import optimize
import numpy as np
def f(x):
    return x ** 2 + np.sin(x) * 10
root=optimize.fsolve(f,1)
root2 = optimize.fsolve(f, -2.5)
roots = optimize.fminbound(f,0, 10)
xdata = np.linspace(-10, 10, num=20)
ydata = f(xdata) + np.random.randn(xdata.size)
def f2(x, a, b):
    return a*x**2 + b*np.sin(x)
guess = [2, 2]
params, params_covariance = optimize.curve_fit(f2, xdata, ydata, guess)
# %%[markddown]
# ## 统计和随机数 scipy.stats
# %%
from scipy import stats
import numpy as np
import matplotlib.pyplot  as plt
a = np.random.normal(size=1000)
bins = np.arange(-4, 5)
bins
histogram = np.histogram(a, bins=bins, normed=True)[0]
bins = 0.5*(bins[1:] + bins[:-1])
bins


b = stats.norm.pdf(bins)  # norm 是一种分布
plt.plot(bins, histogram)
plt.plot(bins, b)
plt.show()


# %%[markdown]
# ## 插值：scipy.interpolate
# %%
from scipy.interpolate import interp1d
import numpy as np
measured_time = np.linspace(0, 1, 10)
noise = (np.random.random(10)*2 - 1) * 1e-1
measures = np.sin(2 * np.pi * measured_time) + noise
# scipy.interpolate.interp1d类可以建立一个线性插值函数
linear_interp = interp1d(measured_time, measures)
# scipy.interpolate.linear_interp实例需要评估感兴趣的时间点
computed_time = np.linspace(0, 1, 50)
linear_results = linear_interp(computed_time)
# 通过提供可选的参数kind也可以选择进行立方插值：
cubic_interp = interp1d(measured_time, measures, kind='cubic')
cubic_results = cubic_interp(computed_time)
# %%[markdowwn]
# ## 数值积分：scipy.integrate
# %%
from scipy.integrate import quad
res, err = quad(np.sin, 0, np.pi/2)
np.allclose(res, 1)
np.allclose(err, 1 - res)

# %%[markdown]
# ## sympy数学符号
# %%
import sympy
a = sympy.Rational(1, 2)
x =sympy.Symbol('x')
y =sympy.Symbol('y')
# %%
