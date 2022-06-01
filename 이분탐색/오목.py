# https://www.acmicpc.net/problem/2615

board = []
visited = []
for i in range(19):
    board.append(list(map(int, input().split())))
    
def dfs(cnt_arr, X, Y, dir, value):
    new_X, new_Y = X + dir[0], Y + dir[1]
    
    if len(cnt_arr) == 5:
        if new_X >= 0 and new_Y >= 0 and new_X < 19 and new_Y < 19:
            if board[new_X][new_Y] == value:
                return False, []
        
        return True, cnt_arr
    
    if new_X < 0 or new_Y < 0 or new_X >= 19 or new_Y >= 19:
        return False, []
    
    if board[new_X][new_Y] == value:
        cnt_arr.append([new_X, new_Y])
        return dfs(cnt_arr, new_X, new_Y, dir, value)
    else:
        return False, []
    
    
    
direction = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]] # 위 위오

def solution():
    for i in range(19):
        for j in range(19):
            if board[i][j] != 0:
                for idx, a in enumerate(direction):
                    dx, dy = a
                    dx = -dx
                    dy = -dy
                    
                    new_i = i + dx
                    new_j = j + dy
                    
                    if new_i >= 0 and new_j >= 0 and new_i < 19 and new_j < 19:
                        if board[new_i][new_j] == board[i][j]:
                            continue
                    
                    result, arr = dfs([[i, j]], i, j, a, board[i][j])
                        
                    if result:
                        arr = sorted(arr, key = lambda X : (X[1], X[0]))
                        return arr[0], board[i][j]
                    
    return [], 0

result, color = solution()

if color == 0:
    print(0)
else:
    print(color)
    print(result[0]+1, result[1] + 1)
