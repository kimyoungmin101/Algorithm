N, M = map(int, input().split())

'''
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4

'''

from queue import deque

def Union(parent, X, Y):
    find_X = Find(parent, X)
    find_Y = Find(parent, Y)

    if find_X < find_Y:
        parent[find_Y] = find_X
    else:
        parent[find_X] = find_Y

def Find(parent, X):
    if parent[X] != X:
        parent[X] = Find(parent, parent[X])
    return parent[X]

parent = [i for i in range(N+1)]

graph = []

for i in range(M):
    a, b, cost = map(int, input().split())
    graph.append([cost, a, b])

graph = sorted(graph, key = lambda X:X[0])

print(graph)

queue = deque(graph)
weight_sum = 0
max_weight = 0

while queue:
    weight, X, Y = queue.popleft()
    if Find(parent, X) != Find(parent, Y):
        Union(parent, X, Y)
        if weight > max_weight:
            max_weight = weight
        weight_sum += weight

print(weight_sum - max_weight)