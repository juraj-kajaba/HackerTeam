""" Day 29: Bitwise AND test """

from hackT import bitwise_and

def test_1():           
    arr = [
        (5, 2),
        (8, 5),
        (2, 2)        
    ]

    out = []
    for i in arr:
        out.append(bitwise_and.getMax(i[0], i[1]))

    assert out == [1, 4, 0]


test_1()

