# https://www.acmicpc.net/problem/18353 병사배치하기

N = int(input())

arr = list(map(int, input().split()))

DP = [0 for _ in range(N)]

for i in range(N):
    for j in range(i-1, -1, -1):
        print(i, j )
        if arr[i] < arr[j]:
            DP[i] = max(DP[j] + 1, DP[i])
print(DP)      
print(N - max(DP) - 1)