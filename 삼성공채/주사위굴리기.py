# https://www.acmicpc.net/problem/14499
from collections import deque

N, M, X, Y, K = map(int , input().split())

board = []
for i in range(N):
    board.append(list(map(int, input().split())))
    
move = list(map(int, input().split()))

dxdy = [[0,1], [0, -1], [-1, 0], [1,0]] # 동 서 북 남

for i in range(len(move)):
    move[i] = dxdy[move[i] - 1]

def move_down(dice_arr):
    A = dice_arr[0][1]
    B = dice_arr[1][1]
    C = dice_arr[2][1]
    D = dice_arr[3][1]
    
    dice_arr[0][1] = D
    dice_arr[1][1] = A
    dice_arr[2][1] = B
    dice_arr[3][1] = C
    
    return dice_arr

def move_up(dice_arr):
    A = dice_arr[0][1]
    B = dice_arr[1][1]
    C = dice_arr[2][1]
    D = dice_arr[3][1]
    
    dice_arr[0][1] = B
    dice_arr[1][1] = C
    dice_arr[2][1] = D
    dice_arr[3][1] = A
    
    return dice_arr

def move_right(dice_arr):
    A = dice_arr[1][0]
    B = dice_arr[1][1]
    C = dice_arr[1][2]
    D = dice_arr[3][1]
    
    dice_arr[1][0] = D
    dice_arr[1][1] = A
    dice_arr[1][2] = B
    dice_arr[3][1] = C
    
    return dice_arr

def move_left(dice_arr):
    A = dice_arr[1][0]
    B = dice_arr[1][1]
    C = dice_arr[1][2]
    D = dice_arr[3][1]
    
    dice_arr[1][0] = B
    dice_arr[1][1] = C
    dice_arr[1][2] = D
    dice_arr[3][1] = A
    
    return dice_arr

dice = [[0,0,0] for _ in range(5)]

def change_board(new_board, X_A, Y_A, new_dice):
    if new_board[X_A][Y_A] == 0:
        new_board[X_A][Y_A] = new_dice[3][1]
    else:
        new_dice[3][1] = new_board[X_A][Y_A]
        new_board[X_A][Y_A] = 0
        
    return new_board, dice

cnt_XY = [X, Y]

# dxdy = [[0,1], [0, -1], [-1, 0], [1,0]] # 동 서 북 남
# 상단 위치좌표 = 1,1 바닥 3,1


for i in move:
    new_X = cnt_XY[0] + i[0]
    new_Y = cnt_XY[1] + i[1]
    
    if new_X < 0 or new_Y < 0 or new_X >= len(board) or new_Y >= len(board[0]):
        continue
    cnt_XY = [new_X, new_Y]

    if i == [0,1]: # 동쪽
        dice = move_right(dice)
        board, dice = change_board(board, new_X, new_Y, dice)
    elif i == [0,-1]: # 서쪽
        dice = move_left(dice)
        board, dice = change_board(board, new_X, new_Y, dice)
    elif i == [-1,0]: # 북쪽
        dice = move_up(dice)
        board, dice = change_board(board, new_X, new_Y, dice)
    else:# 남쪽
        dice = move_down(dice)
        board, dice = change_board(board, new_X, new_Y, dice)
    
    print(dice[1][1])