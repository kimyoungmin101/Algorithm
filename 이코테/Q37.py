# 플로이드
# https://www.acmicpc.net/problem/1613
import sys
n, k = map(int, input().split())

board = [[sys.maxsize for _ in range(n)] for _ in range(n)]

for i in range(k):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    board[a][b] = 1
    
s = int(input())
ans = []

for i in range(s):
    ans.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]

for X,Y in ans:
    X -= 1
    Y -= 1
    if board[X][Y] == sys.maxsize and board[Y][X] == sys.maxsize:
        print(0)
    elif board[X][Y] != sys.maxsize:
        print(-1)
    else:
        print(1)
    
    