"""Magic square"""

def formingMagicSquare(s):
    """ There are a couple of possible magic squeres. Principle is to count the cost of converting to each of them and
        return the minimal one. """
    
    allMagicSquares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        ]

    
    minCost = 99999

    #iterate over all predefined matrices
    for m in range(len(allMagicSquares)):
        totalCost = 0 #total cost of ona matrix
        #iterate over all rows of matrices
        for row in range(len(allMagicSquares[m])):        
            zippedRow = zip(allMagicSquares[m][row],s[row])
            #print(list(zippedRow))
            #compute cost of one row
            for c in zippedRow:
               totalCost += abs(c[0] - c[1]) 
               #print(f'{c[0]}:{c[1]}')
        #print(totalCost)
        if totalCost < minCost:
            minCost = totalCost
        #break # only to debug one matrix

    return minCost

s = [
    [4, 8, 2],
    [4, 5, 7],
    [6, 1, 6]
] # returns 4

s2 = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 5]
] # returns 1


print(formingMagicSquare(s))    
print(formingMagicSquare(s2))    
