from math import log
import operator


def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


def calcShannonEnt(dataSet):
    typeDic = {}
    ent = 0.0
    for data in dataSet:
        type = data[-1]
        if type not in typeDic.keys():
            typeDic[type] = 0
        typeDic[type] += 1

    # 计算香农熵
    for key in typeDic:
        prob = float(typeDic[key]) / len(dataSet)
        ent -= prob * log(prob, 2)
    return ent


def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        # print(featVec[:axis])
        # print(featVec[:1])
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    # print(baseEntropy)
    baseInfoGain = 0.0
    baseFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        bestFeature = -1
        # print(uniqueVals)
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            # print(dataSet,subDataSet)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
            print(newEntropy)
        infoGain = baseEntropy - newEntropy
        if (infoGain > baseInfoGain):
            baseInfoGain = infoGain
            baseFeature = i
    return baseFeature


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] != 1

    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if (classList.count(classList[0]) == len(classList)):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del (labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueValues = set(featValues)
    for value in uniqueValues:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


if __name__ == "__main__":
    dataSet, labels = createDataSet()
    # print(calcShannonEnt(dataSet))
    # splitDataSet(dataSet, 0, 1)
    # splitDataSet(dataSet, 0, 0)
    # print(chooseBestFeatureToSplit(dataSet))
    print(dataSet)
    print("       asdfadsf")
    # print(majorityCnt(dataSet))
    print(createTree(dataSet, labels))
