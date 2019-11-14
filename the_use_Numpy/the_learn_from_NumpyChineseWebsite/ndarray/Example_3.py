# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/14 16:21'

import numpy as np

"""
高级索引

当选择对象 obj 是非元组序列对象，ndarray（数据类型为整数或bool）
或
具有至少一个序列对象或ndarray（数据类型为integer或bool）的元组时，
将触发高级索引。高级索引有两种类型：整数和布尔值。

高级索引始终返回数据的 副本 （与返回视图的基本切片形成对比）

"""

"""
高级索引的定义意味着x[(1,2,3),]根本不同于x[(1,2,3)]。
后者相当于x[1,2,3]触发基本选择，而前者将触发高级索引。
一定要明白为什么会这样。

同时认识到x[[1,2,3]]将触发高级索引，
而由于上面提到的不推荐的数字兼容性， 
x[[1,2,slice(None)]]将触发基本切片。
"""


"""
纯整数数组索引
当索引包含尽可能多的整数数组时，索引的数组具有维度，索引是直接的，但与切片不同。

高级索引始终作为 一个 整体进行 广播 和迭代：

result[i_1, ..., i_M] == x[ind_1[i_1, ..., i_M], ind_2[i_1, ..., i_M],
                           ..., ind_N[i_1, ..., i_M]]
"""

"""
请注意，结果形状与（广播）索引数组形状 ind_1, ..., ind_N 相同。

"""


x = np.array([[1, 2], [3, 4], [5, 6]])

print("x--------------->",x)
print("---------------------------------------------")
print(x[[0, 1, 2], [0, 1, 0]])

















































