# 알고리즘 교재 P395

'''
4
6
2
2
3
3
4
4
'''

G = int(input())
P = int(input())

parent = [_ for _ in range(G+1)]

def find_parent(X):
    if parent[X] == X:
        return X
    else:
        return find_parent(parent[X])

def union(X, Y):
    parent_X = find_parent(X)
    parent_Y = find_parent(Y)
    if parent[parent_X] < parent[parent_Y]:
        parent[parent_Y] = parent[parent_X]
    else:
        parent[parent_X] = parent[parent_Y]

cnt = 0
arr = []
for i in range(P):
    arr.append(int(input()))
for i in range(P):
    parent_A = find_parent(arr[i])
    if parent_A == 0:
        break
    cnt += 1
    union(parent_A, parent_A - 1)

print(cnt)