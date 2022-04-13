from collections import deque

first = list(map(int, input().strip()))
second = list(map(int, input().strip()))
third = list(map(int, input().strip()))
fourth = list(map(int, input().strip()))

K = int(input())

arr = []

board = [first, second, third, fourth]

def get_result(cnt_board, cnt_idx, cnt_dirct):
    this_direct = 0
    
    if cnt_dirct == 1:
        this_direct = 0
    else:
        this_direct = 1
    
    cnt_arr = cnt_board[cnt_idx]
    return [cnt_arr, cnt_idx, this_direct]

def change_board(cnt_board, idx, direction):
    
    queue = []
    visited = [idx]
    
    cnt_arr = cnt_board[idx] # third
    queue.append([cnt_arr, idx, direction]) # third, 2, -1
    
    while queue:
        nxt_queue, cnt_idx, cnt_dirct = queue.pop(0)
        left_direction = nxt_queue[6]
        right_dirction = nxt_queue[2]
        
        nxt_queue = deque(nxt_queue)
        if cnt_dirct == 1:
            nxt_queue.rotate(1)
        else:
            nxt_queue.rotate(-1)
        
        next = []
        for i in nxt_queue:
            next.append(i)
            
        cnt_board[cnt_idx] = next
        
        if cnt_idx - 1 not in visited and cnt_idx - 1 >= 0:
            visited.append(cnt_idx - 1)
            if left_direction != cnt_board[cnt_idx-1][2]:
                nxt = get_result(cnt_board, cnt_idx - 1, cnt_dirct)
                queue.append(nxt)

        if cnt_idx + 1 not in visited and cnt_idx + 1 < 4:
            visited.append(cnt_idx + 1)
            if right_dirction != cnt_board[cnt_idx+1][6]:
                nxt = get_result(cnt_board, cnt_idx + 1, cnt_dirct)
                queue.append(nxt)
            
    return cnt_board

for i in range(K):
    A, B = map(int, input().split())
    A -= 1

    board = change_board(board, A, B)

ans = 0
if board[0][0] == 1:
    ans += 1
if board[1][0] == 1:
    ans += 2
if board[2][0] == 1:
    ans += 4
if board[3][0] == 1:
    ans += 8        
    
print(ans)
    
    