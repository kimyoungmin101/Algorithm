import imp


dic = {}
result = []

import copy

def dfs(cnt_str, visited):
    global result
    global dic
    
    visited.append(cnt_str)
    if len(visited) == len(tickets) + 1:
        if result == []:
            result = copy.deepcopy(visited)
        return
    
    if cnt_str in dic:
        for i in dic[cnt_str]:
            dfs(i, visited)
            visited = visited[:-1]



def solution(tickets):
    global dic
    global result
    visited = []
    
    tickets = sorted(tickets, key = lambda X : (X[0], X[1]))
    
    for i in tickets:
        if i[0] not in dic:
            dic[i[0]] = [i[1]]
        else:
            dic[i[0]].append(i[1])
    
    dfs('ICN', visited)
    
    return result

tickets = [["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]
print(solution(tickets))