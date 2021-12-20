# 다익스트라 알고리즘 : DP 사용, 우선순위Queue 사용
from queue import PriorityQueue
import sys
import copy

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
start -= 1

dic = {}
INF = 100000000
weight = [INF for _ in range(V)]

for i in range(E):
    u,v,w = map(int, sys.stdin.readline().split())
    if(u-1 not in dic):
        dic[u-1] = [[w, v-1]]
    else:
        A = dic[u-1]
        A.append([w, v-1])

arr_start = []

queue_p = PriorityQueue()

weight[start] = 0

for i in dic[start]:
    queue_p.put((i[0], i[1], 0))
    

while(not queue_p.empty()):
    A = queue_p.get()
    new_weight = A[0] # 2
    next_index = A[1] # 1
    current_weight = A[2] # 0
    
    if(weight[next_index] > new_weight + current_weight):
        weight[next_index] = new_weight + current_weight
        current_weight += new_weight
        if(next_index not in dic):
            continue
        for i in dic[next_index]:
            queue_p.put((i[0], i[1], current_weight))

for i in range(len(weight)):
    if(weight[i] == 100000000):
        sys.stdout.write("INF" + "\n")
    else:
        sys.stdout.write(weight[i] + "\n")
