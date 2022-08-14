# 정확한 순위

'''
6 6
1 5
3 4
4 2
4 6
5 2
5 4
'''
import sys
N, M = map(int, input().split())
board = [[sys.maxsize for _ in range(N)] for _ in range(N)]

for i in range(M):
    X, Y = map(int, input().split())
    
    board[X-1][Y-1] = 1
    
for k in range(N):
    for i in range(N):
        for j in range(N):
            if board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]

result = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] != sys.maxsize:
            board[i][j] = True
            board[j][i] = True
        if i == j:
            board[i][j] = True

ans = []
for idx, value in enumerate(board):
    if sys.maxsize not in value:
        ans.append(idx+1)

print(len(ans))