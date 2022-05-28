# 팀 결성

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

N, M = map(int, input().split())

parent = [_ for _ in range(N + 1)]

def union(X, Y):
    X_parent = find_parent(X)
    Y_parent = find_parent(Y)
    if X_parent < Y_parent:
        parent[Y_parent] = X_parent
    else:
        parent[X_parent] = Y_parent
    

def find_parent(value):
    if parent[value] == value:
        return value
    else:
        return find_parent(parent[value])
    
ans = []
for i in range(M):
    num, A, B = map(int, input().split())
    if num == 0:
        union(A, B)
    else:
        find_A = find_parent(A)
        find_B = find_parent(B)
        
        if find_A == find_B:
            ans.append("YES")
        else:
            ans.append("NO")

print(parent)
for i in ans:
    print(i)