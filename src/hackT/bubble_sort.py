""" Day 20: Sorting """


def bubbleSort(a):
    totalSwaps = 0

    for _ in range(len(a)):

        isSwap = False

        # Iterate whole array and do all needed swaps
        for j in range(1, len(a)):
            if a[j - 1] > a[j]:
                a[j], a[j - 1] = a[j - 1], a[j] # do swap
                isSwap = True
                totalSwaps += 1

        if not isSwap:
            break

    return totalSwaps, a

    
