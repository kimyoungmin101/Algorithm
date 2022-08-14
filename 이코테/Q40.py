'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''
import sys
import heapq

N, M = map(int, input().split())

weight = [sys.maxsize for _ in range(N+1)]
weight[0] = 0
weight[1] = 0

dic = {}
for i in range(M):
    X, Y = map(int, input().split())
    if X not in dic:
        dic[X] = [Y]
    else:
        dic[X].append(Y)
    
    if Y not in dic:
        dic[Y] = [X]
    else:
        dic[Y].append(X)

heap = []

heapq.heappush(heap, [0, 1])

while heap:
    A, B = heapq.heappop(heap)
    if B in dic:
        for i in dic[B]:
            if weight[i] > weight[B] + 1:
                weight[i] = weight[B] + 1
                heapq.heappush(heap, [weight[i], i])

max_weight = max(weight)
first = 0

for i, value in enumerate(weight):
    if value == max_weight:
        first = i
        break

print("%d %d %d" %(first, weight[i], weight.count(weight[i])))