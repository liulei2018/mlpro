from numpy import *
import operator


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
        arr[labels[distanceArgSort[i]]]= arr.get(labels[distanceArgSort[i]], 0) + 1

    arr = sorted(arr.items(), key=operator.itemgetter(1), reverse=True)
    return arr[0][0]


def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    l = list(map(lambda x: x.strip().split("\t"), arrayOLines))
    retMat = double(vstack(l)[:, 0:3])
    labels = transpose(vstack(l)[:, -1:])[0]
    return labels , retMat

    # for i in range(numberOfLines):


if __name__ == "__main__":
    labels, dataSet = file2matrix("D:\opensource\machinelearninginaction\Ch02\datingTestSet.txt")
    # dataSet,labels= createData()
    intX = array([3,4,23])
    print(classfy0(intX,dataSet,labels,3))
