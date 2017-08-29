from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
import sklearn


def createData():
    labels = ['A', 'A', 'B', 'B']
    dataSet = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    return dataSet, labels


def classfy0(intX, dataSet, labels, k):
    distance = hstack(list(map(lambda x: ((intX - x) ** 2).sum(axis=0) ** 0.5, dataSet)))
    distanceArgSort = distance.argsort()
    arr = {}
    for i in range(k):
        distanceArgSort[i]
        labels[distanceArgSort[i]]
        # arr[labels[distanceArgSort[i]]]
        arr[labels[distanceArgSort[i]]] = arr.get(labels[distanceArgSort[i]], 0) + 1

    arr = sorted(arr.items(), key=operator.itemgetter(1), reverse=True)
    return arr[0][0]


def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    l = list(map(lambda x: x.strip().split("\t"), arrayOLines))
    retMat = double(vstack(l)[:, 0:3])
    labels = double(transpose(vstack(l)[:, -1:])[0])
    return labels, retMat

    # for i in range(numberOfLines):


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = shape(dataSet)[0]
    diffVals = dataSet - tile(minVals, (m, 1))
    normDataSet = diffVals / tile(ranges, (m, 1))
    return normDataSet, minVals, ranges


def datingClassTest():
    hoRatio = 0.1
    labels, dataSet = file2matrix("D:\opensource\machinelearninginaction\Ch02\datingTestSet2.txt")
    normDataSet, minVals, ranges = autoNorm(dataSet)
    m = normDataSet.shape[0]
    numTestvecs = int(m * hoRatio)
    errorCount = 0
    for i in range(numTestvecs):
        classfierResult = classfy0(normDataSet[i, :], normDataSet[numTestvecs:-1], labels[numTestvecs:-1], 3)
        print("the classifier came back with:%d,the real answer is: %d" % (classfierResult, labels[i]))
        if (classfierResult != labels[i]): errorCount +=1

    print("the total error rate is: %f " %(errorCount/float(numTestvecs)))


if __name__ == "__main__":
    # labels, dataSet = file2matrix("D:\opensource\machinelearninginaction\Ch02\datingTestSet2.txt")
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.scatter(dataSet[:, 1], dataSet[:, 2], 15 * labels, 15 * labels)
    # plt.show()
    # # dataSet,labels= createData()
    intX = array([3, 4, 23])
    xx = intX.shape
    # print(classfy0(intX, dataSet, labels, 3))
    #
    # normDataSet, minVals, ranges = autoNorm(dataSet)
    # print(normDataSet, minVals, ranges)
    datingClassTest()
