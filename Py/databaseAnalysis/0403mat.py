import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0,10,1000)
y=np.sin(x)+1
z=np.cos(x**2)+1

plt.figure(figsize=(8,4))
plt.plot(x,y,label=r'$\sin x+1$',color = 'r',linewidth=2)
plt.plot(x,z,label=r'$\cos x^2+1$',color='b',linestyle='--',linewidth=2)
plt.xlabel('Time(s)')
plt.ylabel('Volt')
plt.title('A Simple Example')
plt.ylim(0,2.2)
plt.legend()
plt.show()