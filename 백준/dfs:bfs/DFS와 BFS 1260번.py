'''
import sys

N, M, V = map(int, sys.stdin.readline().split())

dic = {}

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    if A not in dic:
        dic[A] = [B]
    else:
        C = dic[A]
        C = C.append(B)
    if B not in dic:
        dic[B] = [A]
    else:
        Q = dic[B]
        Q = Q.append(A)

checked = [False] * N

def dfs(dic, V):
    if(checked[V-1] == False):
        checked[V-1] = True # T T F F
        if(V in dic):
            arr = dic[V] # 2, 3, 4
            arr.sort() # 2,3,4
            print(V, end = " ")
            for i in arr: # 2
                dfs(dic, i) # dic, 2 , [1]
        else:
            print(V, end =" ")

checkedb = [False] * N
queue = []

def bfs(dic, V):
    if(checkedb[V-1] == False):
        checkedb[V-1] = True
        if(V not in queue):
            queue.append(V)
            print(V, end = " ")
        arr = dic[V]
        arr.sort() # 2, 3
        while(arr):
            Q = arr.pop(0)
            if(Q not in queue):
                queue.append(Q)
                print(Q, end = " ")
        for i in queue:
            if(checkedb[i-1] == False):
                bfs(dic, i)

dfs(dic, V)
print()
bfs(dic, V)

'''

def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n + 1):
        if visit[i] == 0 and s[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = [v]
    visit[v] = 0
    while(queue):
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, n + 1):
            if visit[i] == 1 and s[v][i] == 1:
                queue.append(i)
                visit[i] = 0

n, m, v = map(int, input().split())
s = [[0] * (n + 1) for i in range(n + 1)]
visit = [0 for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1
    
dfs(v)
print()
bfs(v)
