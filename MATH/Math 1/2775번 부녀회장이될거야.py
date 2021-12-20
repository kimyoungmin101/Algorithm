


        

T = int(input())

for i in range(T):
    
    k = int(input())
    n = int(input())

    arr = [[0 for i in range(n)] for row in range(k+1)]

    count = 1

    for i in range(n):
        arr[0][i] = count
        count += 1
        
    for q in range(k+1):
        arr[q][0] = 1


    for i in range(1, len(arr)):
        for j in range(1, len(arr[i])):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]

    print(arr[k][n-1])
