# 편집거리
'''
cat
cut

sunday
saturday

'''

A = str(input())
B = str(input())

C = list(map(str, A.strip()))
D = list(map(str, B.strip()))
arr_A = []
arr_B = []

if len(C) > len(D):
    arr_A = C
    arr_B = D
else:
    arr_A = D
    arr_B = C
    
board = [[0 for _ in range(len(arr_A)+1)] for _ in range(len(arr_B) + 1)]

for i in range(1, len(board[0])):
    board[0][i] = i
for i in range(1, len(board)):
    board[i][0] = i
    
for i in range(1, len(board)):
    for j in range(1, len(board[i])):
        if arr_A[j-1] == arr_B[i-1]:
            board[i][j] = board[i-1][j-1]
        else:
            board[i][j] = min(board[i-1][j-1]+1, board[i-1][j]+1, board[i][j-1]+1)

print(board[-1][-1])