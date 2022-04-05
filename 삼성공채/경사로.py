# https://www.acmicpc.net/problem/14890

N, L = map(int, input().split())

def board_rotate(board_arr):
    new_board = []
    for i in range(len(board_arr)):
        list_A = []
        for j in range(len(board_arr)):
            list_A.append(board_arr[j][i])
        new_board.append(list_A)
        
    return new_board

board = []

for i in range(N):
    board.append(list(map(int, input().split())))

board_first = board.copy()
board_second = board_rotate(board)

def is_true(list_value, line):
    visited = [False for _ in range(len(list_value))]
    
    # 모두 같으면 True
    A = list_value[0]
    if list_value.count(A) == len(list_value):
        return True
    
    # 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
    for i in range(1, len(list_value)):
        if abs(list_value[i-1] - list_value[i]) >= 2:
            return False
    
    # 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
    # 경사로를 놓다가 범위를 벗어나는 경우
    for i in range(1, len(list_value)):
        if list_value[i] != list_value[i-1]:
            if list_value[i-1] < list_value[i]:
                if i - line < 0:
                    return False
                
                value_i = list_value[i-line] # 1
                
                for j in range(i - line, i):
                    if list_value[j] != value_i:
                        return False
                    elif visited[j] == True:
                        return False
                    else:
                        visited[j] = True
            else:
                if i + line > len(list_value):
                    return False
                else:
                    value_i = list_value[i]
                    for j in range(i, i+line):
                        if list_value[j] != value_i:
                            return False
                        else:
                            visited[j] = True
            
    return True

cnt = 0

for i in range(len(board_first)):
    list_i = board_first[i]
    if is_true(list_i, L):
        cnt += 1

for i in range(len(board_second)):
    list_i = board_second[i]
    if is_true(list_i, L):
        cnt += 1

print(cnt)