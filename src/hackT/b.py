""" Lisa's Workbook"""

def workbook(n, k, arr):
    currPage = 1
    retVal = 0

    for currChapter in range(n):
        currPgProblemIdx, lastPgProblemIdx = 0, 0
        while currPgProblemIdx < arr[currChapter]:
            lastPgProblemIdx = currPgProblemIdx
            currPgProblemIdx += k

            if currPgProblemIdx > arr[currChapter]:
                currPgProblemIdx = arr[currChapter]

            if currPgProblemIdx >= currPage and lastPgProblemIdx < currPage:
                retVal += 1

            print(f'{currPgProblemIdx}:{currPage}:{currChapter}:{retVal}')            

            currPage += 1                


    return retVal


n = 5 #chapters
k = 3 #max. problems
arr = [4, 2, 6, 1, 18]

print(workbook(n, k, arr))