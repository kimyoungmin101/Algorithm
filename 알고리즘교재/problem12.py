from itertools import combinations

N, M = map(int, input().split())

graph = []

for i in range(N):
    A = list(map(int, input().split()))
    graph.append(A)

chicken = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chicken.append([i, j])

list_permu = list(combinations(chicken, M))

min_distance = 100000

while list_permu:
    A = list_permu.pop(0)
    distance = 0
    for i in range(N):
        for j in range(N):
            min_dis = 1000000
            if graph[i][j] == 1: # 0,3
                for k in A: # 0,1 / 3.0
                    min_dis = min(min_dis, abs(i-k[0])+abs(j-k[1]))
                distance += min_dis
    min_distance = min(min_distance, distance)

print(min_distance)


