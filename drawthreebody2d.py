import matplotlib.pyplot as plt
import sys

import numpy as np

m1 = 10  # 绿色
m2 = 1000 # 红色
m3 = 10  # 蓝色
observation_max = 100
f = open(sys.argv[1])
x1_all = []
y1_all = []
x2_all = []
y2_all = []
x3_all = []
y3_all = []
i = 0
while True:
    l = f.readline()
    if not l:
        break
    l = l.split()
    x1_all.append(float(l[1]))
    y1_all.append(float(l[2]))
    x2_all.append(float(l[3]))
    y2_all.append(float(l[4]))
    x3_all.append(float(l[5]))
    y3_all.append(float(l[6]))
    axis_x = np.mean([x1_all[i], x2_all[i], x3_all[i]])  # 观测坐标中心固定在平均值的地方
    axis_y = np.mean([y1_all[i], y2_all[i], y3_all[i]])  # 观测坐标中心固定在平均值的地方
    while True:
        if np.abs(x1_all[i] - axis_x) > observation_max or np.abs(x2_all[i] - axis_x) > observation_max or np.abs(
                x3_all[i] - axis_x) > observation_max or \
                np.abs(y1_all[i] - axis_y) > observation_max or np.abs(y2_all[i] - axis_y) > observation_max or np.abs(
            y3_all[i] - axis_y) > observation_max:
            observation_max = observation_max * 2  # 有一个物体超出视线时，视线范围翻倍
        elif np.abs(x1_all[i] - axis_x) < observation_max / 10 and np.abs(x2_all[i] - axis_x) < observation_max / 10 and np.abs(
                x3_all[i] - axis_x) < observation_max / 10 and \
                np.abs(y1_all[i] - axis_y) < observation_max / 10 and np.abs(y2_all[i]- axis_y) < observation_max / 10 and np.abs(
            y3_all[i] - axis_y) < observation_max / 10:
            observation_max = observation_max / 2  # 所有物体都在的视线的10分之一内，视线范围减半
        else:
            break

    plt.axis([axis_x - observation_max, axis_x + observation_max, axis_y - observation_max, axis_y + observation_max])

    plt.plot(x1_all[i], y1_all[i], 'og', markersize=m1 * 30 / observation_max)  # 默认密度相同，质量越大的，球面积越大。视线范围越宽，球看起来越小。
    plt.plot(x2_all[i], y2_all[i], 'or', markersize=m2 * 30 / observation_max)
    plt.plot(x3_all[i], y3_all[i], 'ob', markersize=m3 * 30 / observation_max)
    plt.plot(x1_all, y1_all, '-g')  # 画轨迹
    plt.plot(x2_all, y2_all, '-r')
    plt.plot(x3_all, y3_all, '-b')
    plt.savefig('fig' + str(i) + '.jpg')
    i = i + 1
f.close()
