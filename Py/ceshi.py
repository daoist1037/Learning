import numpy as np
y = np.arange(10)
print(y)
import requests
urls = 'https://www.baidu.com'
text = requests.get(url=urls).text
print(text[:250])
import matplotlib.pyplot as plt
plt.plot(y)
plt.show()
