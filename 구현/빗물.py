# https://www.acmicpc.net/problem/14719

H, W = map(int, input().split())

arr = list(map(int, input().split()))

first = arr[0]
result = 0

board = [[0 for _ in range(W)] for _ in range(H)]

for idx, value in enumerate(arr):
    for i in range(value):
        board[H-1-i][idx] = 1

cnt = 0
def can_go(board, X, Y):
    global W
    # 왼쪽으로이동
    left_X = X
    left_Y = Y
    
    right_X = X
    right_Y = Y
    while True:
        left_Y -= 1
        if left_Y < 0:
            return False
        if board[left_X][left_Y] == 1:
            break
    while True:
        right_Y += 1
        if right_Y >= W:
            return False
        if board[right_X][right_Y] == 1:
            break
        
    return True

is_bool = True

for i in range(H-1,-1,-1):
    for j in range(W):
        if board[i][j] == 0:
            if can_go(board, i, j):
                board[i][j] = 2
                cnt += 1

print(cnt)        
