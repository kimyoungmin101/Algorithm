# Q23

N = int(input())

arr = []

for i in range(N):
    larr = list(map(str, input().split()))
    A, B, C, D = larr[0], int(larr[1]), int(larr[2]), int(larr[3])
    
    arr.append([A, B, C, D])
    

arr = sorted(arr, key = lambda X : (-X[1], X[2], -X[3], X[0]))

for i in arr:
    print(i[0])