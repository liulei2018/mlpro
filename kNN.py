from os import listdir

from numpy import *
from matplotlib import *
import matplotlib.pyplot as plt
import operator


def createDataset():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classfy0(intX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(intX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqlDistance = sqDiffMat.sum(axis=1)
    distances = sqlDistance ** 0.5
    sortedDisIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlable = labels[sortedDisIndicies[i]]
        classCount[voteIlable] = classCount.get(voteIlable, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    sortedClassCount[0]
    return sortedClassCount[0][0]


def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())
    returnMat = zeros((numberOfLines, 3))
    classLabVector = []
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        # classLabVector.append(int(listFromLine[-1]))
        classLabVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabVector


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix("D:\opensource\machinelearninginaction\Ch02\datingTestSet2.txt")
    print(datingDataMat)
    print(datingLabels)
    norMat, ranges, minVals = autoNorm(datingDataMat)
    m = norMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0

    for i in range(numTestVecs):
        classifierResult = classfy0(norMat[i, :], norMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print("the classfier came back with :%d ,the real answer is : %d " % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1.0

    print("the total error is %f " % (errorCount / float(numTestVecs)))
    listdir('ad')


if __name__ == "__main__":
    groupbl, labels = createDataset()
    # print(2323)
    # print(classfy0([0, 0], groupbl, labels, 3))
    # datingDataMat, datingLabels = file2matrix("D:\opensource\machinelearninginaction\Ch02\datingTestSet2.txt")
    # print(datingDataMat)
    # print(datingLabels[0:20])
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2],15.0 * array(datingLabels), 11.0 * array(datingLabels))
    #  # 15.0 * array(datingLabels), 15.0 * array(datingLabels)
    # plt.show()

    # datingClassTest()
