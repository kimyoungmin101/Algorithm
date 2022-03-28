# 플로이드 https://www.acmicpc.net/problem/11404

n = int(input())
m = int(input())

def floyd(arr):
    global n
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if arr[i][j] > arr[i][k] + arr[k][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]
    return arr
import sys

arr = [[sys.maxsize for _ in range(n)] for _ in range(n)]

for i in range(n):
    arr[i][i] = 0
    
for i in range(m):
    A, B, C = map(int, input().split())
    if arr[A-1][B-1] > C:
        arr[A-1][B-1] = C    
    

floyd(arr)

for i in range(n):
    for j in range(n):
        if arr[i][j] == sys.maxsize:
            print(0, end=" ")
        else:
            print(arr[i][j], end=" ")
    print()
