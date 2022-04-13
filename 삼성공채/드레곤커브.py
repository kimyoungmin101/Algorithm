# https://www.acmicpc.net/problem/15685

board = [[0 for _ in range(101)] for _ in range(101)]

N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    

dxdy = [[0,1], [-1,0], [0, -1], [1,0]] # 오른쪽, 위쪽, 왼쪽, 아래쪽

curved = [[] for _ in range(11)]
curved[1] = [-1]
curved[2] = [-1,-1,1] 

for i in range(3,11):
    # 왼쪽은 -1 오른쪽은 1
    sample = curved[i-1].copy()
    sample.append(-1)
    
    for j in range(len(curved[i-1]) - 1, -1, -1):
        if curved[i-1][j] == 1:
            sample.append(-1)
        else:
            sample.append(1)
            
    curved[i] = sample

for i in arr:
    X, Y ,D, G = i
    
    board[Y][X] = 1
    
    curve_result = curved[G]
    
    for j in range(len(curve_result) + 1):
        
        direction = dxdy[D]
        
        new_Y = Y + direction[0]
        new_X = X + direction[1] 
        
        if new_X > 100 or new_Y > 100 or new_X < 0 or new_Y < 0:
            break
        
        X = new_X
        Y = new_Y
    
        board[Y][X] = 1
        
        if len(curve_result) <= j:
            break
        
        if curve_result[j] == 1:
            D -= 1
            if D < 0:
                D = 3
        else:
            D += 1
            D %= 4

       
cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i+1][j] == 1 and board[i][j+1] == 1 and board[i+1][j+1] == 1:
            cnt += 1
            
print(cnt)
