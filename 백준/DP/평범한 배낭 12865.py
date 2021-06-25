N, K = map(int, input().split())

arr = []

DP = [[0] * (K+1) for _ in range(N+1)]

for i in range(N):
    W, V = map(int, input().split())
    arr.append([W, V])

#표그려서해보깅

arr = sorted(arr, key = lambda x : x[0])

for i in range(1, N+1):
    for j in range(1, K+1):
        if(arr[i-1][0] <= j):
            DP[i][j] = max(DP[i-1][j], arr[i-1][1] + DP[i-1][j - arr[i-1][0]])
        else:
            DP[i][j] = DP[i-1][j]
            
print(DP[-1][-1])    
'''
4 7
6 13
4 8
3 6
5 12
'''
