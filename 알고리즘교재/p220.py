# 개미 전사
N = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(len(arr))]

dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

for i in range(2, len(dp)):
    dp[i] = max(dp[i-1], dp[i-2] + arr[i])

print(dp[-1])

'''
4
1 3 1 5

6
6 1 3 4 5 7
'''