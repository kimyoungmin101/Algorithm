
import copy

n = int(input())


arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    
direction = [[-1,0], [0,1], [1,0], [0,-1]] # 위 오 아 왼

max_num = 0

def right(board):
    for i in range(n):
        pointer = n - 1
        for j in range(n - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer]  == tmp:
                    board[i][pointer] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[i][pointer] = tmp        
    return board

def rotate_90(go_ans):
    go_ans = list(zip(*go_ans[::-1]))
    for i in range(len(go_ans)):
        go_ans[i] = list(go_ans[i])

    return go_ans


    
def recursive(arr, cnt):
    global max_num
    
    if cnt == 5:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if max_num < arr[i][j]:
                    max_num = arr[i][j]
        return

    # 오른쪽
    arr_copy = copy.deepcopy(arr)
    arr_copy = right(arr_copy)
    recursive(arr_copy, cnt + 1)
    
    # 아래쪽
    arr_copy = copy.deepcopy(arr)
    arr_copy = rotate_90(arr)
    arr_copy = right(arr_copy)
    for i in range(3):
        arr_copy = rotate_90(arr_copy)
    recursive(arr_copy, cnt + 1)
    
    # 왼쪽
    arr_copy = copy.deepcopy(arr)
    for i in range(2):
        arr_copy = rotate_90(arr_copy)
    arr_copy = right(arr_copy)
    for i in range(2):
        arr_copy = rotate_90(arr_copy)
    recursive(arr_copy, cnt + 1)
    
    # 위쪽
    arr_copy = copy.deepcopy(arr)
    for i in range(3):
        arr_copy = rotate_90(arr_copy)
    arr_copy = right(arr_copy)
    arr_copy = rotate_90(arr_copy)
    recursive(arr_copy, cnt + 1)
    
recursive(arr, 0)

print(max_num)

'''
4
2 2 4 16
0 0 0 0
0 0 0 0
0 0 0 0
'''