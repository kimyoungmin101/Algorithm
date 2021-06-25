import sys
from collections import deque
N = int(sys.stdin.readline())

arr = [[0] * (N+2) for _ in range(N+2)]
visited = [[True] * (N+2) for _ in range(N+2)]

for i in range(1, N+1):
    A = str(sys.stdin.readline())
    for j in range(1, len(A)):
        arr[i][j] = int(A[j-1])
        if arr[i][j] == 1:
            visited[i][j] = False

def bfs(i, j, count):
    queue = deque([])
    queue.append([i,j])
    while(queue):
        count += 1
        A = queue.popleft()
        i = A[0]
        j = A[1]
        if(arr[i+1][j] == 1 and visited[i+1][j] == False):
            queue.append([i+1, j])
            visited[i+1][j] = True
        if(arr[i][j+1] == 1 and visited[i][j+1] == False):
            queue.append([i, j+1])
            visited[i][j+1] = True
        if(arr[i][j-1] == 1 and visited[i][j-1] == False):
            queue.append([i, j-1])
            visited[i][j-1] = True
        if(arr[i-1][j] == 1 and visited[i-1][j] == False):
            queue.append([i-1, j])
            visited[i-1][j] = True
    return count

ans = []

for i in range(1, len(arr)-1):
    for j in range(1, len(arr[i])-1):
        if(arr[i][j] == 1 and visited[i][j] == False):
            count = 0
            visited[i][j] = True
            Q = bfs(i,j, count)
            ans.append(Q)

print(len(ans))
ans.sort()
for i in ans:
    print(i)

'''

import sys
read = lambda : sys.stdin.readline().strip()

n = int(read())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(matrix, cnt, x, y):
    matrix[x][y]=0
    # 이건 이제 이미 간것이다. 그래서 0으로 바꾼다
    queue = []
    queue.append((x, y))
    while queue:
        x, y = queue.pop()
        for k in range(0, 4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx and nx< n and 0<= ny and ny <n:
                if matrix[nx][ny] == 1:
                    cnt += 1
                    matrix[nx][ny] = 0
                    queue.append((nx, ny))
    return cnt

matrix = [list(map(int, list(read()))) for _ in range(n)]
# matrix에 input값 넣기

cnt = 0
ans = []
for i in range(n):
    for j in range(n):
        if matrix[i][j]==1:
            # 일단 1로 뭔가의 그룹이다.
            ans.append(bfs(matrix, cnt+1, i, j))
            # 여기서 이제 그 주위에 있는 것들 다 돌아보는것이다.
print(len(ans))
for i in sorted(ans):
    print(i)
'''
