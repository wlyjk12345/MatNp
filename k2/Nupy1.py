from numpy import *
''''''
a = eye(2,2,dtype=uint8)  #无符号整数
_= float32(a)
print(_.dtype.name)
print(a)   #eye / zeros /ones /empty
#b =  arange(15).reshape(3,5)
b = arange(0,4,0.5)
print(b)
print(b.shape)  #dtype.name  / size /shape
c = array(([6, 7, 8],[1.5,2,44]))#, dtype=complex)
print(c)
d = c > 4
print(d)
'''d = linspace(0,3,9)
print(d)
e = a @ c
print(e)  # @矩阵乘  *点乘　
e *= 3
print(e)
print(random.random((2,3)))  #随机的浮点数在半开区间 [0,1.0)
print(random.randn(3,2))     #标准正态分布
print(random.randint(2,7,4))  #返回随机的整数，位于半开区间 [low, high)
# random_integers (low[, high, size])  返回随机的整数，位于闭区间 [low, high]
#shuffle 现场修改序列 permutation 返回一个随机排列
f = c.sum(axis=0)
print(f)
e =b[:2].copy
print(e)
'''