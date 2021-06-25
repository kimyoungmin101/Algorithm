import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

arr = [[0] * (N+1) for _ in range(N + 1)]
visited = [False] * N

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    arr[A][B] = 1
    arr[B][A] = 1

stack = []

def dfs(v):
    if(visited[v-1] == False):
        visited[v-1] = True
        stack.append(v)
        for i in range(len(arr[v])):
            if(arr[v][i] == 1):
                dfs(i)

dfs(1)

print(len(stack) - 1)
