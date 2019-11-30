# -*- coding: utf-8 -*-

# @Time  : 2019/11/30 16:16

# @Author : Mr.Lin


import  numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号


"""
通用解决函数
"""



"""
判别函数，检查所有数据是否已经分类完成
"""
def Judge(X,y,w):

    n = X.shape[0]

    # 判断是否同号
    num = np.sum(X.dot(w)*y>0)

    return n == num



"""
    生成N个d维点,x1+...+xd>=t的点标记为+1，x1+...+xd<=-t的点标记为-1，
	rnd为随机数生成器，形式为rnd = np.random.RandomState(seed)，seed为随机种子
"""
def data(N,d,rnd,t=0.1):
    X = []
    w = np.ones(d)
    print("w : \n",w)
    print("")
    print("")
    while (len(X) < N):
        x = rnd.uniform(-1, 1, size=(d))
        if np.abs(x.dot(w)) >= t:
            X.append(x)

    X = np.array(X)
    print("X : \n",X)
    print("")
    print("")
    y = 2 * (X.dot(w) > 0) - 1
    print("y : \n",y)
    print("")
    print("")
    # 添加第一个分量为1
    X = np.c_[np.ones((N, 1)), X]
    print(X)
    print("")
    print("")

    print("X[1, :]  \n",X[1, :])
    return X, y
# 测试结果集：

# w :
#  [ 1.  1.]
#
#
# X :
#  [[-0.25091976  0.90142861]
#  [ 0.46398788  0.19731697]
#  [-0.68796272 -0.68801096]
#  [-0.88383278  0.73235229]
#  [ 0.20223002  0.41614516]
#  [-0.63635007 -0.63319098]
#  [-0.39151551  0.04951286]
#  [-0.13610996 -0.41754172]
#  [ 0.22370579 -0.72101228]
#  [-0.4157107  -0.26727631]
#  [-0.08786003  0.57035192]
#  [-0.60065244  0.02846888]
#  [ 0.18482914 -0.90709917]
#  [ 0.2150897  -0.65895175]
#  [ 0.93126407  0.6167947 ]
#  [-0.39077246 -0.80465577]
#  [ 0.36846605 -0.11969501]
#  [-0.75592353 -0.00964618]
#  [-0.93122296  0.8186408 ]
#  [-0.48244004  0.32504457]]
#
#
# y :
#  [ 1  1 -1 -1  1 -1 -1 -1 -1 -1  1 -1 -1 -1  1 -1  1 -1 -1 -1]
#
#
# [[ 1.         -0.25091976  0.90142861]
#  [ 1.          0.46398788  0.19731697]
#  [ 1.         -0.68796272 -0.68801096]
#  [ 1.         -0.88383278  0.73235229]
#  [ 1.          0.20223002  0.41614516]
#  [ 1.         -0.63635007 -0.63319098]
#  [ 1.         -0.39151551  0.04951286]
#  [ 1.         -0.13610996 -0.41754172]
#  [ 1.          0.22370579 -0.72101228]
#  [ 1.         -0.4157107  -0.26727631]
#  [ 1.         -0.08786003  0.57035192]
#  [ 1.         -0.60065244  0.02846888]
#  [ 1.          0.18482914 -0.90709917]
#  [ 1.          0.2150897  -0.65895175]
#  [ 1.          0.93126407  0.6167947 ]
#  [ 1.         -0.39077246 -0.80465577]
#  [ 1.          0.36846605 -0.11969501]
#  [ 1.         -0.75592353 -0.00964618]
#  [ 1.         -0.93122296  0.8186408 ]
#  [ 1.         -0.48244004  0.32504457]]


def f(N, d, rnd, t=0.1, r=1):
    """
    生成N个d维点（不包括偏置项1），x1+...+xd>=t的点标记为+1，x1+...+xd<=-t的点标记为-1，
    rnd为随机数生成器，形式为rnd = np.random.RandomState(seed)，seed为随机种子
	利用PLA更新，如果r=1，那么按照顺序取点，否则随机取点
    """
    X, y = data(N, d, rnd, t=t)

    # 记录次数
    s = 0
    # 初始化w=[0, 0, 0]
    w = np.zeros(d + 1)
    # 数据数量
    n = X.shape[0]
    if r == 1:
        while (Judge(X, y, w) == 0):
            for i in range(n):
                if X[i, :].dot(w) * y[i] <= 0:
                    w += y[i] * X[i, :]
                    s += 1
    else:
        while (Judge(X, y, w) == 0):
            i = np.random.randint(0, N)
            if X[i, :].dot(w) * y[i] <= 0:
                w += y[i] * X[i, :]
                s += 1

    # 直线方程为w0+w1*x1+w2*x2=0,根据此生成点
    a = np.arange(-1, 1, 0.1)
    b = (a * w[1] + w[0]) / (- w[2])

    # 原直线方程为x1+x2 = 0
    c = - a

    # 返回数据
    return a, b, c, X, y, s, w


def plot_helper(a, b, c, X, y, s, w, t=0):
    """
    作图函数
    """
    #画出图像
    plt.scatter(X[y == 1][:, 1], X[y == 1][:, 2], c='r', s=1)
    plt.scatter(X[y == -1][:, 1], X[y == -1][:, 2], c='b', s=1)
    plt.plot(a, b, label="("+str(w[0])+")+("+str(w[1])+")x1+("+str(w[2])+")x2=0")
    plt.plot(a, c, label="x1+x2="+str(t))
    plt.title(u"经过"+str(s)+u"次迭代收敛")
    plt.legend()
    plt.show()























