""" Day 20: Sorting """

from hackT import bubble_sort

def test_1():
    a = [2, 3, 4, 1]

    n, r = bubble_sort.bubbleSort(a)

    assert n == 3
    assert r == [1, 2, 3, 4]

def test_2():
    a = [3, 2, 1]

    n, r = bubble_sort.bubbleSort(a)

    assert n == 3
    assert r == [1, 2, 3]
