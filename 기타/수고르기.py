# https://www.acmicpc.net/problem/2230

import sys

N, M = map(int, input().split())

arr = []

for i in range(N):
    arr.append(int(input()))

arr.sort()

end = 0
min_cnt = sys.maxsize

for start in range(N):
    while end < N:
        if M <= (arr[end] - arr[start]):
            min_cnt = min(arr[end] - arr[start], min_cnt)
            break
        end += 1
                
print(min_cnt)
