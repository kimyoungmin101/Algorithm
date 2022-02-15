import copy
import heapq

fish_arr = [] # 물고기가 담긴 리스트
arrow_arr = [] # 방향이 담긴 리스트
cnt_shark = [0,0]

for i in range(4):
    fish = []
    arrow = []
    A = list(map(int, input().split()))
    for j in range(len(A)):
        if j % 2 == 0: # 짝수이면   
            fish.append(A[j])
        else: # 홀수이면
            arrow.append(A[j])
    fish_arr.append(fish)
    arrow_arr.append(arrow)

def find_idx(X):
    for i in range(len(fish_arr)):
        for j in range(len(fish_arr[i])):
            if fish_arr[i][j] == X:
                return i , j

arrow_str = ['↑', '↖', '←', '↙', '↓', '↘', '→', '↗']

def move_fish(fish_arr, arrow_arr, cnt_shark):
    fish_arr[cnt_shark[0]][cnt_shark[1]] = 0 # 상어에게 먹힌 물고기는 임의의값 0으로 바꾸어준다.

    heap = []

    for i in range(len(fish_arr)):
        for j in range(len(fish_arr[i])):
            if fish_arr[i][j] != 0:
                heapq.heappush(heap, [fish_arr[i][j]])
    # 가장 작은 물고기부터 이동 할 수 있도록 heap에 담아준다.
    
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,-1,-1,-1,0,1,1,1]

    while heap:
        size = heapq.heappop(heap) # 움직여야하는 물고기 (크기, X좌표, Y좌표)
        
        idx_X, idx_Y = find_idx(size[0])
        
        arrow_idx = arrow_arr[idx_X][idx_Y] - 1 # 방향
        move_idx = [dx[arrow_idx], dy[arrow_idx]]
        
        cnt_index = 0
        while cnt_index < 8:
            
            next_X = idx_X + move_idx[0]
            next_Y = idx_Y + move_idx[1]

            if (next_X == cnt_shark[0] and next_Y == cnt_shark[1]) or next_X < 0 or next_Y < 0 or next_X >= len(fish_arr) or next_Y >= len(fish_arr): 
                # 인덱스 벗어나면 continue: # 이동할 위치에 상어가 있으면 continue
                arrow_idx = (arrow_idx + 1) % 8
                move_idx[0] = dx[arrow_idx] # 시계방향으로 45도 돌려준다.
                move_idx[1] = dy[arrow_idx]
                cnt_index += 1
                continue
            
            change_fish_value = fish_arr[next_X][next_Y]
            fish_arr[next_X][next_Y] = fish_arr[idx_X][idx_Y]
            fish_arr[idx_X][idx_Y] = change_fish_value

            arrow_arr[idx_X][idx_Y] = arrow_arr[next_X][next_Y]
            arrow_arr[next_X][next_Y] = arrow_idx

            break

        


'''
cnt = [0,0] ↘
[0, 2, 9, 10]
[6, 12, 1, 14]
[16, 5, 15, 13]
[3, 4, 11, 8]
count = 7
'''

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

result = 0
def dfs(array_fish, array_arrow , now_x, now_y, total):
    for i in array_fish:
        print(i)
    print('')
    global result

    array_fish = copy.deepcopy(array_fish)
    array_arrow = copy.deepcopy(array_arrow)

    total += array_fish[now_x][now_y]
    array_fish[now_x][now_y] = 0
    shark = [now_x, now_y]

    move_fish(array_fish, array_arrow, shark)

    for i in array_fish:
        print(i)
    print('')
    cnt_arrow = array_arrow[now_x][now_y] - 1
    
    positions = []
    for i in range(4):
        now_x += dx[cnt_arrow]
        now_y += dy[cnt_arrow]

        if now_x < 0 or now_y < 0 or now_x >= 4 or now_y >= 4:
            continue
        positions.append((now_x, now_y))
    
    if len(positions) == 0:
        result = max(result, total)
        return

    for next_x, next_y in positions:
        dfs(array_fish, array_arrow , next_x, next_y, total)

    
dfs(fish_arr, arrow_arr, 0, 0, 0)
print(result)
