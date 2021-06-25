from sys import stdin
from collections import deque
N, M = map(int, stdin.readline().split())

# matrix 배열
matrix = [[0] * N for _ in range(M)]
visited = [[0]* N for _ in range(M)]

for i in range(M):
    listM = list(map(int , stdin.readline().split()))
    matrix[i] = listM

queue = [(0,0)]

# 좌/우/위/아래 방향 이동
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

queue = deque([])

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if(matrix[i][j] == 1):
            queue.append([i,j])

while(queue):
    Q = queue.popleft()
    X = Q[0]
    Y = Q[1]
    
    for i in range(4):
        nx = X + dx[i]
        ny = Y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if visited[nx][ny] == 0 and matrix[nx][ny] == 0:
                visited[nx][ny] = visited[X][Y] + 1
                queue.append([nx,ny])


def answer(matrix, visited):
    max = 0
    
    for i in range(M):
        for j in range(N):
            if(matrix[i][j] == 0 and visited[i][j] == 0):
                return -1
            else:
                if(max < visited[i][j]):
                    max = visited[i][j]
    return max

ans = answer(matrix, visited)
print(ans)
