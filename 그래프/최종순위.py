from collections import deque

def topology_sort(indegree, graph):
    result = []
    q = deque()
    visited = [False for _ in range(len(indegree))]
    visited[0] = True
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)
    # 진입 차수가 0인 차수부터 시작,
    if len(q) == 0:
        return False

    while q:
        idx_count = 0
        now = q.popleft() # 1
        result.append(now)
        visited[now] = True

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                idx_count += 1
                q.append(i)
        if idx_count >= 2:
            return '?'
    if False in visited:
        return False

    return result
n = int(input())

for i in range(n):
    t = int(input())
    last_year = list(map(int, input().split()))
    m = int(input())
    change_arr = []

    for j in range(m):
        change_arr.append(list(map(int, input().split())))

    indegree_graph = [[] for _ in range(t+1)]

    for i in range(1, t+1):
        arr = []
        for j in range(len(last_year)):
            if last_year[j] == i:
                break
            arr.append(last_year[j])
        arr.sort()
        indegree_graph[i] = arr

    for change in change_arr:
        A, B = change[0], change[1]
        if B in indegree_graph[A]:
            indegree_graph[A].remove(B)
            indegree_graph[B].append(A)
        else:
            indegree_graph[B].remove(A)
            indegree_graph[A].append(B)
    

    graph = [[] for _ in range(t+1)]

    indegree = [0 for _ in range(t+1)] # 0 0 0 0 0 0
    
    for i in range(1,len(indegree_graph)):
        for j in indegree_graph[i]:
            graph[j].append(i)
    for i in range(1, len(indegree_graph)):
        indegree[i] = len(indegree_graph[i])
    
    
    result_ans = topology_sort(indegree, graph)
    if result_ans == False:
        print("IMPOSSIBLE")
    elif result_ans == '?':
        print("?")
    else:
        for x in result_ans:
            print(x, end = " ")
        print("")