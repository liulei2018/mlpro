from math import log


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

    #计算香农熵
    for key in typeDic:
        prob = float(typeDic[key])/len(dataSet)
        ent -= prob * log(prob,2)
    return ent

if __name__ == "__main__":
    dataSet , labels = createDataSet()
    print(calcShannonEnt(dataSet))
