""" Day 26: Nested Logic test """

from hackT import nested

def test_1():           
    assert nested.getFine(6, 6, 2015, 9, 6, 2015) == 45


# act = list(map(int, input().split(' ')))
# due = list(map(int, input().split(' ')))

# print(nested.getFine(due[0], due[1], due[2], act[0], act[1], act[2]))
