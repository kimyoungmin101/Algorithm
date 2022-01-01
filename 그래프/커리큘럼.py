from collections import deque
import copy

v = int(input())

indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]

time = [0] * (v+1)

for i in range(1, v+1):
    data = list(map(int ,input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        if x == -1:
            break
        else:
            indegree[i] += 1
            graph[x].append(i)


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft() # 1

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, len(result)):
        print(result[i])         

topology_sort()

'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

< 이것이 코딩테스트다 P305 >
'''