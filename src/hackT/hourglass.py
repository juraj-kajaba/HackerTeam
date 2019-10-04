"""Day 11: 2D Arrays"""



def getHourglassSum(arr, startRow, startCol):
    """ Returns sum of hourglass in arr matrix stating at [startRow, startCol] position (zero based indices)
        Return value is None where hourglass is not possible to construct
    """
    retVal = 0

    if startRow > 3 or startCol > 3:
        return None

    for i in range(3):
        retVal += arr[startRow][startCol + i]

    retVal += arr[startRow + 1][startCol + 1]

    for i in range(3):
        retVal += arr[startRow + 2][startCol + i]

    return retVal

def getHourglassMaxSum(arr):
    maxSum = -9 * 8 # No more then 7 of -9 can be in matrix as hourglass

    for row in range(6):
        for col in range(6):
            rv = getHourglassSum(arr, row, col)
            if rv != None:
                if rv > maxSum:
                    maxSum = rv
    
    return maxSum

#print(getHourglassMaxSum(arr))

