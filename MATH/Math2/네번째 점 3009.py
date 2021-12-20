arr1 = []
arr2 = []

for i in range(3):
    M, N = map(int, input().split())
    if(M not in arr1):
        arr1.append(M)
    else:
        arr1.remove(M)
    if(N not in arr2):
        arr2.append(N)
    else:
        arr2.remove(N)

print(arr1[0], arr2[0])

#https://www.acmicpc.net/problem/3009
