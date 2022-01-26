# https://www.acmicpc.net/problem/1932 

N = int(input())

dp_graph = []
graph = []
for i in range(N):
    arr = [0 for _ in range(i+1)]
    dp_graph.append(arr)

    graph.append(list(map(int, input().split())))
dp_graph[0][0] = graph[0][0]

dx = [1,1] # 아래, 왼쪽아래, 오른쪽아래
dy = [0,1]

for i in range(len(graph)):
    for j in range(len(graph[i])):
        for k in range(2):
            X = dx[k] + i
            Y = dy[k] + j
            
            if X < 0 or Y < 0 or Y >= (len(graph[i]) + 2) or X >= (N):
                continue
            
            if dp_graph[i][j] + graph[X][Y] > dp_graph[X][Y]:
                dp_graph[X][Y] = dp_graph[i][j] + graph[X][Y]


print(max(dp_graph[-1]))