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

0-> 팀합치기 / 1 -> 같은팀인지 확인
'''

def Find(parent, X):
    if parent[X] == X:
        return parent[X]
    return Find(parent, parent[X])

def Union(parent, X, Y):
    find_X = Find(parent, X)
    find_Y = Find(parent, Y)

    if find_X < find_Y:
        parent[find_Y] = find_X
    else:
        parent[find_X] = find_Y
    
        
    return

N, M = map(int, input().split())

parent = [i for i in range(N + 1)]

for i in range(M):
    Q, A, B = map(int, input().split()) # 0 1 3
    if Q == 0:
        Union(parent, A, B)
    else:
        X = Find(parent, A)
        Y = Find(parent, B)
        if X == Y:
            print('YES')
        else:
            print('NO')

print(parent)