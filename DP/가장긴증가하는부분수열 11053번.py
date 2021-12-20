N = int(input())

a = list(map(int, input().split()))


dp = [0] * N
A = 0

for i in range(N):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))

# 1 0 0 0 0 0
# 1 0 0 0 0 0
# 2 0 1 0 0 0
# 2 0 1 0 0 0
# 3 0 2 1 1 0
