'''
최소신장트리 에서 이어진 경로 중 가장 거리가 짧은 경로를 알기 위한 알고리즘

7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25

'''

V, E = map(int ,input().split())
cruscal_arr = []
for i in range(E):
    list_arr = list(map(int,input().split()))
    cruscal_arr.append(list_arr)

cruscal_arr = sorted(cruscal_arr, key=lambda X : X[2])
sum_result = 0

parent = [_ for _ in range(V+1)]

def find_parent(parent, X):
    if parent[X] != X:
        parent[X] = find_parent(parent, parent[X])
    return parent[X]

def union_parent(parent, X, Y):
    A = find_parent(parent, X) # 1
    B = find_parent(parent, Y) # 4

    if A < B:
        parent[B] = A
    else:
        parent[A] = B

    
for edge in cruscal_arr:
    A = edge[0] # 3
    B = edge[1] # 4
    C = edge[2] # 7

    if find_parent(parent, A) == find_parent(parent, B):
        continue
    else:
        sum_result += C
        union_parent(parent, A, B)

print(sum_result)