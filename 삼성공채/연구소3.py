# https://www.acmicpc.net/problem/17142

# 0은 빈 칸, 1은 벽, 2는 바이러스의 위치

'''
7 3
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2
'''


import copy
from collections import deque
from curses.ascii import isdigit
from operator import is_

N, M = map(int, input().split())

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

virus = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus.append([i,j])

minCnt = 1e9
c_virus = []

def dfs(comb, depth):
    global minCnt
    if len(comb) == M:  # 종료 조건 1 : M개를 모두 선택했을 때
        c_virus.append(comb.copy())
        return
    elif depth == len(virus):  # 종료 조건 2: 리스트의 마지막 까지 탐색했을 때
        return
 
    # 현재 depth의 값 포함 재귀 호출
    comb.append(virus[depth])
    dfs(comb, depth + 1)
 
    # 현재 depth의 값 미포함 재귀 호출
    comb.pop()
    dfs(comb, depth + 1)
 
dfs(deque(), 0)

def bfs(value, newArr):
    global minCnt, N
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for i in range(N):
        for j in range(N):
            if newArr[i][j] == 1:
                newArr[i][j] = '-'
            elif newArr[i][j] == 2:
                newArr[i][j] = '*'
            elif newArr[i][j] == 0:
                newArr[i][j] = -1
    
    for i in value:
        newArr[i[0]][i[1]] = 0
    
    newCnt = 0
    
    while value:
        X, Y = value.popleft()
        
        for i in range(4):
            newX = X + dx[i]
            newY = Y + dy[i]
            
            if newX < 0 or newY < 0 or newX >= N or newY >= N:
                continue
            
            if newArr[newX][newY] == '-':
                continue
            if newArr[newX][newY] == '*':
                newArr[newX][newY] = 0
                
            if newArr[newX][newY] == -1 or newArr[newX][newY] == '*':
                value.append([newX, newY])
                newArr[newX][newY] = newArr[X][Y] + 1
                
                if minCnt < newArr[newX][newY]:
                    return 1e9
                
                newCnt = newArr[newX][newY]
            
    for i in newArr:
        print(i)
    print(' ')
    return newCnt
    '''
5 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
0 2 0 2 0
1 1 1 1 1
    '''
    
def checkArr(newArr):
    global N
    for i in range(N):
        for j in range(N):
            if newArr[i][j] == -1:
                return False
    return True

for value in c_virus:
    newArr = copy.deepcopy(arr)
    A = bfs(value, newArr)
    if checkArr(newArr):
        minCnt = min(A, minCnt)

if minCnt == 1e9:
    print(-1)
else:
    print(minCnt)