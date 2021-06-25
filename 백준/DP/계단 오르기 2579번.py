import sys
input = sys.stdin.readline

arr = []


l = int(input())

dp = [0] * l

for _ in range(l):
    arr.append(int(input()))

for i in range(l):
    if(i == 0):
        dp[0] = arr[0]
        continue
    elif(i == 1):
        dp[1] = max(arr[0], arr[0] + arr[1])
        continue
    elif(i == 2):
        dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])
    else:
        dp[i] = (max(dp[i-2] + arr[i], arr[i-1]+arr[i]+dp[i-3]))

print(dp.pop())
