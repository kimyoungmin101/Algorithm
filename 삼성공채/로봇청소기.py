from os import chroot


N, M = map(int, input().split())

r,c,d = map(int ,input().split())

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

direction = [[-1, 0],[0,1],[1,0],[0,-1]] # 북, 동, 남, 서

cnt_robot = [r,c] # 현재 로봇 청소기의 위치
rotate_cnt = 0
cnt = 0

is_ans = False

while True:
    # 1. 현재 위치를 청소한다.
    if arr[cnt_robot[0]][cnt_robot[1]] == 0:
        arr[cnt_robot[0]][cnt_robot[1]] = 2
        cnt += 1
    
    while True:
        
        # 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
        if rotate_cnt == 4:
            if d == 0:
                new_d = 2
            elif d == 1:
                new_d = 3
            elif d == 2:
                new_d = 0
            else:
                new_d = 1
        
            X_result = direction[new_d][0]
            Y_result = direction[new_d][1]
            X_result += cnt_robot[0]
            Y_result += cnt_robot[1]
            
            if arr[X_result][Y_result] == 1:
                is_ans = True
                break
            else:
                cnt_robot[0] = X_result
                cnt_robot[1] = Y_result
                rotate_cnt = 0
                continue
            
        # 2-a : 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.        
        if d - 1 < 0:
            new_d = 3
        else:
            new_d = d - 1
        
        new_X, new_Y = direction[new_d]
        new_X += cnt_robot[0]
        new_Y += cnt_robot[1]
        
        if arr[new_X][new_Y] == 0:
            cnt_robot[0] = new_X
            cnt_robot[1] = new_Y
            d = new_d
            rotate_cnt = 0
            break
        # 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.    
        elif arr[new_X][new_Y] != 0:
            d = new_d
            rotate_cnt += 1
            continue
    
    if is_ans:
        break
    
print(cnt)
