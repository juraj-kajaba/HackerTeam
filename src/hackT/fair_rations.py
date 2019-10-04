""" Fair Rations """

def fairRations(B):
    a = list(B)
    given = 0

    for i in range(1, len(a)):
        if a[i-1] % 2 != 0:
            a[i] += 1
            a[i-1] += 1        
            given += 2

    # if sum all elements is odd value -> result is NO
    if sum(a) % 2 != 0:
        return "NO"
    else:
        return given



a = [2, 4, 2, 3, 3, 3, 4, 3, 4, ]

#print(a)
print(fairRations(a))
