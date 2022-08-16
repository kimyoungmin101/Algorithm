# 탑승구

G = int(input())
P = int(input())

airplain = []

for i in range(P):
    airplain.append(int(input()))
    
parent = [_ for _ in range(G + 1)]

def find(X):
    if X == parent[X]:
        return X
    else:
        return find(parent[X])

def union(X,Y):
    F_X = find(X)
    F_Y = find(Y)
    
    if F_X < F_Y:
        parent[F_Y] = F_X
    elif F_Y < F_X:
        parent[F_X] = F_Y
    
    return parent

cnt = 0
# 0 1 2 3 4
# 0 1 1 3 4
# 0 0 1 2 4
for i in airplain:
    find_X = find(i) # 1
    
    if find_X == 0:
        break
    union(find_X, find_X - 1)
    cnt += 1


print(cnt)

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