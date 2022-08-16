# 여행계획
'''
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
'''
N, M = map(int, input().split())
board = []

for i in range(N):
    board.append(list(map(int,input().split())))
    
number_arr = list(map(int,input().split()))

parent = [i for i in range(0, N)]

def union(X, Y):
    if find(X) != find(Y):
        if X < Y:
            parent[Y] = parent[X]
        elif Y < X:
            parent[X] = parent[Y]
                
    return parent

def find(X):
    if parent[X] == X:
        return X
    else:
        return find(parent[X])

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            parent = union(i, j)

get_first = parent[number_arr[0]]
is_bool = True
for i in range(1, len(number_arr)):
    if parent[number_arr[i]] != get_first:
        is_bool = False
        break

if is_bool:
    print('YES')
else:
    print('NO')
