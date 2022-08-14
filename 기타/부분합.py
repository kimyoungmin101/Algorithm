import sys
N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = sys.maxsize
ans = 0
end = 0

for start in range(len(arr)):
    while ans < S and end < len(arr):
        ans += arr[end]
        end += 1
    if ans >= S:
        cnt = min(cnt, end - start)
    ans -= arr[start]
    
if cnt == sys.maxsize:
    print(0)
else:
    print(cnt)