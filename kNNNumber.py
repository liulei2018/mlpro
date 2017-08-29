from numpy.matlib import zeros, array


def img2vector(filename):
    returnvector= zeros((1,1024))
    file = open(filename)
    for i in range(32):
        readmat = file.readline().split("")
        print(readmat)
        print(returnvector[0,i*32:(i+1)*32] )
        returnvector[0,i*32:(i+1)*32] = readmat
        print(returnvector[0,i*32:(i+1)*32] )

    for i in range(1024):
        print(returnvector[0,i:i+1])


    return returnvector





if __name__ == "__main__":
    img2vector("D:\opensource\machinelearninginaction\Ch02\digits\\testDigits\\0_25.txt")