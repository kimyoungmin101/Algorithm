N = int(input())

T = []
P = []

for i in range(N):
    arr = list(map(int, input().split()))
    T.append(arr[0])
    P.append(arr[1])

DP = [0 for _ in range(N + 1)]

for i in range(N-1, -1, -1):
    if T[i] + i <= N:
        DP[i] = max(DP[i+1], DP[i+T[i]] + P[i])
    else:
        DP[i] = max(DP[i+1], DP[i])
    
    print(DP)

print(DP[0])