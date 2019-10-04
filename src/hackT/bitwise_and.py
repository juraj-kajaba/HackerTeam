""" Day 29: Bitwise AND """


def getMax(N:int, K:int) -> int:
    currMax = 0

    for A in range(1, N+1):
        for B in range(A+1, N+1):
            m = A & B
            if m < K and m > currMax:
                currMax = m
                if currMax == K-1: #shortcut hence greater max cannot be found
                    return currMax 
    
    return currMax


t = int(input())
out = []

for t_itr in range(t):
    nk = input().split()

    n = int(nk[0])
    k = int(nk[1])

    out.append(getMax(n, k))

for o in out:
    print(o)