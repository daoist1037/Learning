import RandomWalk
import matplotlib.pyplot as plt
while True:
    ant = RandomWalk.RandomWalk()
    ant.fill_walk()

    # 可使用形参dpi向figure()传递该分辨率，以有效地利用可用的屏幕空间
    plt.figure(dpi=128,figsize=(10,6))
    plt.plot(ant.x_values,ant.y_values)
    # plt.scatter(ant.x_values,ant.y_values,s=1,c=ant.x_values,cmap=plt.cm.Blues)
    plt.scatter(ant.x_values[0],ant.y_values[0],s=40,color='red')
    plt.scatter(ant.x_values[-1],ant.y_values[-1],s=40,color='red')

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another RandowWalk?[y/n]")
    if keep_running == 'n':
        print("Wish to meet you next time")
        break