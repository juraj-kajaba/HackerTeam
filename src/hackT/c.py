
def diagonalDifference(arr):
    lrIdx, rlIdx  = 0, len(arr) - 1
    lrSum, rlSum  = 0, 0

    for row in range(len(arr)):
        lrSum += arr[row][lrIdx]
        rlSum += arr[row][rlIdx]        
        lrIdx += 1
        rlIdx -= 1

    return abs(lrSum - rlSum)

arr = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

def test_answer():
    assert diagonalDifference(arr) == 15

