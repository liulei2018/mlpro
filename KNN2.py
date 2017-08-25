from numpy import *
import operator


def createData():
    labels = ['A', 'A', 'B', 'B']
    dataSet = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    return dataSet, labels


def classfy2(intX, dataSet, labels, k):
    distance = hstack(list(map(lambda x: ((intX - x) ** 2).sum(axis=0) ** 0.5, dataSet)))
    distanceArgSort = distance.argsort()
    arr = {}
    for i in range(k):
        arr[labels[distanceArgSort[i]]] = arr.get(labels[distanceArgSort[i]], 0) + 1

    arr = sorted(arr.items(),key = operator.itemgetter(1),reverse=True)
    return arr[0][0]


if __name__ == "__main__":
    labels, dataSet = createData()
    print(classfy2(array([1, 2]), labels, dataSet, 3))
