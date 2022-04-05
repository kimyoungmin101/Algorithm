from collections import deque

N, M = map(int, input().split())

board = []
target = []
red = []
blue = []


dxdy = [[0,1], [1,0], [-1,0],  [0,-1]] # 오른쪽, 아래, 위, 왼쪽

for i in range(N):
    board.append(list(map(str, input().strip())))
    
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            board[i][j] = '.'
            red = [i, j]
        elif board[i][j] == 'B':
            board[i][j] = '.'
            blue = [i, j]
        elif board[i][j] == 'O':
            target = [i, j]

def go_to(direction, color_red_result, color_blue_result):
    dx = direction[0]
    dy = direction[1]
    
    color_red = color_red_result.copy()
    color_blue = color_blue_result.copy()
    
    red_goal = False
    blue_goal = False
    
    while True:
        X = color_red[0] + dx
        Y = color_red[1] + dy
        
        if board[X][Y] == '#':
            break
        elif [X, Y] == color_blue:
            new_X = X + dx
            new_Y = Y + dy
            if board[new_X][new_Y] == '.':
                color_red[0] = X
                color_red[1] = Y
                color_blue[0] = new_X
                color_blue[1] = new_Y
                continue
            elif board[new_X][new_Y] == 'O':
                blue_goal = True
                break
            else:
                break
        elif board[X][Y] == '.':
            color_red[0] = X
            color_red[1] = Y
        elif board[X][Y] == 'O':
            red_goal = True
            color_red[0] = X
            color_red[1] = Y
            break
        else:
            if color_red == color_blue:
                color_red[0] -= dx
                color_red[1] -= dy
            break
    
    while True:
        X = color_blue[0] + dx
        Y = color_blue[1] + dy
        
        
        if board[X][Y] == '.':
            color_blue[0] = X
            color_blue[1] = Y
        elif board[X][Y] == 'O':
            blue_goal = True
            break
        else:
            if color_red == color_blue:
                color_blue[0] -= dx
                color_blue[1] -= dy
            break
        
        
    if red_goal == True and blue_goal == False:
        return True, color_red, color_blue
    elif red_goal == False and blue_goal == False:
        return False, color_red, color_blue
    else:
        return False, color_red_result, color_blue_result
    
def bfs(n):
    queue = deque([])
    
    queue.append([red, blue, n])
    
    visited = []
    
    while queue:
        cnt_red, cnt_blue, cnt = queue.popleft()
        visited.append([cnt_red, cnt_blue])
        if cnt > 10:
            return -1
        for i in range(4):
            result, new_red, new_blue = go_to(dxdy[i], cnt_red, cnt_blue)
            
            if result == True:
                if cnt >= 10:
                    return -1
                return cnt + 1
            if [new_red, new_blue] not in visited:
                queue.append([new_red, new_blue, cnt + 1])
                    
    
    return -1

print(bfs(0))