a = [1, 2, 5]
mx = 0

for i in range(len(a)):
    for j in range(i, len(a)):
        print(f'{i}:{j}')
        df = abs(a[i] - a[j])
        if df > mx:
            mx = df

print(mx)            
