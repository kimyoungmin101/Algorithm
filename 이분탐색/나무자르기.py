from sys import stdin, stdout

N, M = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

# 10 15 17 20
start , end = 1, max(arr)

while start <= end:
    mid = int((start+end) // 2)

    log = 0
    for i in arr:
        if i >= mid:
            log += i - mid
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)