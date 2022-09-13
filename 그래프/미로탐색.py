# https://www.acmicpc.net/problem/2178
from collections import deque
N, M = map(int, input().split())

board = []

for i in range(N):
    board.append(list(map(int, input().strip())))
    
q = deque([[0,0]])

visit = [[0 for _ in range(M)] for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

while q:
    X, Y = q.popleft()
    if X == N-1 and Y == M-1:
        print(visit[X][Y] + 1)
        break
    for i in range(4):
        new_X = X + dx[i]
        new_Y = Y + dy[i]
        
        if new_X < 0 or new_Y < 0 or new_X >= N or new_Y >= M:
            continue
        
        if visit[new_X][new_Y] == 0 and board[new_X][new_Y] == 1:
            visit[new_X][new_Y] = visit[X][Y] + 1
            q.append([new_X, new_Y])
            
    