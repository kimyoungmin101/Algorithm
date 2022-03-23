graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

'''
A에서 시작해서 DFS 순으로 탐색 !
'''

def dfs(cnt_str, visited):
    visited.append(cnt_str)
    
    
    for i in graph[cnt_str]:
        if i not in visited:
            dfs(i, visited)
            
    return visited




print(dfs('A', []))