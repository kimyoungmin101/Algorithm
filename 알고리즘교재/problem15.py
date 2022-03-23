# https://www.acmicpc.net/problem/18352 특정 거리의 도시 찾기 성공

'''
4 4 2 1
1 2
1 3
2 3
2 4
'''

from collections import deque

N, M, K, X = list(map(int, input().split()))

dic = {}

for i in range(M):
    A, B = map(int, input().split())
    if A not in dic:
        dic[A] = [B]
    else:
        new_A = dic[A]
        new_A.append(B)
        dic[A] = new_A

queue = deque([])
visited = [False for _ in range(N + 1)]

visited[X] = True
for i in dic[X]:
    visited[i] = True
    queue.append([i, 1])

cities = []

while queue:
    queue_left = queue.popleft() # [2,1]
    if queue_left[1] == K:
        cities.append(queue_left[0])
    
    if queue_left[0] in dic:
        for i in dic[queue_left[0]]:
            if visited[i] == False:
                visited[i] = True
                queue.append([i, queue_left[1] + 1])

cities.sort()

if len(cities) == 0:
    print(-1)
else:
    for i in cities:
        print(i)
