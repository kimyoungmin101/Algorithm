from collections import deque

N, L, R = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int ,input().split())))


open = [[False for _ in range(N)] for _ in range(N)]

def bfs(X, Y):
    global L
    global R
    visited = [[X, Y]]
    sum_result = arr[X][Y]

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]    

    queue = deque()
    queue.append([X, Y])

    while queue:
        new_X, new_Y = queue.popleft()
        if open[new_X][new_Y] == False:
            open[new_X][new_Y] = True
        else:
            continue

        for i in range(4):
            real_X = dx[i] + new_X
            real_Y = dy[i] + new_Y

            if real_X < 0 or real_Y < 0 or real_X >= len(arr) or real_Y >= len(arr) or open[real_X][real_Y] == True:
                continue
            A = abs(arr[real_X][real_Y] - arr[new_X][new_Y])
            if [real_X, real_Y] not in visited and L <= A and A <= R:
                visited.append([real_X, real_Y])
                sum_result += arr[real_X][real_Y]
                queue.append([real_X, real_Y])
    
    for i in visited:
        arr[i[0]][i[1]] = sum_result // len(visited)
    return arr
import copy
cnt = 0
while True:
    
    cnt_arr = copy.deepcopy(arr)
    continue_value = False
    for i in cnt_arr:
        print(i)
    print(' ')
    for i in range(N):
        for j in range(N):
            if open[i][j] == False:
                arr = bfs(i, j)

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != cnt_arr[i][j]:
                continue_value = True
    
    if continue_value == False:
        break
    cnt += 1
    
    open = [[False for _ in range(N)] for _ in range(N)]

print(cnt)