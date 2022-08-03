# 감시피하기

from itertools import combinations
import copy

N = int(input())

board = []

for i in range(N):
    board.append(list(map(str, input().split())))
    
bin_list = []
student_list = []
teacher_list = []

for i in range(N):
    for j in range(N):
        if board[i][j] == "X":
            bin_list.append([i,j])
        elif board[i][j] == "T":
            teacher_list.append([i,j])
        else:
            student_list.append([i,j])

obtain = list(combinations(bin_list, 3))


def get_find(box, new_board):
    for i in box:
        X = i[0]
        Y = i[1]
        
        new_board[X][Y] = "O"
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for teacher in teacher_list:
        for i in range(4):
            t_X = teacher[0] + dx[i]
            t_Y = teacher[1] + dy[i]
            
            while t_X >= 0 and t_Y >= 0 and t_X < len(new_board) and t_Y < len(new_board):
                if new_board[t_X][t_Y] == "O":
                    break
                elif new_board[t_X][t_Y] == "S":
                    return False
                
                t_X += dx[i]
                t_Y += dy[i]
        
    return True

result_bool = False

for i in obtain:
    new_board = copy.deepcopy(board)
    if get_find(i, new_board):
        result_bool = True
        break

if result_bool:
    print("YES")
else:
    print("NO")
        