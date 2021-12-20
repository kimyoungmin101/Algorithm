N = int(input())


arr = []


for i in range(N):
    a, b = map(str, input().split())
    arr.append([int(a), b])

arr = sorted(arr, key = lambda x : x[0])

for i in arr:
    print(i[0], i[1])
