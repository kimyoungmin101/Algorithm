import sys, copy, collections
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
max_num = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
empty_list = []
virus_list = []

EMPTY = 0
WALL = 1
VIRUS = 2

# 입력
g = [[0]*m for _ in range(n)]

for y in range(n):
    raw = [int(x) for x in sys.stdin.readline().split()]

    for x in range(m):
        g[y][x] = raw[x]
        if g[y][x] == EMPTY:
            empty_list.append([y, x])
        if g[y][x] == VIRUS:
            virus_list.append([y, x])

# bfs 탐색
def bfs(ng):
    q = collections.deque([])
    visited = [[False]*m for _ in range(n)]
    cnt = 0
    global max_num

    for virus in virus_list:
        q.append(virus)

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if ng[ny][nx] == EMPTY and visited[ny][nx] == False:
                q.append([ny, nx])
                ng[ny][nx] = VIRUS
                visited[ny][nx] = True
    
    for i in range(n):
        cnt += ng[i].count(EMPTY)
    
    if max_num < cnt:
        max_num = cnt


# 벽 세우기
for i in combinations(empty_list, 3):
    dx1, dy1 = i[0][0], i[0][1]
    dx2, dy2 = i[1][0], i[1][1]
    dx3, dy3 = i[2][0], i[2][1]

    g[dx1][dy1] = WALL
    g[dx2][dy2] = WALL
    g[dx3][dy3] = WALL
    
    ng = copy.deepcopy(g)
    bfs(ng)

    g[dx1][dy1] = EMPTY
    g[dx2][dy2] = EMPTY
    g[dx3][dy3] = EMPTY

print(max_num)

