# https://www.acmicpc.net/problem/2252 위상정렬
from collections import deque

N, M = map(int , input().split())

def topology_sort(indegree, graph):
    result = []

    q = deque()

    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)

    while q:
        q_pop = q.popleft() #1
        result.append(q_pop)

        for i in graph[q_pop]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)    
    return result

indegree = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())    
    indegree[B] += 1
    graph[A].append(B)

ans = topology_sort(indegree, graph)

for i in ans:
    print(i, end = " ")