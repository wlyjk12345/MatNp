from numpy import *
import matplotlib.pyplot as plt
#T，时间/A 破口面积/H 破口距外水面/h 内液面高//h1 液面差/h2 碗高/v 水速 = 0.62*sqrt(2*g*h1)
# s 水面面积/C 孔口出流流量系数/ M 质量/m 碗中的水重量 / q水 10³千克/立方米 q碗》q水 /a 碗加速度
#  p+ρgh+(1/2)*ρv^2=
#碗的重量+碗中的水重量=碗的外廓体积*水的密度*重力加速度。
#球形物体在粘滞性流体中运动时，所受到的粘滞阻力位：：F=6πηrv ，速度v、流体的粘滞系数η
#碗现状质量均匀
#极限情况1速度接近0，它时刻处于受力平衡，在洞不大且忽略粘滞阻力的情况下，通过洞口的水流速度等价于水掉落h高度得到的速度
# 2整个底无

#假设为一圆柱
v = 0.
H = 0.
h1 =0.
h2 =0.05
A = 0.00001
h = 0.
s =0.0001
g = 10.
Q = 0.
m =0.
M = 0.2
k = arange(10.)
V1 = h2*s
m_max = V1*1000*g/g - M
b = k.copy()
a = g
for t in arange(10):
    H = a * t * t /2  #sssss

    if m >= m_max :
        break


    m = m + 0.62 * A * sqrt(2*g*h1)#薄壁孔口，淹没出流

    h1 = H - m/s
    a = g - h1*1000*g  # ffff
    k[t] = a
fig = plt.figure()
plt.plot(b, k)
plt.show()
print(k)
print(b)