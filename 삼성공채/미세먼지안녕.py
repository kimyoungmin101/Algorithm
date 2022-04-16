# https://www.acmicpc.net/problem/17144

from collections import deque

R, C, T = map(int, input().split())

board = []
for i in range(R):
    board.append(list(map(int, input().split())))
    
clean = []    


def getQueue(newBoard):    
    queue = deque()
    
    for i in range(len(newBoard)):
        for j in range(len(newBoard[i])):
            if newBoard[i][j] == -1:
                clean.append([i,j])
            elif newBoard[i][j] == 0:
                continue
            else:
                queue.append([i,j, newBoard[i][j]])
    return queue


dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(T):
    queue = getQueue(board)
    
    newBoard = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    newBoard[clean[0][0]][clean[0][1]] = -1
    newBoard[clean[1][0]][clean[1][1]] = -1
    
    while queue:
        X, Y, value = queue.popleft()
        
        changeCnt = 0
        
        for j in range(4):
            newX = X + dx[j]
            newY = Y + dy[j]
            
            if newX < 0 or newY < 0 or newX >= len(board) or newY >= len(board[0]):
                continue
            
            if board[newX][newY] == -1:
                continue
            
            changeCnt += 1
            newBoard[newX][newY] += (value // 5)
        
        if changeCnt != 0:
            newValue = value - ((value // 5) * changeCnt)
            newBoard[X][Y] += newValue
    
    
    upRotate = clean[0]
    downRotate = clean[1]
    
    # 윗 방향 회전
    upX = upRotate[0]
    upY = upRotate[1]
    newRoateUp = []
    newRoateUp = newBoard[upX][:]
    for a in range(upX-1,-1,-1):
        newRoateUp.append(newBoard[a][len(newBoard[0])-1])
    
    for a in range(len(newBoard[0])-2,-1,-1):
        newRoateUp.append(newBoard[0][a])
    
    for a in range(1, upX):
        newRoateUp.append(newBoard[a][0])
    
    newRoateUp = deque(newRoateUp)
    newRoateUp.rotate(1)
    newRoateUp[0] = -1
    newRoateUp[1] = 0

    # attach
    cnt = 0
    for a in range(len(newBoard[upX])):
        newBoard[upX][cnt] = newRoateUp[cnt]
        cnt += 1
        
    for a in range(upX-1,-1,-1):
        newBoard[a][len(newBoard[0])-1] = newRoateUp[cnt]
        cnt += 1
    
    for a in range(len(newBoard[0])-2,-1,-1):
        newBoard[0][a] = newRoateUp[cnt]
        cnt += 1
    
    for a in range(1, upX):
        newBoard[a][0] = newRoateUp[cnt]
        cnt += 1
    
    
    # 아랫 방향 회전
    downX = downRotate[0]
    downY = downRotate[1]
    
    newRoateDown = []
    newRoateDown = newBoard[downX][:]
    
    for a in range(downX+1, len(newBoard)):
        newRoateDown.append(newBoard[a][len(newBoard[0])-1])
    
    for a in range(len(newBoard[0])-2,-1,-1):
        newRoateDown.append(newBoard[len(newBoard)-1][a])
            
    for a in range(len(newBoard)-2, downX, -1):
        newRoateDown.append(newBoard[a][0])
    
    newRotate = deque(newRoateDown)
    newRotate.rotate(1)
    newRotate[0] = -1
    newRotate[1] = 0
    
    # 아래 attach
    cnt = 0
    for a in range(len(newBoard[downX])):
        newBoard[downX][cnt] = newRotate[cnt]
        cnt += 1
            
    for a in range(downX+1, len(newBoard)):
        newBoard[a][len(newBoard[0])-1] = newRotate[cnt]
        cnt += 1
        
    for a in range(len(newBoard[0])-2,-1,-1):
        newBoard[len(newBoard)-1][a] = newRotate[cnt]
        cnt += 1
    
    for a in range(len(newBoard) -2 , downX, -1):
        newBoard[a][0] = newRotate[cnt]
        cnt += 1
    
    board = newBoard[:]
    
answer = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == -1:
            continue
        else:
            answer += board[i][j]

print(answer)