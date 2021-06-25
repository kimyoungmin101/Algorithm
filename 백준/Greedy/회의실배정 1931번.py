N = int(input())
arr = []

for i in range(N):
    A, B = map(int, input().split())
    arr.append([A, B])

arr = sorted(arr, key = lambda x : x[0])
arr = sorted(arr, key = lambda x : x[1])


A = arr.pop(0)

count = 1

for i in arr:
    if(A[1] <= i[0]):
        count += 1
        A = i

print(count)
