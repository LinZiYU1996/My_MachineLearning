# -*- coding: utf-8 -*-
# @Time  : 2019/12/4 22:59
# @Author : Mr.Lin

"""
朴素贝叶斯
基于贝叶斯定理与特征条件独立假设的分类方法。
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from collections import Counter
import math


# data
def create_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['label'] = iris.target
    df.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'label']
    data = np.array(df.iloc[:100, :])
    # print(data)
    return data[:,:-1], data[:,-1]


X, y = create_data()
print("y: \n{}".format(y))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
count_pairs = Counter(y)
print("")
print("")
print("count_pairs:\n{}".format(count_pairs))
print("")
print("")
print("X_train:\n{}".format(X_train))
print("")
print("")

# X_train:
# [[ 5.   3.5  1.6  0.6]
#  [ 4.6  3.2  1.4  0.2]
#  [ 5.4  3.7  1.5  0.2]
#  [ 5.8  2.6  4.   1.2]
#  [ 5.7  3.8  1.7  0.3]
#  [ 6.2  2.2  4.5  1.5]
#  [ 5.5  3.5  1.3  0.2]
#  [ 5.5  2.6  4.4  1.2]
#  [ 5.   3.4  1.6  0.4]
#  [ 4.7  3.2  1.3  0.2]
#  [ 5.3  3.7  1.5  0.2]
#  [ 4.8  3.   1.4  0.1]
#  [ 5.4  3.9  1.7  0.4]
#  [ 5.2  2.7  3.9  1.4]
#  [ 5.2  3.5  1.5  0.2]
#  [ 5.1  2.5  3.   1.1]
#  [ 6.4  2.9  4.3  1.3]
#  [ 4.8  3.4  1.9  0.2]
#  [ 5.7  2.8  4.5  1.3]
#  [ 5.5  2.5  4.   1.3]
#  [ 6.9  3.1  4.9  1.5]
#  [ 5.5  2.4  3.8  1.1]
#  [ 5.6  3.   4.1  1.3]
#  [ 5.1  3.5  1.4  0.3]
#  [ 5.1  3.8  1.5  0.3]
#  [ 5.5  2.3  4.   1.3]
#  [ 6.7  3.   5.   1.7]
#  [ 5.   3.5  1.3  0.3]
#  [ 4.8  3.4  1.6  0.2]
#  [ 5.   3.   1.6  0.2]
#  [ 4.4  3.2  1.3  0.2]
#  [ 4.6  3.6  1.   0.2]
#  [ 4.3  3.   1.1  0.1]
#  [ 5.1  3.8  1.9  0.4]
#  [ 5.8  2.7  4.1  1. ]
#  [ 4.6  3.4  1.4  0.3]
#  [ 4.9  3.   1.4  0.2]
#  [ 5.4  3.4  1.5  0.4]
#  [ 5.9  3.   4.2  1.5]
#  [ 5.   3.6  1.4  0.2]
#  [ 6.7  3.1  4.4  1.4]
#  [ 4.4  3.   1.3  0.2]
#  [ 5.6  3.   4.5  1.5]
#  [ 5.8  2.7  3.9  1.2]
#  [ 4.9  3.1  1.5  0.1]
#  [ 5.   3.3  1.4  0.2]
#  [ 4.6  3.1  1.5  0.2]
#  [ 5.7  4.4  1.5  0.4]
#  [ 6.3  2.5  4.9  1.5]
#  [ 6.6  2.9  4.6  1.3]
#  [ 5.1  3.7  1.5  0.4]
#  [ 5.2  3.4  1.4  0.2]
#  [ 5.   3.4  1.5  0.2]
#  [ 6.7  3.1  4.7  1.5]
#  [ 5.5  4.2  1.4  0.2]
#  [ 4.7  3.2  1.6  0.2]
#  [ 6.4  3.2  4.5  1.5]
#  [ 5.7  2.8  4.1  1.3]
#  [ 6.1  2.8  4.   1.3]
#  [ 5.7  2.6  3.5  1. ]
#  [ 5.4  3.4  1.7  0.2]
#  [ 6.6  3.   4.4  1.4]
#  [ 4.8  3.1  1.6  0.2]
#  [ 6.3  2.3  4.4  1.3]
#  [ 5.6  2.5  3.9  1.1]
#  [ 5.9  3.2  4.8  1.8]
#  [ 5.4  3.9  1.3  0.4]
#  [ 6.2  2.9  4.3  1.3]
#  [ 6.3  3.3  4.7  1.6]
#  [ 4.8  3.   1.4  0.3]]



# i :
# (5.0, 4.5999999999999996, 5.4000000000000004, 5.7000000000000002, 5.5, 5.0, 4.7000000000000002, 5.2999999999999998, 4.7999999999999998, 5.4000000000000004, 5.2000000000000002, 4.7999999999999998, 5.0999999999999996, 5.0999999999999996, 5.0, 4.7999999999999998, 5.0, 4.4000000000000004, 4.5999999999999996, 4.2999999999999998, 5.0999999999999996, 4.5999999999999996, 4.9000000000000004, 5.4000000000000004, 5.0, 4.4000000000000004, 4.9000000000000004, 5.0, 4.5999999999999996, 5.7000000000000002, 5.0999999999999996, 5.2000000000000002, 5.0, 5.5, 4.7000000000000002, 5.4000000000000004, 4.7999999999999998, 5.4000000000000004, 4.7999999999999998)
# i :
# (3.5, 3.2000000000000002, 3.7000000000000002, 3.7999999999999998, 3.5, 3.3999999999999999, 3.2000000000000002, 3.7000000000000002, 3.0, 3.8999999999999999, 3.5, 3.3999999999999999, 3.5, 3.7999999999999998, 3.5, 3.3999999999999999, 3.0, 3.2000000000000002, 3.6000000000000001, 3.0, 3.7999999999999998, 3.3999999999999999, 3.0, 3.3999999999999999, 3.6000000000000001, 3.0, 3.1000000000000001, 3.2999999999999998, 3.1000000000000001, 4.4000000000000004, 3.7000000000000002, 3.3999999999999999, 3.3999999999999999, 4.2000000000000002, 3.2000000000000002, 3.3999999999999999, 3.1000000000000001, 3.8999999999999999, 3.0)
# i :
# (1.6000000000000001, 1.3999999999999999, 1.5, 1.7, 1.3, 1.6000000000000001, 1.3, 1.5, 1.3999999999999999, 1.7, 1.5, 1.8999999999999999, 1.3999999999999999, 1.5, 1.3, 1.6000000000000001, 1.6000000000000001, 1.3, 1.0, 1.1000000000000001, 1.8999999999999999, 1.3999999999999999, 1.3999999999999999, 1.5, 1.3999999999999999, 1.3, 1.5, 1.3999999999999999, 1.5, 1.5, 1.5, 1.3999999999999999, 1.5, 1.3999999999999999, 1.6000000000000001, 1.7, 1.6000000000000001, 1.3, 1.3999999999999999)
# i :
# (0.59999999999999998, 0.20000000000000001, 0.20000000000000001, 0.29999999999999999, 0.20000000000000001, 0.40000000000000002, 0.20000000000000001, 0.20000000000000001, 0.10000000000000001, 0.40000000000000002, 0.20000000000000001, 0.20000000000000001, 0.29999999999999999, 0.29999999999999999, 0.29999999999999999, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.10000000000000001, 0.40000000000000002, 0.29999999999999999, 0.20000000000000001, 0.40000000000000002, 0.20000000000000001, 0.20000000000000001, 0.10000000000000001, 0.20000000000000001, 0.20000000000000001, 0.40000000000000002, 0.40000000000000002, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.40000000000000002, 0.29999999999999999)
#
#
# i :
# (5.7999999999999998, 6.2000000000000002, 5.5, 5.2000000000000002, 5.0999999999999996, 6.4000000000000004, 5.7000000000000002, 5.5, 6.9000000000000004, 5.5, 5.5999999999999996, 5.5, 6.7000000000000002, 5.7999999999999998, 5.9000000000000004, 6.7000000000000002, 5.5999999999999996, 5.7999999999999998, 6.2999999999999998, 6.5999999999999996, 6.7000000000000002, 6.4000000000000004, 5.7000000000000002, 6.0999999999999996, 5.7000000000000002, 6.5999999999999996, 6.2999999999999998, 5.5999999999999996, 5.9000000000000004, 6.2000000000000002, 6.2999999999999998)
# i :
# (2.6000000000000001, 2.2000000000000002, 2.6000000000000001, 2.7000000000000002, 2.5, 2.8999999999999999, 2.7999999999999998, 2.5, 3.1000000000000001, 2.3999999999999999, 3.0, 2.2999999999999998, 3.0, 2.7000000000000002, 3.0, 3.1000000000000001, 3.0, 2.7000000000000002, 2.5, 2.8999999999999999, 3.1000000000000001, 3.2000000000000002, 2.7999999999999998, 2.7999999999999998, 2.6000000000000001, 3.0, 2.2999999999999998, 2.5, 3.2000000000000002, 2.8999999999999999, 3.2999999999999998)
# i :
# (4.0, 4.5, 4.4000000000000004, 3.8999999999999999, 3.0, 4.2999999999999998, 4.5, 4.0, 4.9000000000000004, 3.7999999999999998, 4.0999999999999996, 4.0, 5.0, 4.0999999999999996, 4.2000000000000002, 4.4000000000000004, 4.5, 3.8999999999999999, 4.9000000000000004, 4.5999999999999996, 4.7000000000000002, 4.5, 4.0999999999999996, 4.0, 3.5, 4.4000000000000004, 4.4000000000000004, 3.8999999999999999, 4.7999999999999998, 4.2999999999999998, 4.7000000000000002)
# i :
# (1.2, 1.5, 1.2, 1.3999999999999999, 1.1000000000000001, 1.3, 1.3, 1.3, 1.5, 1.1000000000000001, 1.3, 1.3, 1.7, 1.0, 1.5, 1.3999999999999999, 1.5, 1.2, 1.5, 1.3, 1.5, 1.5, 1.3, 1.3, 1.0, 1.3999999999999999, 1.3, 1.1000000000000001, 1.8, 1.3, 1.6000000000000001)



print(X_test[0], y_test[0])
# [5.4 3.4 1.5 0.4] 0.0





class NaiveBayes:

    def __init__(self):
        self.model = None

    # 数学期望
    @staticmethod
    def mean(X):
        return sum(X) / float(len(X))

    # 标准差（方差）
    def stdev(self, X):
        avg = self.mean(X)
        return math.sqrt(sum([pow(x - avg, 2) for x in X]) / float(len(X)))

    # 概率密度函数
    def gaussian_probability(self, x, mean, stdev):
        exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
        return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent


    # 处理X_train
    def summarize(self, train_data):
        for i in zip(*train_data):
            print("i :\n{}".format(i))

        print("")
        print("")


        # 每次迭代数据不一致
        # i:
        # (4.7999999999999998, 5.0, 4.7999999999999998, 4.5999999999999996, 4.4000000000000004, 5.0, 5.0999999999999996,
        #  5.7999999999999998, 4.7000000000000002, 5.0, 5.2000000000000002, 5.0999999999999996, 4.7999999999999998,
        #  4.9000000000000004, 5.0, 5.4000000000000004, 5.5, 4.4000000000000004, 5.4000000000000004, 5.0,
        #  4.2999999999999998, 5.2000000000000002, 5.0, 5.2999999999999998, 5.2000000000000002, 4.7999999999999998,
        #  5.0999999999999996, 5.7000000000000002, 4.9000000000000004, 4.5999999999999996, 5.0)
        # i:
        # (3.0, 3.5, 3.0, 3.6000000000000001, 3.2000000000000002, 3.3999999999999999, 3.3999999999999999, 4.0,
        #  3.2000000000000002, 3.0, 3.5, 3.7999999999999998, 3.3999999999999999, 3.0, 3.3999999999999999,
        #  3.8999999999999999, 4.2000000000000002, 3.0, 3.8999999999999999, 3.2000000000000002, 3.0, 3.3999999999999999,
        #  3.2999999999999998, 3.7000000000000002, 4.0999999999999996, 3.1000000000000001, 3.5, 3.7999999999999998,
        #  3.1000000000000001, 3.3999999999999999, 3.5)
        # i:
        # (1.3999999999999999, 1.3, 1.3999999999999999, 1.0, 1.3, 1.5, 1.5, 1.2, 1.6000000000000001, 1.6000000000000001,
        #  1.5, 1.8999999999999999, 1.8999999999999999, 1.3999999999999999, 1.6000000000000001, 1.3, 1.3999999999999999,
        #  1.3, 1.7, 1.2, 1.1000000000000001, 1.3999999999999999, 1.3999999999999999, 1.5, 1.5, 1.6000000000000001,
        #  1.3999999999999999, 1.7, 1.5, 1.3999999999999999, 1.6000000000000001)
        # i:
        # (0.29999999999999999, 0.29999999999999999, 0.10000000000000001, 0.20000000000000001, 0.20000000000000001,
        #  0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001,
        #  0.20000000000000001, 0.40000000000000002, 0.20000000000000001, 0.20000000000000001, 0.40000000000000002,
        #  0.40000000000000002, 0.20000000000000001, 0.20000000000000001, 0.40000000000000002, 0.20000000000000001,
        #  0.10000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.10000000000000001,
        #  0.20000000000000001, 0.20000000000000001, 0.29999999999999999, 0.10000000000000001, 0.29999999999999999,
        #  0.59999999999999998)
        # i:
        # (6.5, 5.2000000000000002, 5.9000000000000004, 4.9000000000000004, 6.9000000000000004, 6.2000000000000002,
        #  5.7000000000000002, 5.7000000000000002, 5.5, 6.0, 5.5, 6.2999999999999998, 5.0999999999999996, 5.5,
        #  6.7000000000000002, 5.0, 5.9000000000000004, 5.0, 6.0999999999999996, 5.7000000000000002, 6.5999999999999996,
        #  6.7000000000000002, 6.0, 5.7000000000000002, 5.5999999999999996, 6.7000000000000002, 6.4000000000000004,
        #  5.5999999999999996, 5.5, 5.5999999999999996, 5.7999999999999998, 6.4000000000000004, 6.0, 6.0999999999999996,
        #  5.5999999999999996, 6.7999999999999998, 6.2000000000000002, 5.7999999999999998, 6.5999999999999996)
        # i:
        # (2.7999999999999998, 2.7000000000000002, 3.2000000000000002, 2.3999999999999999, 3.1000000000000001,
        #  2.8999999999999999, 2.7999999999999998, 3.0, 2.3999999999999999, 2.2000000000000002, 2.3999999999999999, 2.5,
        #  2.5, 2.5, 3.1000000000000001, 2.2999999999999998, 3.0, 2.0, 3.0, 2.7999999999999998, 2.8999999999999999,
        #  3.1000000000000001, 2.7000000000000002, 2.8999999999999999, 2.5, 3.0, 3.2000000000000002, 2.7000000000000002,
        #  2.2999999999999998, 3.0, 2.7000000000000002, 2.8999999999999999, 3.3999999999999999, 2.7999999999999998, 3.0,
        #  2.7999999999999998, 2.2000000000000002, 2.7000000000000002, 3.0)
        # i:
        # (4.5999999999999996, 3.8999999999999999, 4.7999999999999998, 3.2999999999999998, 4.9000000000000004,
        #  4.2999999999999998, 4.0999999999999996, 4.2000000000000002, 3.7000000000000002, 4.0, 3.7999999999999998,
        #  4.9000000000000004, 3.0, 4.0, 4.4000000000000004, 3.2999999999999998, 4.2000000000000002, 3.5,
        #  4.5999999999999996, 4.5, 4.5999999999999996, 4.7000000000000002, 5.0999999999999996, 4.2000000000000002,
        #  3.8999999999999999, 5.0, 4.5, 4.2000000000000002, 4.0, 4.0999999999999996, 3.8999999999999999,
        #  4.2999999999999998, 4.5, 4.0, 4.5, 4.7999999999999998, 4.5, 4.0999999999999996, 4.4000000000000004)
        # i:
        # (1.5, 1.3999999999999999, 1.8, 1.0, 1.5, 1.3, 1.3, 1.2, 1.0, 1.0, 1.1000000000000001, 1.5, 1.1000000000000001,
        #  1.3, 1.3999999999999999, 1.0, 1.5, 1.0, 1.3999999999999999, 1.3, 1.3, 1.5, 1.6000000000000001, 1.3,
        #  1.1000000000000001, 1.7, 1.5, 1.3, 1.3, 1.3, 1.2, 1.3, 1.6000000000000001, 1.3, 1.5, 1.3999999999999999, 1.5,
        #  1.0, 1.3999999999999999)


        summaries = [(self.mean(i), self.stdev(i)) for i in zip(*train_data)]
        # print("summaries : \n{}".format(summaries))
        # print("")
        return summaries


    # 分类别求出数学期望和标准差
    def fit(self, X, y):

        labels = list(set(y))
        print("labels : \n{}".format(labels))
        print("")
        # labels:
        # [0.0, 1.0]


        data = {label:[] for label in labels}
        print("data : \n{}".format(data))
        print("")
        # data:
        # {0.0: [], 1.0: []}



        for f, label in zip(X, y):
            data[label].append(f)
        print("After process data: \n{}".format(data))
        print("")
        # After
        # process
        # data:
        # {0.0: [array([5.1, 3.4, 1.5, 0.2]), array([5.4, 3.7, 1.5, 0.2]), array([5.4, 3.9, 1.7, 0.4]),
        #        array([4.4, 2.9, 1.4, 0.2]), array([5.2, 3.4, 1.4, 0.2]), array([5.1, 3.7, 1.5, 0.4]),
        #        array([5., 3.2, 1.2, 0.2]), array([4.9, 3.1, 1.5, 0.1]), array([5., 3.3, 1.4, 0.2]),
        #        array([4.7, 3.2, 1.3, 0.2]), array([4.7, 3.2, 1.6, 0.2]), array([5.3, 3.7, 1.5, 0.2]),
        #        array([5.4, 3.9, 1.3, 0.4]), array([5.5, 3.5, 1.3, 0.2]), array([5.1, 3.5, 1.4, 0.3]),
        #        array([4.9, 3.1, 1.5, 0.1]), array([5.1, 3.5, 1.4, 0.2]), array([4.8, 3.4, 1.6, 0.2]),
        #        array([4.6, 3.4, 1.4, 0.3]), array([5.2, 3.5, 1.5, 0.2]), array([4.6, 3.1, 1.5, 0.2]),
        #        array([5.7, 3.8, 1.7, 0.3]), array([4.8, 3.1, 1.6, 0.2]), array([4.8, 3., 1.4, 0.3]),
        #        array([4.5, 2.3, 1.3, 0.3]), array([5., 3.4, 1.6, 0.4]), array([4.9, 3., 1.4, 0.2]),
        #        array([5., 3.5, 1.3, 0.3]), array([4.8, 3., 1.4, 0.1]), array([4.9, 3.1, 1.5, 0.1]),
        #        array([4.6, 3.2, 1.4, 0.2])],
        #  1.0: [array([5.5, 2.5, 4., 1.3]), array([5.7, 2.8, 4.5, 1.3]), array([7., 3.2, 4.7, 1.4]),
        #        array([5.1, 2.5, 3., 1.1]), array([5.8, 2.7, 4.1, 1.]), array([5.6, 3., 4.5, 1.5]),
        #        array([5.7, 3., 4.2, 1.2]), array([5.9, 3.2, 4.8, 1.8]), array([6.3, 2.5, 4.9, 1.5]),
        #        array([5.6, 3., 4.1, 1.3]), array([5.5, 2.4, 3.7, 1.]), array([6.6, 3., 4.4, 1.4]),
        #        array([5.6, 2.5, 3.9, 1.1]), array([6.1, 2.9, 4.7, 1.4]), array([6.1, 3., 4.6, 1.4]),
        #        array([6.3, 3.3, 4.7, 1.6]), array([6.7, 3.1, 4.4, 1.4]), array([5.7, 2.6, 3.5, 1.]),
        #        array([5.9, 3., 4.2, 1.5]), array([5.8, 2.7, 3.9, 1.2]), array([6.7, 3., 5., 1.7]),
        #        array([6.1, 2.8, 4.7, 1.2]), array([6.4, 3.2, 4.5, 1.5]), array([6., 2.2, 4., 1.]),
        #        array([5.2, 2.7, 3.9, 1.4]), array([6., 2.7, 5.1, 1.6]), array([5.8, 2.6, 4., 1.2]),
        #        array([6., 3.4, 4.5, 1.6]), array([6.7, 3.1, 4.7, 1.5]), array([6.2, 2.9, 4.3, 1.3]),
        #        array([5.6, 2.7, 4.2, 1.3]), array([6., 2.9, 4.5, 1.5]), array([5.4, 3., 4.5, 1.5]),
        #        array([5., 2.3, 3.3, 1.]), array([5.6, 2.9, 3.6, 1.3]), array([6.4, 2.9, 4.3, 1.3]),
        #        array([4.9, 2.4, 3.3, 1.]), array([5., 2., 3.5, 1.]), array([5.5, 2.3, 4., 1.3])]}

        print("")
        for label, value in data.items():
            print("label : {},value:  {}".format(label,value))


        print("")

        self.model = {label: self.summarize(value) for label, value in data.items()}
        print("Model : \n{}".format(self.model))
        print("")
        # Model:
        # 对应每个维度的均值和方差
        # {0.0: [(4.9806451612903224, 0.3052437997982868), (3.3225806451612905, 0.32893736772135623),
        #        (1.4516129032258063, 0.11878679122272243), (0.23225806451612904, 0.08571180810055758)],
        #  1.0: [(5.8717948717948714, 0.4997172112862962), (2.7923076923076926, 0.31815543321530465),
        #        (4.2230769230769241, 0.49170636352298114), (1.3230769230769228, 0.21178307535286467)]}

        return 'gaussianNB train done!'

    # 计算概率
    def calculate_probabilities(self, input_data):
        # summaries:{0.0: [(5.0, 0.37),(3.42, 0.40)], 1.0: [(5.8, 0.449),(2.7, 0.27)]}
        # input_data:[1.1, 2.2]
        probabilities = {}
        for label, value in self.model.items():
            probabilities[label] = 1

            for i in range(len(value)):
                mean, stdev = value[i]
                probabilities[label] *= self.gaussian_probability(input_data[i], mean, stdev)
                print("")
                print("probabilities[label] : \n{}".format(probabilities[label]))
                print("")
        print("")
        print("probabilities: \n{}".format(probabilities))
        print("")
        return probabilities


    # 类别
    def predict(self, X_test):
        # {0.0: 2.9680340789325763e-27, 1.0: 3.5749783019849535e-26}
        print("sorted(self.calculate_probabilities(X_test).items(), key=lambda x: x[-1]):\n{}".format(sorted(self.calculate_probabilities(X_test).items(), key=lambda x: x[-1])))
        label = sorted(self.calculate_probabilities(X_test).items(), key=lambda x: x[-1])[-1][0]
        return label

    def score(self, X_test, y_test):
        right = 0
        for X, y in zip(X_test, y_test):
            label = self.predict(X)
            if label == y:
                right += 1

        return right / float(len(X_test))




model = NaiveBayes()

model.fit(X_train, y_train)

print(model.predict([4.4,  3.2,  1.3,  0.2]))

print("Score : \n{}".format(model.score(X_test, y_test)))
































































