# https://www.acmicpc.net/problem/16236 삼성 기출문제
from collections import deque
import copy

N = int(input())

arr = []
size = [2,0]

for i in range(N):
    arr.append(list(map(int, input().split())))

cnt_where = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            cnt_where.append(i)
            cnt_where.append(j)

arr[cnt_where[0]][cnt_where[1]] = 0

def bfs():
    arr_copy = copy.deepcopy(arr)

    for i in range(N):
        for j in range(N):
            if arr_copy[i][j] > size[0] and arr_copy[i][j] != 9:
                arr_copy[i][j] = 100
            else:
                arr_copy[i][j] = 0
    

    queue = deque([[cnt_where[0], cnt_where[1]]])

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while queue:
        X, Y = queue.popleft()
        
        for i in range(4):
            real_X = X + dx[i]
            real_Y = Y + dy[i]

            if real_X < 0 or real_Y < 0 or real_X >= N or real_Y >= N or arr_copy[real_X][real_Y] == 100:
                continue  
            if arr_copy[real_X][real_Y] != 0 or (real_X == cnt_where[0] and real_Y == cnt_where[1]):
                continue
            arr_copy[real_X][real_Y] = arr_copy[X][Y] + 1
            queue.append([real_X,real_Y])

    return arr_copy

def find_to_eat():
    find_eat = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] < size[0] and arr[i][j] != 0:
                find_eat.append([i,j])
    
    return find_eat

cnt_value = 0
cnt = 0
while True:
    can_eat = find_to_eat() # [0,3], [3,0]
    if len(can_eat) == 0:
        break
    bfs_result = bfs()
    result = []
    
    cnt += 1
    
    for i in can_eat:
        result.append([bfs_result[i[0]][i[1]], i[0], i[1]])
    
    result = sorted(result, key = lambda X : (X[0], X[1], X[2]))
    while result:
        if result[0][0] == 0:
            result.pop(0)
        else:
            break
    if len(result) == 0:
        break

    cnt_value += result[0][0]
    size[1] += 1
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    arr[result[0][1]][result[0][2]] = 0

    cnt_where = [result[0][1], result[0][2]]
    
print(cnt_value)