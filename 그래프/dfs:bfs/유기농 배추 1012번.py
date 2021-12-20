import sys
from collections import deque
T = int(sys.stdin.readline())

def bfs(i, j, arr, count):
    queue = deque([])
    queue.append([i,j])
    while(queue):
        A = queue.popleft()
        i = A[0]
        j = A[1]
        if(arr[i+1][j] == 1):
            queue.append([i+1, j])
            arr[i+1][j] = 0
        if(arr[i][j+1] == 1):
            queue.append([i, j+1])
            arr[i][j+1] = 0
        if(arr[i][j-1] == 1):
            queue.append([i, j-1])
            arr[i][j-1] = 0
        if(arr[i-1][j] == 1):
            queue.append([i-1, j])
            arr[i-1][j] = 0
    return count + 1


for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0] * (N+2) for _ in range(M+2)]

    for j in range(K):
        A, B = map(int, sys.stdin.readline().split())
        arr[A+1][B+1] = 1


    count = 0
    for R in range(1, len(arr)):
        for T in range(1, len(arr[R])):
            if(arr[R][T] == 1):
                count = bfs(R, T, arr, count)
    print(count)
