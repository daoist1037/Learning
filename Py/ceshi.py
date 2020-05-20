import matplotlib.pyplot as plt
import numpy as np
y = np.arange(100)


plt.figure(figsize=(6.4, 4.8), frameon=None)
plt.plot(y)
plt.show()
import os
print(os.getcwd())
import requests
html_text = requests.get('https://www.baidu.com').text
print(html_text[:250])
