graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1

from collections import deque

def bfs(graph, root):
    visited = []
    queue = deque([root])
    
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

print(bfs(graph_list, root_node))

def BFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

print(BFS_with_adj_list(graph_list, root_node))

list = [[1, 1, 1, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 0, 1], [0, 1, 0, 1, 0], [0, 0 ,1, 0, 1]]
# DFS 순서구하기
answer = []
visited = [0] * len(list)

def dfs(dlist, visited, v):
    stack = []
    if(visited[v] == 0):
        visited[v] = 1

    for i in range(len(dlist[v])):
        if(dlist[v][i] == 1 and visited[i] == 0):
            visited[i] = 1
            stack.append(i)

    stack.sort(reverse = True) # 2 1 / 3
    print(visited)
    print(stack)
    
    while stack:
        n = stack.pop()
        answer.append(n+1)
        dfs(dlist, visited, n)
    
