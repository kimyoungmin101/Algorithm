N = int(input())

arr = list(map(int, input().split()))

#n개의 정수중 연속된 숫자의 합의 가장큰 것

DP = [0] * len(arr)
DP[0] = arr[0]

for i in range(len(arr)):
    if(arr[i] + DP[i-1] < 0 ):
        DP[i] = arr[i]
        continue
    if(arr[i] + DP[i-1] > arr[i]):
        DP[i] = arr[i] + DP[i-1]
    else:
        DP[i] = arr[i]

# 2 1 -4 3 4 -4 6 5 -5 1
# 2 3 -4 3 7 3 9 14 9 10

# -1 -2 -3 -4 -5
# -1 -2 -3 -4 -5

print(max(DP))
