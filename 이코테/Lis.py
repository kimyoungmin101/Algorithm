# 4 2 6 7 9 1 3 10
# 최장증가수열

import sys, bisect

x = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]
record = []

for i in range(x):
    record.append(bisect.bisect_left(dp, arr[i])+1)
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))
max_len = max(record)
result = []

for i in range(len(arr)-1, -1, -1):
    if record[i] == max_len:
        max_len -= 1
        result.append(arr[i])

result.reverse()
print(*result)

