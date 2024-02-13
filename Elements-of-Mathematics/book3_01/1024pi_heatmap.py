#圆周率小数点后1024位热图
import numpy as np
from mpmath import mp
import seaborn as sns
import matplotlib.pyplot as plt
import time
t1 = time.time()

#取pi的1024位小数
mp.dps = 1024 + 1   # 要出正方形热图，1024个，就是32*32
pi = mp.pi
# print(pi)

# 转换为字符串
pi = str(pi)

# 去除小数点
pi = pi.replace('.', '')

# 取后1024位
pi_1024 = pi[1:]
# print(pi_1024)

#把整数分割为数组
pi_1024List = list(pi_1024)
# print(pi_1024List)

#字符串数组转换为数字数组：因为元素是字符串不能在热图里使用，所以必须都转成int或float
pi_1024N = [ int(x) for x in pi_1024List ]     #列表推导式
# print(pi_1024N)

#一维数组转多维数组：
'''
用 numpy.array()函数定义向量时如果只用一层中括号 []，比如
numpy.array([1, 2, 3])，得到的结果只有一个维度。有两层中括号 [[]]，
numpy.array([[1, 2, 3]]) 得到的结果有两个维度
'''
array = np.array(pi_1024N)
pi_array = array.reshape(32,32)
# print(pi_array)

#绘制热图
sns.set(rc = {'figure.figsize':(6,5)})
sns.heatmap(pi_array, cmap='RdYlBu_r', xticklabels = False, yticklabels = False)
plt.show()
t2 = time.time()
print(t2 - t1)
