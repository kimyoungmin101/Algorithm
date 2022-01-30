# https://www.acmicpc.net/problem/11404

import sys


N = int(input())

graph = [[sys.maxsize for _ in range(N)] for _ in range(N)]

M = int(input())

for i in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    
    graph[A][B] = min(graph[A][B], C)

for i in range(N):
    graph[i][i] = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
            # 1,0 => 1 4 + 4 0 / 5 + 7

for i in range(N):
    for j in range(N):
        if graph[i][j] == sys.maxsize:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
'''
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
'''