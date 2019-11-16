# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/16 15:09'


"""
6、数组转置和轴对换
转置和轴对换返回的是原对象的视图，不是新对象
"""


import numpy as np


arr = np.arange(12).reshape(3,4)


# print(arr)
# # >>>
# # [[ 0  1  2  3]
# #  [ 4  5  6  7]
# #  [ 8  9 10 11]]


# print(arr.T)
# >>>
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]

# print(arr.transpose())
# >>>
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]


# print(arr)
# >>>
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# arr.T[:2] = 0
# print(arr)
# >>>
# [[ 0  0  2  3]
#  [ 0  0  6  7]
#  [ 0  0 10 11]]






















































































