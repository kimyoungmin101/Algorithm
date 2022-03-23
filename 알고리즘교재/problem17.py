# https://www.acmicpc.net/problem/18405 경쟁적 전염

'''
런타임 에러가 난 이유는 
N, K가 행 열의 길이인줄 착각했다!!
앞으로 잘보고 다시한번 신중하게 글 읽고 풀어보기 !
'''
import heapq

M, K = map(int, input().split())

graph = []
for i in range(M):
    graph.append(list(map(int, input().split())))
    
S, X, Y = map(int, input().split())
X -= 1
Y -= 1
# S초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 출력한다. 만약 S초 뒤에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다.

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

heap = []

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] != 0:
            heapq.heappush(heap, [graph[i][j], i, j])

while S:
    heap_sort = []
    while heap:
        value, A, B = heapq.heappop(heap)
        heap_sort.append([value, A, B])
    S -= 1
    
    for q in heap_sort:
        value = q[0]
        A = q[1]
        B = q[2]
        for i in range(4):
            new_X = A + dx[i]
            new_Y = B + dy[i]
            
            if new_X < 0 or new_Y < 0 or new_X >= len(graph) or new_Y >= len(graph[0]):
                continue
            
            if graph[new_X][new_Y] == 0:
                graph[new_X][new_Y] = value
                heapq.heappush(heap, [graph[new_X][new_Y], new_X, new_Y])

print(graph[X][Y])