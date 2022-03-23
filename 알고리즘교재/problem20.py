# https://www.acmicpc.net/problem/18428 감시 피하기

'''
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
'''

from itertools import combinations

N = int(input())
arr = []

for i in range(N):
    arr.append(list(map(str, input().split())))
    
students = []
techers = []
object = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'S':
            students.append([i,j])
        elif arr[i][j] == 'T':
            techers.append([i,j])
        else:
            object.append([i,j])

list_combi = list(combinations(object, 3))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
# 위 오 아 왼
def can_avoid(arr_i):
    # 위쪽으로 계속
    for i in techers:
        X = i[0]
        Y = i[1]
        # 위쪽
        real_X = X
        real_Y = Y
        while True:
            real_X += dx[0]
            if real_X < 0:
                break
            if arr_i[real_X][real_Y] == 'O':
                break
            if arr_i[real_X][real_Y] == 'S':
                return False
            
        # 오른쪽
        real_X = X
        real_Y = Y
        while True:
            real_Y += dy[1]
            if real_Y >= len(arr_i):
                break
            if arr_i[real_X][real_Y] == 'O':
                break
            if arr_i[real_X][real_Y] == 'S':
                return False
            
        # 아래쪽
        real_X = X
        real_Y = Y
        while True:
            real_X += dx[2]
            if real_X >= len(arr_i):
                break
            if arr_i[real_X][real_Y] == 'O':
                break
            if arr_i[real_X][real_Y] == 'S':
                return False
            
        # 왼쪽
        real_X = X
        real_Y = Y
        while True:
            real_Y += dy[3]
            if real_Y < 0:
                break
            if arr_i[real_X][real_Y] == 'O':
                break
            if arr_i[real_X][real_Y] == 'S':
                return False
            
    return True

result = 'NO'

for i in list_combi:
    
    for j in i:
        arr[j[0]][j[1]] = 'O'
    
    if can_avoid(arr):
        result = 'YES'
        break
    for j in i:
        arr[j[0]][j[1]] = 'X'   
    
print(result)