# https://www.acmicpc.net/problem/21610


# 비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다

N, M = map(int, input().split())
from copy import deepcopy
from collections import deque

board = []
for i in range(N):
    board.append(list(map(int, input().split())))
    
# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
cloud = deque([(N-1,0), (N-1, 1), (N-2,0), (N-2,1)])

for i in range(M):
    d, s = map(int, input().split())
    d -= 1
    #  (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다.
    
    go_x, go_y = dx[d], dy[d] # 방향 0,-3
    
    go_x *= s
    go_y *= s
    
    for idx, cl in enumerate(cloud):
        X, Y = cl
        
        go_x %= N
        go_y %= N
        
        X += go_x
        Y += go_y
        
        if X < 0:
            X = N + X
        elif X >= N:
            X %= N
        if Y < 0:
            Y = N + Y
        elif Y >= N:
            Y %= N
            
        board[X][Y] += 1
        cloud[idx] = (X,Y)
    
    before_cloud = cloud.copy()
    
    len_cloud = len(cloud)
    
    while cloud:
        X, Y = cloud.popleft()
        n_direct = [[-1,-1],[-1,1],[1,-1],[1,1]] # 대각선
        
        for a in range(4):
            new_X = X + n_direct[a][0]
            new_Y = Y + n_direct[a][1]
            
            if new_X < 0 or new_Y < 0 or new_Y >= N or new_X >= N:
                continue
            
            if board[new_X][new_Y] != 0:
                board[X][Y] += 1
    
    for x in range(N):
        for y in range(N):
            if board[x][y] >= 2 and (x,y) not in before_cloud:
                cloud.append((x,y))
                board[x][y] -= 2

sum_result = 0

for i in range(N):
    for j in range(N):
        sum_result += board[i][j]

print(sum_result)