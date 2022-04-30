# https://www.acmicpc.net/problem/20058

from collections import deque

N, Q = map(int, input().split())

board = []

def rotate_right(ans):
    ans = list(zip(*ans[::-1]))
    for i in range(len(ans)):
        ans[i] = list(ans[i])
    return ans

for i in range(2**N):
    board.append(list(map(int, input().split())))
    
L = list(map(int,input().split()))

while L:
    A = L.pop(0)
    divide = 2 ** A
    
    for i in range(0, 2**N, divide):
        for j in range(0, 2**N, divide):
            ans = []
            for k in range(i, i + divide):
                new_ans = []
                for l in range(j, j + divide):
                    new_ans.append(board[k][l])
                ans.append(new_ans)
            
            ans = rotate_right(ans)
            
            for k in range(len(ans)):
                for l in range(len(ans[k])):
                    new_X = i + k
                    new_Y = j + l
                    board[new_X][new_Y] = ans[k][l]

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    new_board = [[0 for _ in range(2**N)] for _ in range(2**N)]
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            cnt = 0
            for k in range(4):
                new_X = dx[k] + i
                new_Y = dy[k] + j
                
                if new_X < 0 or new_Y < 0 or new_X >= len(board) or new_Y >= len(board):
                    continue
                
                if board[new_X][new_Y] > 0:
                    cnt += 1
            
            if cnt < 3:
                new_board[i][j] = board[i][j] - 1     
                if new_board[i][j] < 0:
                    new_board[i][j] = 0
            else:
                new_board[i][j] = board[i][j]
    
    board = new_board[:]

sum_result = 0
    
for i in board:
    sum_result += sum(i)

max_result = 0

def bfs(board):
    global max_result
    queue = deque([])
    visited = [[False for _ in range(len(board))] for _ in range(len(board))]
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 0 and visited[i][j] == False:
                queue.append([i,j])
            else:
                continue
            
            dx = [1,-1,0,0]
            dy = [0,0,1,-1]
            
            cnt = 0
            
            while queue:
                cnt += 1
                X, Y = queue.popleft()
                
                visited[X][Y] = True
                
                for k in range(4):
                    newX = X + dx[k]
                    newY = Y + dy[k]
                    
                    if newX < 0 or newY < 0 or newX >= len(board) or newY >= len(board):
                        continue
                    
                    if board[newX][newY] != 0 and visited[newX][newY] == False and [newX, newY] not in queue:
                        queue.append([newX, newY])
            
            max_result = max(cnt, max_result)
            
            
    return board

board = bfs(board)

print(sum_result)
print(max_result)