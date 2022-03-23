# https://www.acmicpc.net/problem/16234 인구 이동
from collections import deque
import copy

N, L, R = map(int, input().split())

populations = []

for i in range(N):
    populations.append(list(map(int, input().split())))
    
    
dx = [1,-1,0,0]
dy = [0,0,1,-1]

cnt = 0

while True:
    first_poputlations = copy.deepcopy(populations)
    continue_value = False
    
    visited = [[False for _ in range(N)] for _ in range(N)]
    
    ans = []
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == True:
                continue
            
            queue = deque([[i, j]])
            add_result = [[i, j]]
            
            while queue:
                X, Y = queue.popleft()
                
                for q in range(4):
                    real_X = X + dx[q]
                    real_Y = Y + dy[q]
                    
                    if real_X < 0 or real_Y < 0 or real_X >= N or real_Y >= N:
                        continue
                    
                    A = abs(populations[real_X][real_Y] - populations[X][Y])
                    if R >= A and L <= A and visited[real_X][real_Y] == False and [real_X, real_Y] not in add_result:
                        visited[real_X][real_Y] = True
                        add_result.append([real_X, real_Y])
                        queue.append([real_X, real_Y])
                        
            sum_result = 0
            
            if len(add_result) != 1:
                ans.append(add_result)
    
    
    for z in ans:
        sum_result = 0
        if len(z) >= 1:
            for q in z:
                sum_result += populations[q[0]][q[1]]
            for x in z:
                populations[x[0]][x[1]] = sum_result // len(z)
    
    for i in range(len(populations)):
        for j in range(len(populations)):
            if populations[i][j] != first_poputlations[i][j]:
                continue_value = True
                
    if continue_value == False:
        break
    
    cnt += 1

print(cnt)