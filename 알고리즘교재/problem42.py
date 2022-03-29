# 탑승구
'''
4
3
4
1
1

4
6
2
2
3
3
4
4

'''

G = int(input()) # 탑승구 개수
P = int(input()) # 비행기 개수

airplains = []

for cnt in range(P):
    airplain = int(input())
    airplains.append(airplain)

docking = [0 for _ in range(G + 1)]
parent = [i for i in range(G + 1)]


def find(X):
    if X == parent[X]:
        return X
    else:
        return find(parent[X])
    
def union(X, Y):
    parent_X = find(X)
    parent_Y = find(Y)
    
    if parent_X < parent_Y:
        parent[parent_Y] = parent_X
    else:
        parent[parent_X] = parent_Y

cnt = 0

for airplain in airplains:
    A = find(airplain) # 2
    
    if A == 0:
        break
    else:
        cnt += 1
        union(A, A-1)
        print(parent)

print(cnt)