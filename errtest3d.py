import math
import sys

import matplotlib.pyplot as plt
import numpy as np

G = 1
m1 = 10
m2 = 1000
m3 = 10

ix1 = 0
iy1 = 500
iz1 = -100
ix2 = 0
iy2 = 0
iz2 = 0
ix3 = 0
iy3 = 1000
iz3 = 100
iv1_x = 1.5
iv1_y = 0
iv1_z = 0
iv2_x = 0
iv2_y = 0
iv2_z = 0
iv3_x = 0.8
iv3_y = 0
iv3_z = 0
f = open(sys.argv[1])
t = []
x1 = []
y1 = []
z1 = []
x2 = []
y2 = []
z2 = []
x3 = []
y3 = []
z3 = []
v1_x = []
v1_y = []
v1_z = []
v2_x = []
v2_y = []
v2_z = []
v3_x = []
v3_y = []
v3_z = []
while True:
    l = f.readline()
    if not l:
        break
    l = l.split()
    t.append(float(l[0]))
    x1.append(float(l[1]))
    y1.append(float(l[2]))
    z1.append(float(l[3]))
    x2.append(float(l[4]))
    y2.append(float(l[5]))
    z2.append(float(l[6]))
    x3.append(float(l[7]))
    y3.append(float(l[8]))
    z3.append(float(l[9]))
    v1_x.append(float(l[10]))
    v1_y.append(float(l[11]))
    v1_z.append(float(l[12]))
    v2_x.append(float(l[13]))
    v2_y.append(float(l[14]))
    v2_z.append(float(l[15]))
    v3_x.append(float(l[16]))
    v3_y.append(float(l[17]))
    v3_z.append(float(l[18]))
f.close()


def cacl_E(x1, y1, z1, x2, y2, z2, x3, y3, z3, v1_x, v1_y, v1_z, v2_x, v2_y, v2_z, v3_x, v3_y, v3_z):
    dis12 = np.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) + (z1 - z2) * (z1 - z2))
    dis23 = np.sqrt((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2) + (z3 - z2) * (z3 - z2))
    dis13 = np.sqrt((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1) + (z3 - z1) * (z3 - z1))
    U = -G * (m1 * m2 / dis12 + m2 * m3 / dis23 + m1 * m3 / dis13)
    K = 0.5 * (m1 * (v1_x * v1_x + v1_y * v1_y + v1_z * v1_z) + m2 * (v2_x * v2_x + v2_y * v2_y + v2_z * v2_z) + m3 * (
                v3_x * v3_x + v3_y * v3_y + v3_z * v3_z))
    return U + K


E0 = cacl_E(ix1, iy1, iz1, ix2, iy2, iz2, ix3, iy3, iz3, iv1_x, iv1_y, iv1_z, iv2_x, iv2_y, iv2_z, iv3_x, iv3_y, iv3_z)
print(E0)
err = np.zeros(len(t))
for i in range(len(t)):
    Ei = cacl_E(x1[i], y1[i], z1[i], x2[i], y2[i], z2[i], x3[i], y3[i], z3[i], v1_x[i], v1_y[i], v1_z[i], v2_x[i],
                v2_y[i], v2_z[i], v3_x[i], v3_y[i], v3_z[i])
    err[i] = math.log(np.abs(Ei - E0) / np.abs(E0))

fig = plt.figure()
l = plt.plot(t, err)
plt.xlabel('t')
plt.ylabel('err')
plt.show()
