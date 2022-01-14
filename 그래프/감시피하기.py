from itertools import combinations
N = int(input())

graph = []

teachers = []
students = []
object_X = []
for i in range(N):
    graph.append(list(map(str, input().split())))



for i in range(N):
    for j in range(N):
        if graph[i][j] == 'T':
            teachers.append([i,j])
        elif graph[i][j] == 'S':
            students.append([i,j])
        else:
            object_X.append([i,j])

combi_object = list(combinations(object_X, 3))


def dfs(new_graph, teacher, direction):
    global N
    X_arr = new_graph.copy()

    dx = teacher[0] + direction[0]
    dy = teacher[1] + direction[1]

    if dx < 0 or dy < 0 or dx >= N or dy >= N:
        return True
    
    if X_arr[dx][dy] == 'X':
        return dfs(X_arr, [dx, dy], direction)
    elif X_arr[dx][dy] == 'S':
        return False
    else:
        return True

def find_bool(X):
    first, second, third = X[0], X[1], X[2]
    new_graph = graph.copy()
    
    new_graph[first[0]][first[1]] = 'O'
    new_graph[second[0]][second[1]] = 'O'
    new_graph[third[0]][third[1]] = 'O'
    
    for i in teachers:
        # 위쪽
        if dfs(new_graph, i, [-1, 0]) == False:
            new_graph[first[0]][first[1]] = 'X'
            new_graph[second[0]][second[1]] = 'X'
            new_graph[third[0]][third[1]] = 'X'
            return False
        # 오른쪽
        if dfs(new_graph, i, [0, 1]) == False:
            new_graph[first[0]][first[1]] = 'X'
            new_graph[second[0]][second[1]] = 'X'
            new_graph[third[0]][third[1]] = 'X'
            return False
        # 아래쪽
        if dfs(new_graph, i, [1, 0]) == False:
            new_graph[first[0]][first[1]] = 'X'
            new_graph[second[0]][second[1]] = 'X'
            new_graph[third[0]][third[1]] = 'X'
            return False
        # 왼쪽
        if dfs(new_graph, i, [0, -1]) == False:
            new_graph[first[0]][first[1]] = 'X'
            new_graph[second[0]][second[1]] = 'X'
            new_graph[third[0]][third[1]] = 'X'
            return False
    
    return True
is_bool = False

for i in combi_object:
    if find_bool(i):
        print('YES')
        is_bool = True
        break

if is_bool == False:
    print('NO')