N = int(input())

DP = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    if i == 1:
        DP[i] = 0
        continue
    DP[i] = DP[i-1] + 1
    if i % 3 == 0 and DP[i//3] + 1 < DP[i]:
        DP[i] = DP[i//3] + 1
    if i % 2 == 0 and DP[i//2] + 1< DP[i]:
        DP[i] = DP[i//2] + 1

print(DP[N])
