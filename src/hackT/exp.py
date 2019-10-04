""" Day 16: Exceptions - String to Integer """

a = '12'

res = 0

try:
    res = int(a)
    print(res)    
except ValueError:
    print('Bad String')


