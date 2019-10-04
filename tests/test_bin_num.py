""" Day 10: Binary Numbers test"""

from hackT import bin_num

def test_getMaxConsectiveOnes():
    assert bin_num.getMaxConsectiveOnes(bin(13)[2:]) == 2


def test_getMaxConsectiveOnes_tc2():
    assert bin_num.getMaxConsectiveOnes(bin(2002)[2:]) == 5

def test_getMaxConsectiveOnes_tc3():
    assert bin_num.getMaxConsectiveOnes(bin(9999)[2:]) == 4

def test_getMaxConsectiveOnes_tc4():
    assert bin_num.getMaxConsectiveOnes(bin(99999)[2:]) == 5

def test_getMaxConsectiveOnes_tc5():
    assert bin_num.getMaxConsectiveOnes(bin(124587)[2:]) == 4

    
