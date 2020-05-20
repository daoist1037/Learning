import matplotlib.pyplot as plt
a=[1,2,3,4,5]
sqare= [1,4, 9, 6 ,25 ]

# 折线图
plt.plot(a,sqare,linewidth=5)

# 标题
plt.title("a numbers", fontsize=24)

## 坐标轴标题
plt.xlabel("value", fontsize=14)
plt.ylabel("square of value", fontsize=14)


plt.tick_params(axis='both',which='both',labelsize=14)

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

# 散点图
# c and cmap 形成颜色的映射，渐变色
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=40)
x_values = list(range(1,1001))
y_values = [x for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=40)

# bbox_inches='tight'让保存的文件排去多余的部分
# plt.savefig('squares.png',bbox_inches='tight')
plt.show()
