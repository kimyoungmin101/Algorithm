from collections import deque
import sys

N, K = map(int, input().split())

queue = deque([[0, N]])
visited = [False] * 100001

def bfs(N):
    while(queue):
        pop = queue.popleft() # 0, 5
        if(pop[1] == K):
            return pop[0]
        if not visited[pop[1]]:
            visited[pop[1]] = True
            if (pop[1]+1) <= 100000:
                queue.append([pop[0]+1, pop[1]+1])
            if (pop[1]-1) >= 0:
                queue.append([pop[0]+1, pop[1]-1])
            if (pop[1]*2) <= 100000:
                queue.append([pop[0]+1, pop[1]*2])
    return pop[0]

print(bfs(N))
