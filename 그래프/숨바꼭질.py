# 알고리즘 교재 P390

import heapq
import sys

N, M = map(int, input().split())
map_graph = [[sys.maxsize for _ in range(N)] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    
    map_graph[A][B] = 1
    map_graph[B][A] = 1

for i in range(N):
    map_graph[i][i] = 0

visited = [False for _ in range(N)]
min_distance = [sys.maxsize for _ in range(N)]

'''
heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)


while heap:
    print(heapq.heappop(heap))
'''
def dkstra(X):
    heap = []
    for i in range(len(map_graph[X])):
        if map_graph[X][i] != 0:
            min_distance[i] = min(min_distance[i], map_graph[X][i])
            heapq.heappush(heap, [map_graph[X][i], X, i])
    
    while heap:
        distance, A, B = heapq.heappop(heap)
        # 0 1 1 max max max
        for k in range(len(map_graph[B])):
            if min_distance[k] > min_distance[B] + map_graph[B][k]:
                min_distance[k] = min_distance[B] + map_graph[B][k]
                heapq.heappush(heap, [min_distance[k], B, k])
    return

min_distance[0] = 0
visited[0] = True
dkstra(0)

max_num = max(min_distance) # 2
num_cnt = min_distance.count(max_num) # 3
result_num = 0 # 4
for i in range(len(min_distance)):
    if max_num == min_distance[i]:
        result_num = i + 1
        break

print(result_num, end= " ")
print(max_num, end= " ")
print(num_cnt)

'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''