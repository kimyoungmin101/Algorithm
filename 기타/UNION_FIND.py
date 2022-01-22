'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''

N, M = map(int,input().split())

graph = []
parent = [_ for _ in range(N+1)]

def union(X, Y):
    A = find(X)
    B = find(Y)

    if A < B:
        parent[B] = parent[A]
    else:
        parent[A] = parent[B]

def find(X):
    if X == parent[X]:
        return parent[X]
    else:
        return find(parent[X])

for i in range(M):
    A = list(map(int, input().split()))
    if A[0] == 0:
        union(A[1], A[2])
    else:
        Q = find(A[1])
        W = find(A[2])
        if Q == W:
            print('YES')
        else:
            print('NO')



print(parent)