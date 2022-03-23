# 효율적인 화폐구성


'''
2 15
2
3

3 4
3
5
7

'''
N, M = map(int, input().split())

dp = [10001 for _ in range(M+1)]
dp[0] = 0

answer = -1
arr = []

for i in range(N):
    arr.append(int(input()))

arr.sort()

for i in range(N):
    for j in range(arr[i], M + 1):
        if (dp[j - arr[i]]) != 10001:
            dp[j]  = min(dp[j], dp[j-arr[i]] + 1)
            
print(dp)
        

# [2,3] / [4,5,6] / []