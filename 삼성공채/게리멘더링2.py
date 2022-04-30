# https://www.acmicpc.net/problem/17779


N = int(input())

dic = {}
board = [[0 for _ in range(N)] for _ in range(N)]
likedic = {}

for i in range(N*N):
    dic[i+1] = []
    
    arr = list(map(int, input().split()))
    likedic[arr[0]] = arr[1:]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    resultAns = 0
    dicans = {}
    for j in range(5):
        dicans[j] = []
        
    #1) 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    for j in range(N):
        for k in range(N):
            ans = 0
            if board[j][k] == 0:
                for z in range(4):
                    newX = dx[z] + j
                    newY = dy[z] + k
                    if newX < 0 or newY < 0 or newX >= N or newY >= N:
                        continue
                    if board[newX][newY] in likedic[arr[0]]:
                        ans += 1
            else:
                continue
            resultAns = max(ans, resultAns)
            dicans[ans].append([j,k])

    if len(dicans[resultAns]) == 1:
        X, Y = dicans[resultAns][0]
        board[X][Y] = arr[0]
        continue
    
    cntAns = dicans[resultAns]
    # 2) 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    cnt = 0
    diccnt = {}
    
    for i in range(5):
        diccnt[i] = []
        
    for i in cntAns:
        ans = 0
        for j in range(4):
            newX = dx[j] + i[0]
            newY = dy[j] + i[1]
            if newX < 0 or newY < 0 or newX >= N or newY >= N:
                continue
            if board[newX][newY] == 0:
                ans += 1
        diccnt[ans].append([i[0],i[1]])
        cnt = max(cnt, ans)
    
    if len(diccnt[cnt]) == 1:
        X, Y = diccnt[cnt][0]
        board[X][Y] = arr[0]
        continue
    
    # 3) 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
    diccnt[cnt].sort()
    X, Y = diccnt[cnt][0]
    board[X][Y] = arr[0]

total = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(N):
    for j in range(N):
        ans = 0
        for k in range(4):
            newX = dx[k] + i
            newY = dy[k] + j
            if newX < 0 or newY < 0 or newX >= N or newY >= N:
                continue
            
            if board[newX][newY] in likedic[board[i][j]]:
                
                ans += 1
        # 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000
        if ans == 0:
            continue
        
        total += (10 ** (ans-1))
        
print(total)