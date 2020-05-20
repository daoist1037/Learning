#%%
import pandas as pd
import numpy as np
a = np.linspace(0, 20, 10, endpoint=False)
print(a)

d = pd.DataFrame(np.arange(10).reshape(2, 5))
print(d)
dt = []
d = pd.DataFrame(dt, index=['a', 'b', 'c'], columns=['two', 'three'])
print(d)
dt = {'one': pd.Series([1, 2, 3], index=['a', 'd', 'c']),
      'two': pd.Series([9, 8, 7, 6], index=['a', 'd', 'c', 'b'])}
print(dt)
d = pd.DataFrame(data=dt)
print(d)
# %%
import numpy as np
np.random.seed(64)
data=np.random.randn(2, 3)
print(data)
np.random.seed(64)
data=np.random.randn(2, 3)
print(data)
#%%


def count():
      fs = []
      def f(j):
          return j * j
      for i in range(4):
            fs.append(f(i))
      return fs


f1, f2, f3,*_ = count()


# %%
