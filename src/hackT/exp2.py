""" Day 17: More Exceptions """

a = '12'

res = 0

try:
    res = int(a)
    print(res)    
except ValueError:
    print('Bad String')



#Write your code here
class Calculator:
    def __init__(self):
        pass

    def power(self, n, p):
        if n < 0 or p < 0:
            raise Exception('n and p should be non-negative') 
        return n ** p

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
