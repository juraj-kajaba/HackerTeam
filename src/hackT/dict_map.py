"""Day 8: Dictionaries and Maps"""

if __name__ == '__main__':
    phoneNums = {}

    n = int(input())

    for i in range(n):
        arr = list(map(str, input().rstrip().split()))
        phoneNums[arr[0]] = arr[1]

    try:
        while(True):
            q = input()

            if q == '':
                break
            else:
                if q in phoneNums:
                    print(f'{q}={phoneNums[q]}')
                else:
                    print('Not found')
    except EOFError as e:
        print(end="")                    

            

