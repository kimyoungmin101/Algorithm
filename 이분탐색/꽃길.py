# https://www.acmicpc.net/problem/14620
import sys

N = int(input())
board = []
visited = []
for i in range(N):
    visited.append([False for _ in range(N)])
    
for i in range(N):
    board.append(list(map(int, input().split())))

min_money = sys.maxsize

def attach(arr):
    for i in arr:
        X = i[0]
        Y = i[1]
        visited[X][Y] = True

def deatch(arr):
    for i in arr:
        X = i[0]
        Y = i[1]
        visited[X][Y] = False

def dfs(cnt, sum_result):
    global min_money
    
    if cnt == 3:
        min_money = min(sum_result, min_money)
        return
    
    direction = [[1,0], [0,1], [-1,0], [0,-1]]
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                arr = [[i,j]]
                sum_arr = [board[i][j]]
                
                for k in range(4):
                    dx = direction[k][0] + i
                    dy = direction[k][1] + j
                    
                    
                    if dx < 0 or dy < 0 or dx >= N or dy >= N:
                        break
                    
                    if visited[dx][dy] == True:
                        break
                    arr.append([dx, dy])
                    sum_arr.append(board[dx][dy])
                    
                if len(arr) == 5:
                    attach(arr)
                    dfs(cnt + 1, sum_result + sum(sum_arr))
                    deatch(arr)
                    
dfs(0, 0)

print(min_money)