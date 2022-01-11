# 메모리 초과에 주의 할려면 dic형식으로 저장해야함 이차원 배열은 안돼 !~!
from collections import deque
import sys

N, M, K, X = map(int, sys.stdin.readline().split())

graph_dic = {}

visited = [False for _ in range(N)]

for i in range(M):
    Q, W = map(int, sys.stdin.readline().split())
    Q -= 1
    W -= 1

    if Q not in graph_dic:
        graph_dic[Q] = [W]
    else:
        A = graph_dic[Q]
        A.append(W)
        graph_dic[Q] = A


distance = [10000 for _ in range(N)] # 0 0 0 0

def dkstra(start):
    queue = deque([])
    distance[start] = 0
    visited[start] = True

    for i in graph_dic[start]:
        distance[i] = 1
        queue.append(i)
    
    while len(queue) != 0:
        A = queue.popleft() # 1, 2
            
        if A in graph_dic and visited[A] == False:
            visited[A] = True
            for j in graph_dic[A]:
                queue.append(j)
                if distance[j] > distance[A] + 1:
                    distance[j] = distance[A] + 1
                    
    return distance

result_graph = dkstra(X-1) # 시작하는 지점 X를 넣어준다.

if K not in result_graph:
    print(-1)
else:
    for i in range(len(result_graph)):
        if result_graph[i] == K:
            print(i + 1)
