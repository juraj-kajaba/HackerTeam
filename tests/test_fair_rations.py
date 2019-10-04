""" Fair Rations test """ 

from hackT import fair_rations


def test_1():
    a = [2, 3, 4, 5, 6]

    assert fair_rations.fairRations(a) == 4


def test_2():
    a = [4, 5, 6, 7]

    assert fair_rations.fairRations(a) == 4

def test_3():
    a = [1, 2]

    assert fair_rations.fairRations(a) == "NO"

def test_4():
    a = [2, 4, 2, 3, 3, 3, 4, 3, 4, 3]

    assert fair_rations.fairRations(a) == "NO"

def test_5():
    a = [2, 4, 2, 3, 3, 3, 4, 3, 4]

    assert fair_rations.fairRations(a) == 6
