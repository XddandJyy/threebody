import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
m1 = 10  # 绿色
m2 = 1000  # 红色
m3 = 10  # 蓝色
observation_max = 100
f = open(sys.argv[1])
x1_all = []
y1_all = []
z1_all = []
x2_all = []
y2_all = []
z2_all = []
x3_all = []
y3_all = []
z3_all = []
i = 0
while True:
    l = f.readline()
    if not l:
        break
    l = l.split()
    x1_all.append(float(l[1]))
    y1_all.append(float(l[2]))
    z1_all.append(float(l[3]))
    x2_all.append(float(l[4]))
    y2_all.append(float(l[5]))
    z2_all.append(float(l[6]))
    x3_all.append(float(l[7]))
    y3_all.append(float(l[8]))
    z3_all.append(float(l[9]))
    fig=plt.figure()
    ax = Axes3D(fig)
    ax.plot3D(x1_all[i], y1_all[i], z1_all[i],'og', markersize=m1 * 30 / observation_max)
    ax.plot3D(x2_all[i], y2_all[i], z2_all[i],'or', markersize=m2 / observation_max)
    ax.plot3D(x3_all[i], y3_all[i], z3_all[i],'ob', markersize=m3 * 30 / observation_max)
    ax.plot3D(x1_all, y1_all, z1_all, '-g')
    ax.plot3D(x2_all, y2_all, z2_all, '-r')
    ax.plot3D(x3_all, y3_all, z3_all, '-b')

    plt.savefig('fig' + str(i) + '.jpg')
    i = i + 1
f.close()
