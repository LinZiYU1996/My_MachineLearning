# -*- coding: utf-8 -*-

# @Time  : 2019/12/8 15:44

# @Author : Mr.Lin


from math import log


# 计算信息熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)  # 样本数
    labelCounts = {}
    for featVec in dataSet:  # 遍历每个样本
        currentLabel = featVec[-1]  # 当前样本的类别
        if currentLabel not in labelCounts.keys():  # 生成类别字典
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:  # 计算信息熵
        prob = float(labelCounts[key]) / numEntries
        shannonEnt = shannonEnt - prob * log(prob, 2)
    return shannonEnt


# 划分数据集，axis:按第几个属性划分，value:要返回的子集对应的属性值
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    featVec = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


# 选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet):
    print(dataSet)
    numFeatures = len(dataSet[0]) - 1  # 属性的个数
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):  # 对每个属性技术信息增益
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)  # 该属性的取值集合
        newEntropy = 0.0
        for value in uniqueVals:  # 对每一种取值计算信息增益
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):  # 选择信息增益最大的属性
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

import operator  # 此行加在文件顶部


# 通过排序返回出现次数最多的类别
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(),
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


# 递归构建决策树
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]  # 类别向量
    if classList.count(classList[0]) == len(classList):  # 如果只有一个类别，返回
        return classList[0]
    if len(dataSet[0]) == 1:  # 如果所有特征都被遍历完了，返回出现次数最多的类别
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)  # 最优划分属性的索引
    print(bestFeat)
    bestFeatLabel = labels[bestFeat]  # 最优划分属性的标签
    myTree = {bestFeatLabel: {}}
    del (labels[bestFeat])  # 已经选择的特征不再参与分类
    featValues = [example[bestFeat] for example in dataSet]
    uniqueValue = set(featValues)  # 该属性所有可能取值，也就是节点的分支
    for value in uniqueValue:  # 对每个分支，递归构建树
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(
            splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


# -*- coding: cp936 -*-
# import trees
import json

fr = open(r'watermalon.txt',encoding='UTF-8')

listWm = [inst.strip().split('\t') for inst in fr.readlines()]
print(listWm)
labels = ['色泽', '根蒂', '敲声', '纹理', '脐部', '触感']
Trees = createTree(listWm, labels)

print(json.dumps(Trees, encoding="UTF-8", ensure_ascii=False))





