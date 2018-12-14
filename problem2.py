import matplotlib.pyplot as plt
import numpy as np
from sympy import *
####c_1(f_1) = 12 * (1 + 0.15*((f_1/1200)**4))
####c_2(f_2) = 18 * (1 + 0.15*((f_2/1500)**4))
####d = 3,500 vehicles/hour

#用户最优
####  c_1(f_1) = c_2(f_2)
####  f_1 + f_2 = d

def c_1(x):
    c_1 = 12 * (1 + 0.15*((x /1200)**4))
    return c_1

def c_2(x):
    c_2 = 18 * (1 + 0.15 * ((x / 1500) ** 4))
    return c_2

f_1 = np.arange(0, 3500, 0.001)
d = 3500

c1 = c_1(f_1)
c2 = c_2(d - f_1)
'''''
#根据差方求交点
crossover = 10000
for i in range(len(c1)):
    distance = (c1[i] - c2[i])**2
    if distance <= crossover:
        crossover = distance
        x_point = i * 0.02
        y1_point = c1[i]
        y2_point = c2[i]

print(x_point, y1_point)
'''''
#绘制c_1(f_1)的图像
plt.plot(f_1, c2, color = "b")

#绘制c_2(f_2)
#plt.plot(f_1, c2, color = 'y', linestyle = '--')

#图像加注

#系统最优
####  c_1(f_1) + f_1 * (d c_1(f_1)/d f_1) = c_2(f_2) + f_2 * (d c_2(f_2)/d f_2)
####  f_1 + f_2 = d
####  d c_1(f_1)/d f_1 = 3.47222222222222e-12*x**3
####  d c_2(f_2)/d f_2 = 2.13333333333333e-12*x**3
def soc_1(x):
    c_1 = 12 * (1 + 0.15 * ((x / 1200) ** 4))
    soc1 = c_1 + x * (3.47222222222222e-12*x**3)
    return soc1

def soc_2(x):
    c_2 = 18 * (1 + 0.15 * ((x / 1500) ** 4))
    soc2 = c_2 + x*(2.13333333333333e-12*x**3)
    return soc2

f_2 = np.arange(0, 3500, 0.001)
d = 3500

soc1 = soc_1(f_2)
soc2 = soc_2(d - f_2)
'''''
crossover = 10000
for i in range(len(soc1)):
    distance = (soc1[i] - soc2[i])**2
    if distance <= crossover:
        crossover = distance
        x_point = i * 0.001
        y1_point = soc1[i]
        y2_point = soc2[i]

print(x_point, y1_point, y2_point)
'''''


plt.xlabel('line2-flow')
plt.ylabel('time')
plt.plot(f_2, soc2, color = "r")
plt.text(1000,300,"SO")
plt.text(500,150,"UE")
#plt.plot(f_2, c2, color = 'y', linestyle = '--')
plt.show()