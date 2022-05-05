import math
import sys

import matplotlib.pyplot as plt
import numpy as np

G = 1
m1 = 10
m2 = 1000
m3 = 10
ix1=0
iy1=500
ix2=0
iy2=0
ix3=0
iy3=1000

iv1_x=0
iv1_y=0
iv2_x=0
iv2_y=0
iv3_x=0
iv3_y=0

f = open(sys.argv[1])
t = []
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
v1_x = []
v1_y = []
v2_x = []
v2_y = []
v3_x = []
v3_y = []
while True:
    l = f.readline()
    if not l:
        break
    l = l.split()
    t.append(float(l[0]))
    x1.append(float(l[1]))
    y1.append(float(l[2]))
    x2.append(float(l[3]))
    y2.append(float(l[4]))
    x3.append(float(l[5]))
    y3.append(float(l[6]))
    v1_x.append(float(l[7]))
    v1_y.append(float(l[8]))
    v2_x.append(float(l[9]))
    v2_y.append(float(l[10]))
    v3_x.append(float(l[11]))
    v3_y.append(float(l[12]))
f.close()


def cacl_E(M1, M2, M3, x1, y1, x2, y2, x3, y3, v1_x, v1_y, v2_x, v2_y, v3_x, v3_y):
    dis12 = np.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    dis23 = np.sqrt((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2))
    dis13 = np.sqrt((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1))
    U = -G * (M1 * M2 / dis12 + M2 * M3 / dis23 + M1 * M3 / dis13)
    K = 0.5 * (M1 * (v1_x * v1_x + v1_y * v1_y) + M2 * (v2_x * v2_x + v2_y * v2_y) + M3 * (v3_x * v3_x + v3_y * v3_y))
    return U + K


E0 = cacl_E(m1,m2,m3,ix1,iy1,ix2,iy2,ix3,iy3,iv1_x,iv1_y,iv2_x,iv2_y,iv3_x,iv3_y)
print(E0)
err = np.zeros(len(t))
for i in range(len(t)):
    Ei = cacl_E(m1,m2,m3,x1[i], y1[i], x2[i], y2[i], x3[i], y3[i], v1_x[i], v1_y[i], v2_x[i], v2_y[i], v3_x[i], v3_y[i])
    err[i] = math.log((np.abs(Ei - E0) / np.abs(E0)), 10)

fig = plt.figure()
l = plt.plot(t, err)
plt.xlabel('t')
plt.ylabel('err')
plt.show()
