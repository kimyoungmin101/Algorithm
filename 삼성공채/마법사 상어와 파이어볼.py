# https://www.acmicpc.net/problem/20056

N, M, K = map(int, input().split())

fire = []

board = [[[] for _ in range(N)] for _ in range(N)]

for i in range(M):
    arr = list(map(int,input().split()))
    arr[0] -= 1
    arr[1] -= 1
    fire.append(arr)
    
    # X, Y = arr[0]-1, arr[1]-1
    # board.append([arr[2], arr[3], arr[4]])
    


# 1 1 5 2 2
# r c m s d

# 방향
dir = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]

#  ri, ci, mi, si, d

while K:
    # 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다. 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
    
    board = [[[] for _ in range(N)] for _ in range(N)]
    
    for idx, value in enumerate(fire):
        si = value[3]
        for i in range(si):
            di = value[4]
            
            X = (value[0] + (si * dir[di][0])) % N
            Y = (value[1] + (si * dir[di][1])) % N
            
            if X < 0:
                X = N - 1
            if Y < 0:
                Y = N - 1
        
        board[X][Y].append([X,Y, value[2], value[3], value[4]])
    
    # 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
    fire = []
    
    for i in range(N):
        for j in range(N):
            len_board = len(board[i][j])
            is_left = False # 홀수
            is_right = False # 짝수
            weight = 0
            speed = 0
            
            if len_board == 1:
                fire.append(board[i][j][0])
            
            if len_board >= 2:    
                for k in board[i][j]:
                    weight += k[2]
                    speed += k[3]
                    
                    if k[4] % 2 == 0:
                        is_right = True
                    else:
                        is_left = True
                
                weight //= 5
                
                if weight == 0:
                    continue
                
                speed //= len_board
                
                if (is_right == True and is_left == False) or (is_right == False and is_left == True):
                    fire.append([i,j, weight, speed, 0])
                    fire.append([i,j, weight, speed, 2])
                    fire.append([i,j, weight, speed, 4])
                    fire.append([i,j, weight, speed, 6])
                else:
                    fire.append([i,j, weight, speed, 1])
                    fire.append([i,j, weight, speed, 3])
                    fire.append([i,j, weight, speed, 5])
                    fire.append([i,j, weight, speed, 7])
    
    K -= 1

result = 0
for X in fire:
    result += X[2]

print(result)

