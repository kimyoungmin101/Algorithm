# https://www.acmicpc.net/problem/2003


N, M = map(int, input().split())

arr = list(map(int, input().split()))
cnt = 0

for start in range(len(arr)):
    ans = 0
    end = start
    
    while end < len(arr):
        ans += arr[end]
        if ans == M:
            cnt += 1
            break
        elif ans > M:
            break
        
        end += 1
            
print(cnt)