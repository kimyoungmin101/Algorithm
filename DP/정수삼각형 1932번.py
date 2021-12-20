N = int(input())

dp = [[0] * (i+1) for i in range(N)]
arr = []
for i in range(N):
    Q = list(map(int, input().split()))
    arr.append(Q)


dp[0] = arr[0]

for i in range(1, N):
    for j in range(len(dp[i])):
        if(j == 0):
            dp[i][j] = arr[i][j] + dp[i-1][j]
        elif(j == (len(dp[i])-1)):
            dp[i][j] = arr[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j] + arr[i][j], dp[i-1][j-1] + arr[i][j])
            
print(max(dp[-1]))
