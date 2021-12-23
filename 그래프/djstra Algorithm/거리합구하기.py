'''
제한시간 : C/C++(2초)/Java/JS/Python(6초)| 메모리 제한 : 2048MB 


현호는 사내 네트워크 분석 업무를 담당하게 되었다. 현재 사내 네트워크는 N개의 노드를 가지는 트리 형태의 네트워크인데, 이 말은 두 노드간의 연결이 정확히 N-1개 있어서 이 연결만으로 모든 노드간에 통신을 할 수 있다는 뜻이다.

각 노드에 1에서 N사이의 번호를 붙이면 i번째 연결은 xi번 노드와 yi번 노드를 양방향으로 연결하며, 통신에 걸리는 시간은 ti이다. D(i,j)는 i번 노드와 j번 노드 사이의 거리를 나타내는데, i번 노드에서 여러 연결을 거쳐 j번 노드에 도달하기 위해 걸리는 최소 시간이다. 노드를 들를 때 추가적인 작업이 없는 이상적인 시간을 따진다.

현호는 네트워크 분석을 위해 어떤 노드 i를 기준으로 다른 모든 노드 사이와의 거리의 합을 알고 싶다. 즉, 을 알고 싶다.

입력예제 2번을 예로 들면, 다음과 같이 7개의 노드로 이루어진 네트워크로 표현할 수 있다. 각 연결 위에 적힌 수는 t를 나타낸다.

4
1 2 1
2 3 2
3 4 4
'''
import sys
from queue import PriorityQueue

N = int(input()) # 노드의 개수
dic_arr = {}

is_parent = [[False for _ in range(N)] for _ in range(N)]
graph_arr = [[sys.maxsize for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        graph_arr[i][j] = 0


for i in range(N-1):
    A = list(map(int , input().split())) # 1 2 1
    graph_arr[A[0]-1][A[1]-1] = A[2]
    graph_arr[A[1]-1][A[0]-1] = A[2]

    if A[0] not in dic_arr:
        dic_arr[A[0]] = [[A[2], A[1], A[0]]] # distance, Next_Node, Current_Node
        is_parent[A[1]-1][A[0]-1] = [True, A[0]-1] #부모노드를 찾음 9 6
        
    else:
        cnt_dic = dic_arr[A[0]].copy()
        cnt_dic.append([A[2], A[1], A[0]])
        dic_arr[A[0]] = cnt_dic
        is_parent[A[1]-1][A[0]-1] = [True, A[0]-1] #부모노드를 찾음 9 6

    if A[1] not in dic_arr:
        dic_arr[A[1]] = [[A[2], A[0], A[1]]]
    else:
        cnt_dic = dic_arr[A[1]].copy()
        cnt_dic.append([A[2], A[0], A[1]])
        dic_arr[A[1]] = cnt_dic
# dic_arr은 가는 거리도 있지만 오는 거리도 생각해준다, 예를들어 1에서 2로가는 거리가 3이라면 2에서 1로 가는 거리도 3이다.


def dkstra(X): #다익스트라 알고리즘 X는 1부터 N까지의 start지점
    visited = [False for _ in range(N)]
    distance = [sys.maxsize for _ in range(N)] # 거리는 INF(INT형의 최대값)으로 계산
    distance[X-1] = 0 # 0 INF INF 현재 거리 가중치
    visited[X-1] = True
    queue = PriorityQueue() # 우선순위큐이용
    
    for i in dic_arr[X]:
        queue.put(i) # 우선순위큐에 삽입
    
    while queue.qsize() != 0: # 우선순위 queue의 크기가 0일때까지 반복!
        cnt_queue = queue.get() # queue에서 맨앞에있는 배열을 꺼내준다
        if distance[cnt_queue[2]-1] + cnt_queue[0] < distance[cnt_queue[1]-1]:
            distance[cnt_queue[1]-1] = distance[cnt_queue[2]-1] + cnt_queue[0]
            if cnt_queue[1] in dic_arr and visited[cnt_queue[1]-1] == False:
                visited[cnt_queue[1]-1] = True
                for j in dic_arr[cnt_queue[1]]: # 만약 dic_arr에 다음으로 가는 위치가 존재한다면 queue에 넣어준다.
                    queue.put(j) # 큐에 집어넣어준다


    return distance


real_distance = dkstra(1)

for i in is_parent:
    print(i)

for i in range(len(real_distance)):
    distance_sum = 0
    for j in range(len(real_distance)):
        if i == j:
            continue
        if is_parent[i][j] == True: # 1 0
            distance_sum += graph_arr[i][j]
            if i == 2:
                print(distance_sum, j)
            continue
        else:
            if is_parent[j][i] == True:
                distance_sum += graph_arr[j][i]
                continue
            distance_sum += real_distance[i] + real_distance[j] #  2 + 6
            if i == 2:
                print(distance_sum)
    

'''
[0, 5, 2, 8, 6, 3, 14]

38
63
40
62
60
45
92
'''