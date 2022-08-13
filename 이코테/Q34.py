# https://www.acmicpc.net/problem/18353 병사배치하기

# N = int(input())
# arr = list(map(int, input().split()))

# DP = [0 for _ in range(len(arr))]
# for i in range(len(arr)):
#     for j in range(i):
#         if arr[j] > arr[i]:
#             DP[i] = max(DP[i], DP[j] + 1)
            
    
# print(len(arr) - max(DP) - 1)

# 이진법으로 풀기

from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))
arr.reverse()

lis = [arr[0]]
record = [1]

for i in range(1, len(arr)):
    record.append(bisect_left(lis, arr[i]) + 1)
    if arr[i] > lis[-1]:
        lis.append(arr[i])
    else:
        A = bisect_left(lis, arr[i])
        lis[A] = arr[i]

max_record = max(record)
result = []

for i in range(len(arr)-1, -1, -1):
    if record[i] == max_record:
        result.append(arr[i])
        max_record -= 1

result
print(len(result))
print(*result)