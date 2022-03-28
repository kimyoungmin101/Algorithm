# 정확한 순위

N, M = map(int, input().split())
import sys
import copy

def floyd(arr_Q):
    global N
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if arr_Q[i][j] > arr_Q[i][k] + arr_Q[k][j]:
                    arr_Q[i][j] = arr_Q[i][k] + arr_Q[k][j]
    
    return arr_Q

arr = [[sys.maxsize for _ in range(N)] for _ in range(N)]
brr = [[sys.maxsize for _ in range(N)] for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    arr[A-1][B-1] = 1
    brr[B-1][A-1] = 1

for i in range(N):
    arr[i][i] = 0
    brr[i][i] = 0


    

A_arr = floyd(copy.deepcopy(arr))

B_arr = floyd(copy.deepcopy(brr))

for i in A_arr:
    print(i)
    
print(' ')

for i in B_arr:
    print(i)

'''
6 6
1 5
3 4
4 2
4 6
5 2
5 4
'''