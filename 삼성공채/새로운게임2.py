# https://www.acmicpc.net/problem/17837

from collections import deque

N, K = map(int, input().split())

# 말이 4개 이상 쌓이는 순간 게임이 종료된다.

# 1 : →, 2: ←, 3: ↑, 4: ↓
board = []
direct_dic = {}

for i in range(N):
    board.append(list(map(int, input().split())))

stack_board = [[[] for _ in range(N)] for _ in range(N)]

queue = deque([])

for i in range(K):
    X, Y, dir = map(int, input().split())
    X -= 1
    Y -= 1
    queue.append([X,Y])
    direct_dic[i+1] = dir
    stack_board[X][Y].append(i+1)

def attach_blue(cnt_val, cnt_number, go_stack, remain_stack):
    cnt_X, cnt_Y = cnt_val
    
    cnt_dir = direct_dic[cnt_number]
    
    if cnt_dir == 1:
        cnt_dir = 2
    elif cnt_dir == 2:
        cnt_dir = 1
    elif cnt_dir == 3:
        cnt_dir = 4
    else:
        cnt_dir = 3
    
    direct_dic[cnt_number] = cnt_dir
    
    nxt_X = cnt_X
    nxt_Y = cnt_Y
    
    if cnt_dir == 1: # 오른쪽이라면
        nxt_Y += 1
    elif cnt_dir == 2: # 왼쪽이라면
        nxt_Y -= 1
    elif cnt_dir == 3: # 위쪽이라면
        nxt_X -= 1
    else:
        nxt_X += 1
    
    if nxt_X < 0 or nxt_Y < 0 or nxt_X >= N or nxt_Y >= N: # 벽이라면
        return cnt_X, cnt_Y
    
    if board[nxt_X][nxt_Y] == 2: # 파란색 이라면
        return cnt_X, cnt_Y
    elif board[nxt_X][nxt_Y] == 0:
        attach_white([cnt_X, cnt_Y], [nxt_X, nxt_Y], go_stack, remain_stack)
        return nxt_X, nxt_Y
    elif board[nxt_X][nxt_Y] == 1:
        attach_red([cnt_X, cnt_Y], [nxt_X, nxt_Y], go_stack, remain_stack)    
        return nxt_X, nxt_Y
    

def attach_red(cnt_val, nxt_val, go_stack, remain_stack):
    # 빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
    cnt_X, cnt_Y = cnt_val
    nxt_X, nxt_Y = nxt_val
    
    go_stack.reverse()
    
    stack_board[cnt_X][cnt_Y] = remain_stack
    stack_board[nxt_X][nxt_Y].extend(go_stack)
    

def attach_white(cnt_val, nxt_val, go_stack, remain_stack):
    cnt_X, cnt_Y = cnt_val
    nxt_X, nxt_Y = nxt_val
    
    stack_board[cnt_X][cnt_Y] = remain_stack
    stack_board[nxt_X][nxt_Y].extend(go_stack)

def go_forward(cnt_X, cnt_Y, direction):
    global N
    
    nxt_X = cnt_X
    nxt_Y = cnt_Y
    
    if direction == 1: # 오른쪽이라면
        nxt_Y += 1
    elif direction == 2: # 왼쪽이라면
        nxt_Y -= 1
    elif direction == 3: # 위쪽
        nxt_X -= 1
    else:
        nxt_X += 1
    
    if nxt_X < 0 or nxt_Y < 0 or nxt_X >= N or nxt_Y >= N:
        return False, cnt_X, cnt_Y
    elif board[nxt_X][nxt_Y] == 2:
        return False, cnt_X, cnt_Y
    else:
        return True, nxt_X, nxt_Y

def solution(cnt, queue):
    while cnt < 1000:
        
        cnt_number = 1
        
        for idx in range(len(queue)):
            cnt_X, cnt_Y = queue[idx]
            cnt_dir = direct_dic[cnt_number]
            cnt_stack = stack_board[cnt_X][cnt_Y]
            
            val_idx = cnt_stack.index(cnt_number)
            
            remain_stack = cnt_stack[:val_idx] # 남아야 하는 스택
            go_stack = cnt_stack[val_idx:] # 옮겨져야 하는 스택
            
            is_bool, nxt_X, nxt_Y = go_forward(cnt_X, cnt_Y, cnt_dir) # 첫 번째는 벽인지 아닌지 판단 가능,
            
            if is_bool == False: # 벽이나 파란색이라면 ?
                nxt_X, nxt_Y = attach_blue([cnt_X, cnt_Y], cnt_number, go_stack, remain_stack) # 파란색과 똑같음
            else:
                nxt_color = board[nxt_X][nxt_Y]
                if nxt_color == 0: # 흰색이면
                    attach_white([cnt_X, cnt_Y], [nxt_X, nxt_Y], go_stack, remain_stack)
                elif nxt_color == 1: # 빨간색이면
                    attach_red([cnt_X, cnt_Y], [nxt_X, nxt_Y], go_stack, remain_stack)
            
            for val in go_stack:
                queue[val-1] = [nxt_X, nxt_Y]
                
            if len(stack_board[nxt_X][nxt_Y]) >= 4:
                return cnt
            
            cnt_number += 1
        
        cnt += 1
        
    return -1
        
print(solution(1,queue))