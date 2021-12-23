'''
입력
3 2 1
1 2 4
1 3 2

출력 2 4

첫 째줄에 도시의개수 N 통로의 개수 M 메시지를 보내고자 하는 도시 C가 있다.
둘째 줄 부터 M+1 번째 줄에 걸쳐서 통로에 대한 정보 X Y Z가 주어진다. 이는 특정 도시 X에서 
다른 특정 도시 Y로 이어지는 통로가 있으며
메시지가 전달되는 시간이 Z라는 의미이다.
첫째줄 도시 C에서 보낸 메시지를 받는 도시의 총개수와 총 걸리는 시간을 공백으로 구분하여 출력한다.
'''


import sys
from queue import PriorityQueue

N, M, C = map(int , input().split())

dic_arr = {}
weight = [sys.maxsize for _ in range(N)]

for i in range(M):
    X, Y, Z = map(int, input().split())
    if X not in dic_arr:
        dic_arr[X] = [[Z, Y, X]]
    else:
        A = dic_arr[X].copy()
        A.append([Z,Y, X])
        dic_arr[X] = A

def dkstra(start):
    queue = PriorityQueue()
    for i in dic_arr[start]:
        queue.put(i)
    weight[start-1] = 0

    while queue.qsize() != 0:
        next_go = queue.get() # [2,3,1]
        if next_go[0] + weight[next_go[2]-1] < weight[next_go[1]-1]:
            weight[next_go[1]-1] = next_go[0] + weight[next_go[2]-1]
            if next_go[1] in dic_arr:
                for j in dic_arr[next_go[1]]:
                    queue.put(j)
    return

dkstra(C)

cnt = 0
max_size = 0

for i in weight:
    if i == 0 or i == sys.maxsize:
        continue
    else:
        if i > max_size:
            max_size = i
        cnt += 1

print(cnt, max_size)

'''
Solution

이 문제는 한 도시에서 다른 도시 까지의 최단거리 문제로 치환할 수 있으므로 다익스트라 알고리즘을
이용해서 풀 수 있다. 또한 N과 M의 범위가 충분히 크기 때문에 우선순위큐를 이용하여 다익스트라 알고맂므을
작성해야 한다.
'''