import sys
from collections import deque
import copy
N, M = map(int, sys.stdin.readline().split())
max_num = 0

empty_list = []
virus_list = []
board = []
# 0은 빈 칸, 1은 벽, 2는 바이러스

result = []

def combinations_def(empty, empty_new_list):
    if len(empty_new_list) == 3:
        result.append(empty_new_list.copy())
        return
    
    start = empty.index(empty_new_list[-1]) if empty_new_list else 0
    
    for i in range(start, len(empty)):
        if empty[i] not in empty_new_list:
            empty_new_list.append(empty[i])
            combinations_def(empty, empty_new_list)
            empty_new_list.pop()
    
for i in range(N):
    board.append(list(map(int, input().split())))
    
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            virus_list.append([i,j])    
        elif board[i][j] == 0:
            empty_list.append([i,j])

combinations_def(empty_list, [])

max_safe = 0 # 안전영역의 개수

def get_find(value, new_board):
    global max_safe
    
    for v in value:
        new_board[v[0]][v[1]] = 1
    
    queue = virus_list.copy()
    queue = deque(queue)
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    while queue:
        X, Y = queue.popleft()
        
        for i in range(4):
            new_X = X + dx[i]
            new_Y = Y + dy[i]
            
            if new_X < 0 or new_Y < 0 or new_X >= len(new_board) or new_Y >= len(new_board[0]):
                continue
            
            if new_board[new_X][new_Y] != 0:
                continue
            
            queue.append([new_X, new_Y])
            new_board[new_X][new_Y] = 2
            
    cnt = 0
    
    for i in range(len(new_board)):
        for j in range(len(new_board[i])):
            if new_board[i][j] == 0:
                cnt += 1
    
    max_safe = max(cnt, max_safe)


for value in result:
    new_board = copy.deepcopy(board)
    get_find(value, new_board)

print(max_safe)