# 여행 계획
'''
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
'''

N, M = map(int , input().split())

board = []
for i in range(N):
    board.append(list(map(int, input().split())))

parent = [_ for _ in range(N)]

way = list(map(int, input().split()))

def find(value):
    if value == parent[value]:
        return value
    else:
        return find(parent[value])

def union(X, Y):
    parent_X = find(X)
    parent_Y = find(Y)
    
    if parent_X > parent_Y:
        parent[parent_X] = parent_Y
    elif parent_X == parent_Y:
        return parent
    else:
        parent[parent_Y] = parent_X
    
    return parent

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            parent = union(i, j)

def possible(arr, arr_value):
    parent_num = parent[arr_value[0]]
    for i in range(1, len(arr_value)):
        if parent_num != parent[arr_value[i]]:
            return False
        
    return True

if possible(parent, way):
    print('YES')
else:
    print('NO')


