N, K = map(int, input().split())

arr = []

for i in range(N):
    A = int(input())
    arr.append(A)

arr = sorted(arr, reverse = True)


count = 0
i = 0

while(True):
    if(K - arr[i] >= 0):
        count += 1
        K -= arr[i]
        if(K == 0):
            break
    else:
        i += 1

print(count)
