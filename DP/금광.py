N = int(input())

for i in range(N):
    Q, W = map(int, input().split()) # 3, 4
    graph = list(map(int, input().split()))
    dp_graph = [[0 for _ in range(W)] for _ in range(Q)]
    new_graph = []
    for k in range(W, len(graph)+1, W):
        new_graph.append(graph[k-W:k])
    for s in range(Q):
        dp_graph[s][0] = new_graph[s][0]
        
    dx = [0,-1,1]
    dy = [1,1,1] # 오른쪽, 오른쪽 위, 오른쪽 아래
    for h in range(W):
        for l in range(Q):
            
            for f in range(3):
                X = dx[f] + l
                Y = dy[f] + h
                if X < 0 or Y < 0 or X >= Q or Y >= W:
                    continue
                
                if new_graph[X][Y] + dp_graph[l][h] > dp_graph[X][Y]:
                    dp_graph[X][Y] = new_graph[X][Y] + dp_graph[l][h]
    max_result = 0
    for e in range(Q):
        max_result = max(dp_graph[e][W-1], max_result)
    print(' ')
    print('max_result : ', max_result)

'''
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

'''
