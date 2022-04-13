# https://www.acmicpc.net/problem/16235

from collections import deque

# (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)

direct = [[-1,-1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

N, M, K = map(int, input().split())

board = [[5 for _ in range(N)] for _ in range(N)]

new_board = []

for i in range(N):
    new_board.append(list(map(int, input().split())))    

def spring(newAge):    

    for i in range(N):
        for j in range(N):
            tree = deque([])
            next_land = 0
            for A in newAge[i][j]:
                if board[i][j] - A < 0:
                    next_land += (A // 2)
                else:
                    board[i][j] -= A
                    A += 1
                    tree.append(A)
            board[i][j] += next_land
            newAge[i][j] = tree
                
    return newAge


age = [[deque() for _ in range(N)] for _ in range(N)]

for i in range(M):
    X, Y, Z = map(int, input().split())
    age[X-1][Y-1].append(Z)

for i in range(K):
    # 봄
    age = spring(age)
    
    '''
    for k in dead_tree:
        X, Y, A = k
        value = (A // 2)
        board[X][Y] += value 
    '''
    
    tmp_trees = [] # (r, c)
    for r in range(N):
        for c in range(N):
            for value in age[r][c]:
                if value % 5 == 0: #
                    for j in range(8):
                        new_X = r + direct[j][0]
                        new_Y = c + direct[j][1]
                        
                        if new_X < 0 or new_Y < 0 or new_X >= N or new_Y >= N:
                            continue
                        
                        tmp_trees.append([new_X, new_Y])
                    
            board[r][c] += new_board[r][c]
            
    for tree in tmp_trees:
        r, c = tree
        age[r][c].appendleft(1)
        
cnt = 0

for i in range(N):
    for j in range(N):
        cnt += len(age[i][j])
        
print(cnt)