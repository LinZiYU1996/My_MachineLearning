# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/16 13:40'

import numpy as np


"""
拷贝
NumPy中拷贝分为三种情况：

完全不拷贝

一个数组的任何变化都反映在另一个数组上，包括值变化和形状变化

浅拷贝

一个数组值会变化会反映在另一个数组上，但是形状不变化

深拷贝

创建原数组的副本，副本的任何变化都不会反映在原数组上
"""


# 完全不拷贝
a = np.arange(12)
b = a
# print(a)
# print("")
# print(b)
# >>>
# [ 0  1  2  3  4  5  6  7  8  9 10 11]
#
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

b[5] = 5000
# print(a)
# print("")
# print(b)
# >>>
# [   0    1    2    3    4 5000    6    7    8    9   10   11]
#
# [   0    1    2    3    4 5000    6    7    8    9   10   11]

# print(b is a)
# >>>
# True

b.shape = (4,3)
print(a)
print("")
print(b)

# >>>
# [[   0    1    2]
#  [   3    4 5000]
#  [   6    7    8]
#  [   9   10   11]]
#
# [[   0    1    2]
#  [   3    4 5000]
#  [   6    7    8]
#  [   9   10   11]]



























































































