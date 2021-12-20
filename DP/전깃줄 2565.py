N = int(input())

arr = []
dp = [1] * N
for i in range(N):
    A = list(map(int,input().split()))
    arr.append(A)


arr = sorted(arr, key = lambda x : x[0])

print(arr)

for i in range(N):
    for j in range(i):
        if (arr[i][1] > arr[j][1]):
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
