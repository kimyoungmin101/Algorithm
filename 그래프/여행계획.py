# 알고리즘 교재 P393
# 서로소 집합 알고리즘 그래프이론 문제

'''
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
'''

N, M = map(int , input().split())
arr = []
for i in range(N):
    arr.append(list(map(int ,input().split())))

parent = [_ for _ in range(N)]
# 0 1 2 3 4

visited = list(map(int,input().split()))
for i in range(len(visited)):
    visited[i] -= 1

def find_parent(X):
    if parent[X] == X:
        return X
    else:
        return find_parent(parent[X])

def union(A, B):
    A_parent = find_parent(A)
    B_parent = find_parent(B)
    
    if A_parent == B_parent:
        return
    elif A_parent > B_parent:
        parent[A_parent] = B_parent
    else:
        parent[B_parent] = A_parent

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            union(i, j)

parent_value = []

for i in visited:
    parent_value.append(parent[i])

if len(parent_value) != parent_value.count(parent_value[0]):
    print('NO')
else:
    print('YES')
