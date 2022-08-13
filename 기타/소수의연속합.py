# https://www.acmicpc.net/problem/1644
import math
N = int(input())

arr = [True for _ in range(N+1)]


for i in range(2, int(math.sqrt(N)) + 1):
    if arr[i] == True:
        for j in range(i*i, N+1, i):
            arr[j] = False
result = []
for i in range(2, N+1):
    if arr[i] == True:
        result.append(i)

cnt = 0

for start in range(len(result)):
    ans = 0
    end = start
    
    while end < len(result):
        ans += result[end]
        if ans < N:
            end += 1
        elif ans == N:
            cnt += 1
            break
        else:
            break
print(cnt)