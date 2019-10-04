""" Day 7:Arrays"""

def getReversedArray(arr):
    """ Returns input array in reversed order """
    retVal = []
    for i in range(len(arr) - 1, -1, -1):
        retVal.append(arr[i])

    return retVal

