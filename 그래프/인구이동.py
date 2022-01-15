from collections import deque
import copy
N, L, R = map(int, input().split())

conturies = []

for i in range(N):
    conturies.append(list(map(int, input().split())))

visited = [[False for _ in range(N)] for _ in range(N)]

def get_queue(queue, idx):
    global L, R

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        real_X = dx[i] + idx[0]
        real_Y = dy[i] + idx[1]

        cnt_value = conturies[idx[0]][idx[1]] # 10

        if real_X < 0 or real_Y < 0 or real_X >= N or real_Y >= N:
            continue
        
        value = conturies[real_X][real_Y] - cnt_value
        
        if value < 0:
            value = -value
        if value < L or value > R or visited[real_X][real_Y] == True:
            continue
        
        if visited[idx[0]][idx[1]] == False:
            visited[idx[0]][idx[1]] = True

        queue.append([real_X, real_Y])
        visited[real_X][real_Y] = True
    
    return queue
    

add_arr = []

def bfs(idx):
    queue = deque([])

    queue = get_queue(queue, idx)

    new_arr = [idx]
    while queue:
        A = queue.popleft()
        new_arr.append(A)
        queue = get_queue(queue, A)
    
    add_arr.append(new_arr)
    return
cnt = 0

cnt_conturies = copy.deepcopy(conturies)

while True:
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                bfs([i,j])
    
    while add_arr:
        A = add_arr.pop(0)
        add_result = 0
        len_result = len(A)
        for i in A:
            add_result += conturies[i[0]][i[1]]
        
        av_result = add_result // len_result

        for i in A:
            conturies[i[0]][i[1]] = av_result
    
    if cnt_conturies == conturies:
        break

    cnt_conturies = copy.deepcopy(conturies)

    

    cnt += 1
    
    add_arr = []

    visited = [[False for _ in range(N)] for _ in range(N)]


print(cnt)

'''
True True 
True False

False False
False False
'''