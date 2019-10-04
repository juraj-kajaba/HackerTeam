""" Day 11: 2D Arrays test"""

from hackT import hourglass

arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]


def test_getHourglassMaxSum():
    global arr
    assert hourglass.getHourglassMaxSum(arr) == 19

