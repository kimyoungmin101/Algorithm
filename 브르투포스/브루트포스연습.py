import imp
import re
N = 5



arr = [[0 for _ in range(N)] for _ in range(N)]

visited = [[False for _ in range(N)] for _ in range(N)]
can_visited = [[False for i in range(N)] for _ in range(N)]

def recursive(X):
    
    if len(X) == 3:
        for i in range(1, len(X)):
            if ((X[i][0] < X[i-1][0]) and (X[i][1] < X[i-1][1])) or ((X[i][0] == X[i-1][0]) and (X[i][1] < X[i-1][1])) or (X[i][0] < X[i-1][0]):
                return
        print(X[0], X[1], X[2])
        return
    
    for i in range(N):
        for j in range(N):
            if (visited[i][j] == False):
                visited[i][j] = True
                X.append([i,j])
                recursive(X)
                X.pop()
                visited[i][j] = False


recursive([])