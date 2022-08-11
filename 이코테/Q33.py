# 퇴사

N = int(input())

arr = []
dp = []

for i in range(N):
    arr.append(list(map(int, input().split())))
    dp.append(0)
dp.append(0)
for i in range(N-1, -1, -1):
    day = arr[i][0]
    cost = arr[i][1]
    
    if i + day <= N:
        dp[i] = max(dp[i+1], dp[i+day] + arr[i][1])
    else:
        dp[i] = dp[i+1]
        
print(dp[0])
