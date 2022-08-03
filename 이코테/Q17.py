import heapq

N, K = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    
S, X, Y = map(int, input().split())
X -= 1
Y -= 1

virus = []

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            heapq.heappush(virus, [graph[i][j], i, j])
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(S):
    new_virus = []
    
    while virus:
        A, B, C = heapq.heappop(virus)
        
        for i in range(4):
            new_X = B + dx[i]
            new_Y = C + dy[i]
            
            if new_X < 0 or new_Y < 0 or new_X >= N or new_Y >= N:
                continue
            
            if graph[new_X][new_Y] == 0:
                graph[new_X][new_Y] = A
                new_virus.append([A, new_X, new_Y])
    
    virus = new_virus.copy()

print(graph[X][Y])