from random_walk import RandomWalk
import matplotlib.pyplot as plt



while True:
    rw= RandomWalk(50000)
    rw.fill_walk()

    """设置图形大小"""
    plt.figure(figsize=(10, 6))

    """取消X和Y轴"""
    current_axes = plt.axes()
    current_axes.xaxis.set_visible(False)
    current_axes.yaxis.set_visible(False)


    """绘制渐变的图形"""

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    """突出起点和终点"""
    plt.scatter(0,0,c='green',edgecolors ='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)


    plt.show()
    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break
