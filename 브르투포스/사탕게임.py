N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(str,input().strip())))

def find_eat(graph_candy, X, Y):
    # 0, 0
    arr_X = graph_candy[X]
    arr_Y = [graph[i][Y] for i in range(N)]

    x_count = 1
    x_cnt = 1

    y_count = 1
    y_cnt = 1
    # PPXPPP
    for i in range(1, len(arr_X)):
        if(arr_X[i-1] == arr_X[i]):
            x_cnt += 1
            x_count = max(x_count, x_cnt)
        else:
            x_cnt = 1
            
        
    for i in range(1, len(arr_Y)):
        if(arr_Y[i-1] == arr_Y[i]):
            y_cnt += 1
            y_count = max(y_count, y_cnt)
        else:
            y_cnt = 1

    return max(x_count, y_count)

result = find_eat(graph, 0, 0)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
max_result = 0

for i in range(N):
    for j in range(N):
        max_result = max(max_result, find_eat(graph, i, j))
        for k in range(4):
            X = dx[k] + i
            Y = dy[k] + j
            if(X < 0 or Y < 0 or X >= N or Y >= N):
                continue
            if(graph[i][j] != graph[X][Y]):
                graph[i][j], graph[X][Y] = graph[X][Y], graph[i][j]
                max_result = max(max_result, find_eat(graph, i, j))
                graph[i][j], graph[X][Y] = graph[X][Y], graph[i][j]

print(max_result)