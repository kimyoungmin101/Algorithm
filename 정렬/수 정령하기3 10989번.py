import sys 

N = int(sys.stdin.readline())
visited = [0] * 10001

for i in range(N):
    A = int(sys.stdin.readline())
    visited[A] += 1


for i in range(len(visited)):
    while(visited[i] != 0):
        print(i)
        visited[i] -= 1



