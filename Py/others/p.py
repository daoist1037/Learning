""" import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2
plt.figure()
plt.plot(x,y1)
plt.plot(y1,x)
ax = plt.gca()
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('top')
# ax.invert_yaxis()
plt.show() """
import zipfile, os
    
newzip = zipfile.ZipFile('a.zip', 'w')
for folderName, subfolders, fileName in os.walk('.\\autoPython'):
    for folder in subfolders:
        # newzip.write(folder,compress_type=zipfile.ZIP_DEFLATED)
        print(folder)
    for file in fileName:
        file = folderName +'\\' +file
        print(file)
        newzip.write(file,compress_type=zipfile.ZIP_DEFLATED)    
newzip.close()