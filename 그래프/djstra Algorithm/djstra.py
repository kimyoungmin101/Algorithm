from queue import PriorityQueue
que = PriorityQueue()
INF = 999
N = 1 # 시작위치
n = 5
m = 6

adj_mat2 =   [[0,7,INF,INF,3,10,INF],
  [7,0,4,10,2,6,INF],
  [INF,4,0,2,INF,INF,INF],
  [INF,10,2,0,11,9,4],
  [3,2,INF,11,0,INF,5],
  [10,6,INF,9,INF,0,INF],
  [INF,INF,INF,4,5,INF,0]]

for _ in range(m):
    a, b, c = map(int, input().split())
    adj_mat2[a-1][b-1] = min(adj_mat2[a-1][b-1], c)

for i in range(len(adj_mat2)):
    for j in range(len(adj_mat2)):
        adj_mat2[i][i] = 0

visited = [False] * len(adj_mat2)
v = [INF] * len(adj_mat2)
v[N] = 0
parent = [None] * len(adj_mat2)
que = PriorityQueue()
que.put([adj_mat2[N][N], N, 0]) # 0 0 0

while que:
    A = que.get() # 20 5 3
    N = A[1] # 4
    if( visited[N] == False):
        visited[N] = True
    Q = adj_mat2[N]
    for i in range(len(Q)):
        if(Q[i] != 0 and Q[i] != INF):
            que.put([Q[i], i, N]) # 가중치, 인덱스, 부모노드 
            if(v[i] > Q[i] + v[N]):
                v[i] = Q[i] + v[N]
    print(v)
