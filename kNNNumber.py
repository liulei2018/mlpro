from numpy.matlib import zeros, array
from os import listdir

from kNN import classfy0


def img2vector(filename):
    returnvector = zeros((1, 1024))
    file = open(filename)
    for i in range(32):
        readmat = list(file.readline().strip("\n"))
        print(readmat)
        print(returnvector[0, i * 32:(i + 1) * 32])
        returnvector[0, i * 32:(i + 1) * 32] = array(readmat, dtype=int)
        print(returnvector[0, i * 32:(i + 1) * 32])

    for i in range(1024):
        print(returnvector[0, i:i + 1])

    return returnvector


def trainDataTest():
    traindir = "D:\\opensource\\machinelearninginaction\\Ch02\\digits\\trainingDigits\\"
    textdir = "D:\\opensource\\machinelearninginaction\\Ch02\digits\\testDigits\\"
    traintexts = listdir(traindir)
    print(traintexts)
    testtexts = listdir(textdir)
    trainfilecount = len(traintexts)
    traindata = ""
    errcount = 0
    count = 0
    for traintext in traintexts:
        file = open(traindir + traintext)
        # matline = "".join(list(map(lambda x : x.replace("\n",""),file.readlines())))
        fr = file.readlines()
        traindata += "".join(fr).replace("\n", "")

    trainMat = array(list(traindata), int).reshape(-1, 1024)
    for testtext in testtexts:
        count += 1
        file = open(textdir + testtext)
        # matline = "".join(list(map(lambda x : x.replace("\n",""),file.readlines())))
        fr = file.readlines()
        textdata = array(list("".join(fr).replace("\n", "")), int).reshape(1024, )
        x = textdata.shape
        m = classfy0(textdata, trainMat, traintexts, 3)
        if m.split("_")[0] != testtext.split("_")[0]:
            errcount += 1
            print("nomatch", m, testtext, )

    print(count)
    print(errcount)
    # for()


if __name__ == "__main__":
    # img2vector("D:\opensource\machinelearninginaction\Ch02\digits\\testDigits\\0_25.txt")
    trainDataTest()
