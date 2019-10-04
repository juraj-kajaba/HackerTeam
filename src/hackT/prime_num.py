""" Day 25: Running Time and Complexity """

import math
from itertools import count

def isPrime1(possiblePrime):
    if possiblePrime <= 1:
        return False

    # Assume number is prime until shown it is not. 
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False
            break
    
    return isPrime


def isPrime2(possiblePrime):
    """
    To explain why this approach works, it is important to note a few things. 
    A composite number is a positive number greater than 1 that is not prime 
    (which has factors other than 1 and itself). 
    Every composite number has a factor less than or equal to its square root.
    """
    if possiblePrime <= 1:
        return False

      # Assume number is prime until shown it is not. 
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
            break

    return isPrime



def primes_lazy_sieve():
    """
    To implement a lazy sieve as described by Prof. O’Neill we use the general idea of the 
    classic sieve of Eratosthenes algorithm, but whereas the classic sieve removes all 
    multiples of all the primes already discovered from a given starting set the lazy 
    sieve tries to do as little work upfront as possible. The algorithm keeps a map where 
    the values are (maybe empty) lists of prime numbers and the key of such list is the number 
    that is the next one divisible by the primes in the list. In other words, it maps from numbers 
    to their prime factors. This map starts out empty as we don’t know any prime numbers yet.    
    """
    multiples = {}
    for candidate in count(2):
        candidate_divisors = multiples.pop(candidate, None)
        if candidate_divisors is None:
            yield candidate
            multiples[candidate * candidate] = [candidate]
        else:
            # upfront generation of number witch can be composed of divisors and
            # therefore cannot be prime numbers
            for divisor in candidate_divisors:
                multiples.setdefault(candidate + divisor, []).append(divisor)


# n = int(input())
# arr =[]

# for _ in range(n):
#     i = int(input())
#     arr.append(i)

# for i in arr:
#     if isPrime2(i):
#         print("Prime")
#     else:
#         print("Not prime")


# for i,val in enumerate(primes_lazy_sieve()):
#     print(val)
#     if i == 10:
#         break

