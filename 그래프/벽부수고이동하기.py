import sys
from collections import deque
'''
9 9 
010001000
010101010
010101010
010101010
010101010
010101010
010101010
010101011
000100010
    
ANSWER : 33
WA : -1 

6 6
010001
010101
010101
010101
010110
000110
Answer : 21
WA : -1
'''

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append([0, 0, 0])
    
    visit = [[[0,0] for _ in range(m)] for _ in range(n)] # 벽을 안부수고 지나간거리 , 벽을 부수고 지나간거리
    
    while q:
        X,Y,W = q.popleft()
        
        
        if X == n-1 and Y == m-1:
            return visit[X][Y][W] + 1
        # q -> X Y (벽을 안부심 : 0 / 부심 : 1)
        for i in range(4):
            new_X = X + dx[i]
            new_Y = Y + dy[i]
            
            if new_X < 0 or new_Y < 0 or new_X >= n or new_Y >= m:
                continue
            
            if s[new_X][new_Y] == 1 and W == 0: # 벽을 안 부순 경우와 다음 지나갈 자리가 1 인경우
                q.append([new_X, new_Y, 1])
                visit[new_X][new_Y][1] = visit[X][Y][W] + 1
            elif s[new_X][new_Y] == 0 and visit[new_X][new_Y][W] == 0:
                q.append([new_X, new_Y, W])
                visit[new_X][new_Y][W] = visit[X][Y][W] + 1
                
    return -1

n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, list(input().strip()))))
print(bfs())
