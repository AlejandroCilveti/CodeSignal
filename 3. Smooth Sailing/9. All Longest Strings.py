def repeatedMax(length, maxi):
    repeated = []
    for i in range(0, len(length)):
        if length[i] == maxi:
            repeated.append(i)
    return repeated


def getLength(inputArray):
    length = []
    for i in range(0, len(inputArray)):
        length.append(len(inputArray[i]))
    return length


def allLongestStrings(inputArray):
    maxi = []
    length = getLength(inputArray)
    maxi = max(length)
    final = []
    repeated = repeatedMax(length, maxi)

    for i in range(0, len(repeated)):
        final.append(inputArray[repeated[i]])

    return final
