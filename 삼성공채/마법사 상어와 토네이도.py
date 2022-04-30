# https://www.acmicpc.net/problem/20057

from collections import deque
import copy

N = int(input())

def rotate_right(direct):
    direct = list(zip(*direct[::-1]))
    for i in range(len(direct)):
        direct[i] = list(direct[i])
        
    return direct

    
board = []
for i in range(N):
    board.append(list(map(int,input().split())))
    
dx = [[0,-1],[1,0],[0,1],[-1,0]] # 왼 아 오 위

arr = []

for i in range(1, N):
    if i == N-1:
        arr.append(i)
        arr.append(i)
        arr.append(i)
    else:
        arr.append(i)
        arr.append(i)
        
X = N // 2
Y = N // 2

dir = 0

result = [[X,Y]]

direction = [[0,0,2,0,0],
             [0,10,7,1,0],
             [5,0,0,0,0],
             [0,10,7,1,0],
             [0,0,2,0,0]
             ]


left = []
ans = 0

for i in arr:
    for j in range(i):
        X = X + dx[dir][0]
        Y = Y + dx[dir][1]
        
        value = board[X][Y] # y의 모래의 값
        
        if value == 0:
            continue
        
        board[X][Y] = 0
        
        new_direction = copy.deepcopy(direction)
        
        if dir == 1: # 아래쪽
            new_direction = rotate_right(new_direction)
            new_direction = rotate_right(new_direction)
            new_direction = rotate_right(new_direction)
        elif dir == 2: # 오른쪽
            new_direction = rotate_right(new_direction)
            new_direction = rotate_right(new_direction)
        elif dir == 3: # 위쪽
            new_direction = rotate_right(new_direction)
        
        sum_result = 0
        
        for k in range(5):
            for r in range(5):
                if new_direction[k][r] != 0:
                     new_direction[k][r] = (value * new_direction[k][r]) // 100
                     sum_result += new_direction[k][r]
        
        if dir == 0:
            new_direction[2][1] = value - sum_result
        elif dir == 1:
            new_direction[3][2] = value - sum_result
        elif dir == 2:
            new_direction[2][3] = value - sum_result
        else:
            new_direction[1][2] = value - sum_result
        
        ansarr = []
        
        for k in range(5):
            for r in range(5):
                if new_direction[k][r] != 0:
                    ansarr.append([k-2,r-2, new_direction[k][r]])
        
        for k in ansarr:
            newX = k[0] + X
            newY = k[1] + Y
        
            if newX < 0 or newY < 0 or newX >= N or newY >= N:
                ans += k[2]
                continue
            
            board[newX][newY] += k[2]
            
        
        
    dir = (dir + 1) % 4

print(ans)
