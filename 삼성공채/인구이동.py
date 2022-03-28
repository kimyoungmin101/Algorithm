'''
2 20 50
50 30
20 40

'''
import copy
from collections import deque

N, L, R = map(int, input().split())
people = []

for i in range(N):
    people.append(list(map(int, input().split())))
    
day = 0

def bfs(arr):
    global L, R
    
    visited = [[False for _ in range(len(arr))] for _ in range(len(arr))]
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    visit = []
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            ans = []
            if visited[i][j] == False:
                queue = deque([])
                queue.append([i, j])
                                
                while queue:
                    X, Y = queue.popleft()
                    if visited[X][Y]:
                        continue
                    ans.append([X, Y])
                    visited[X][Y] = True
                    
                    for a in range(4):
                        real_X = X + dx[a]
                        real_Y = Y + dy[a]
                        
                        if real_X < 0 or real_Y < 0 or real_X >= len(arr) or real_Y >= len(arr):
                            continue
                        if visited[real_X][real_Y] == True:
                            continue
                        
                        A = abs(arr[real_X][real_Y] - arr[X][Y])
                        
                        if L <= A <= R:
                            queue.append([real_X, real_Y])
                        
            
                visit.append(ans)
                
    for i in visit:
        sum_arr = 0
        if len(i) == 1:
            continue
        
        for j in i:
            sum_arr += arr[j[0]][j[1]]
            
        sum_arr //= len(i)
        
        for j in i:
            arr[j[0]][j[1]] = sum_arr
    
    return arr


while True: # 인구이동 전이랑 인구이동 이후가 같으면 Break
    before_day = copy.deepcopy(people)
    
    
    after_day = bfs(before_day)
        
    if people == after_day:
        break
    else:
        people = copy.deepcopy(after_day)
        day += 1

print(day)