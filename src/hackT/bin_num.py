#!/bin/python3

""" Day 10: Binary Numbers"""


import os
import random
import re



def getMaxConsectiveOnes(bin_n):
    currMax = 0
    currCount = 0

    for i in bin_n:
        if i == '1':
            currCount += 1
        else:
            if currMax < currCount:
                currMax = currCount
            currCount = 0

    #if number ends with 1
    if currMax < currCount:
        currMax = currCount

    return currMax

if __name__ == '__main__':
    n = int(input())

    bin_n = bin(n)[2:]

    print(getMaxConsectiveOnes(bin_n))

