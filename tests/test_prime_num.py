""" Day 25: Running Time and Complexity test """

from hackT import prime_num

def test_1():
    assert prime_num.isPrime2(1223) == True
    assert prime_num.isPrime2(1224) == False
    assert prime_num.isPrime2(13459) == False
    assert prime_num.isPrime2(13457) == True            

