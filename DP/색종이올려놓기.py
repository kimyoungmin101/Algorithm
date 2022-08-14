# https://www.acmicpc.net/problem/2643

N = int(input())

DP = [1 for _ in range(N)]
arr = sorted([sorted(map(int, input().split())) for i in range(N)])

for i in range(1, N): 
    for j in range(i):
        if arr[j][1] <= arr[i][1]:
            DP[i] = max(DP[j] + 1, DP[i])

print(max(DP))