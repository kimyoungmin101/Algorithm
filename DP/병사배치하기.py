# https://www.acmicpc.net/problem/18353

N = int(input())

army = list(map(int, input().split()))
DP = [1 for _ in range(len(army))]

for i in range(N):
    for j in range(i - 1, -1, -1):
        if army[i] < army[j]:
            DP[i] = max(DP[i], DP[j] + 1)
            
print(N - max(DP))
