'''
노드 개수 / 간선 개수

6 4
1 4
2 3
2 4
5 6

'''

V, E = map(int, input().split())
parent = [_ for _ in range(V+1)]
root_parent = [_ for _ in range(V+1)]

def find_parent(parent_arr, X):
    if parent_arr[X] != X:
        parent_arr[X] = find_parent(parent_arr, parent_arr[X])
    return parent_arr[X]

def union_parent(parent_arr, X, Y):
    Q = find_parent(parent_arr, X) # 1
    W = find_parent(parent_arr, Y) # 4

    if Q < W:
        parent_arr[W] = Q
    else:
        parent_arr[Q] = W

    return parent_arr

cycle = False

for i in range(E):
    A, B = map(int, input().split())
    
    if find_parent(parent,A) == find_parent(parent, B):
        cycle = True
        break
    else:
        parent = union_parent(parent, A, B)


print(cycle)

print(parent)

for i in range(V+1):
    root_parent[i] = find_parent(parent,i)


print(root_parent)