# -*- coding: utf-8 -*-

# @Time  : 2019/12/15 15:12

# @Author : Mr.Lin


'''

3.2. 调整估计器的超参数

'''

'''
超参数，即不直接在估计器内学习的参数。在 scikit-learn 包中，它们作为估计器类中构造函数的参数进行传递。典型的例子有：用于支持向量分类器的 C 、kernel 和 gamma ，用于Lasso的 alpha 等。

搜索超参数空间以便获得最好 交叉验证 分数的方法是可能的而且是值得提倡的。

通过这种方式，构造估计器时被提供的任何参数或许都能被优化。具体来说，要获取到给定估计器的所有参数的名称和当前值，使用:

estimator.get_params()
Copy
搜索包括:

估计器(回归器或分类器，例如 sklearn.svm.SVC())
参数空间
搜寻或采样候选的方法
交叉验证方案
计分函数
'''